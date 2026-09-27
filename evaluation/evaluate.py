import sys
import os
import chromadb
from chromadb.utils import embedding_functions
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

# Ensure Python can find our project modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import CHROMA_PATH, EMBEDDING_MODEL

def evaluate_clusters(n_clusters=2):
    """Calculates the Silhouette Score to measure cluster coherence."""
    print("Evaluating Cluster Coherence...")
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    
    collection = chroma_client.get_collection(
        name="feedback_semantic_search",
        embedding_function=sentence_transformer_ef
    )
    
    data = collection.get(include=['embeddings'])
    embeddings = data.get('embeddings', [])
    
    # FIX: Use `is None` and check length to safely handle NumPy arrays
    if embeddings is None or len(embeddings) < 2:
        print("Not enough data to evaluate clusters.")
        return
        
    embeddings_array = np.array(embeddings)
    
    # Fit the model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(embeddings_array)
    
    # Calculate Silhouette Score
    score = silhouette_score(embeddings_array, cluster_labels)
    
    print("-" * 40)
    print(f"Silhouette Score (K={n_clusters}): {score:.4f}")
    print("Range: -1.0 (Worst) to 1.0 (Best)")
    
    if score > 0.15:
        print("Result: ✅ Strong semantic separation. Themes are distinct.")
    elif score > 0.05:
        print("Result: ⚠️ Moderate separation. Themes may overlap slightly.")
    else:
        print("Result: ❌ Weak separation. Consider adjusting K or cleaning text.")
    print("-" * 40)

if __name__ == "__main__":
    evaluate_clusters(n_clusters=2)