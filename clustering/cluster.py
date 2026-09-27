import sys
import os
import chromadb
from chromadb.utils import embedding_functions
from sklearn.cluster import KMeans
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import CHROMA_PATH, EMBEDDING_MODEL

def cluster_feedback(n_clusters=2):
    """Fetches embeddings from ChromaDB and groups them using K-Means."""
    print("Connecting to ChromaDB...")
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    
    collection = chroma_client.get_collection(
        name="feedback_semantic_search",
        embedding_function=sentence_transformer_ef
    )
    
    # Extract all data and embeddings
    data = collection.get(include=['embeddings', 'documents', 'metadatas'])
    embeddings = data.get('embeddings', [])
    documents = data.get('documents', [])
    metadatas = data.get('metadatas', [])
    
    # FIX: Check length to safely handle NumPy arrays
    if embeddings is None or len(embeddings) == 0:
        print("No embeddings found. Run embeddings/embed.py first.")
        return pd.DataFrame()
        
    print(f"Applying K-Means clustering (K={n_clusters}) to {len(embeddings)} records...")
    
    # Initialize and fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(embeddings)
    
    # Combine results into a DataFrame for readability
    results_df = pd.DataFrame({
        'Cluster_ID': cluster_labels,
        'Comment': documents,
        'Category': [meta['category'] for meta in metadatas],
        'Rating': [meta['rating'] for meta in metadatas]
    })
    
    # Sort by cluster so we can easily read grouped comments
    results_df = results_df.sort_values(by='Cluster_ID')
    return results_df

if __name__ == "__main__":
    clustered_df = cluster_feedback(n_clusters=2)
    
    if not clustered_df.empty:
        print("\n--- Semantic Clustering Results ---")
        for cluster_id, group in clustered_df.groupby('Cluster_ID'):
            print(f"\nCluster {cluster_id}:")
            for _, row in group.iterrows():
                print(f" - [{row['Rating']} Star | {row['Category']}] {row['Comment']}")