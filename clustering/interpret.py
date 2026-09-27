import sys
import os
import chromadb
from chromadb.utils import embedding_functions
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import pandas as pd
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import CHROMA_PATH, EMBEDDING_MODEL

def get_cluster_representatives(n_clusters=2):
    """Finds the comment closest to the mathematical center of each cluster."""
    print("Fetching embeddings to interpret clusters...")
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    
    collection = chroma_client.get_collection(
        name="feedback_semantic_search",
        embedding_function=sentence_transformer_ef
    )
    
    data = collection.get(include=['embeddings', 'documents'])
    embeddings = data.get('embeddings', [])
    documents = data.get('documents', [])
    
    if embeddings is None or len(embeddings) == 0:
        return pd.DataFrame()
        
    # Convert list of vectors to NumPy array for fast math
    embeddings_array = np.array(embeddings)
    
    # Fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(embeddings_array)
    
    # Calculate the closest document to each cluster centroid
    # closest_docs will contain the index of the document closest to center
    closest_docs, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, embeddings_array)
    
    representatives = []
    for cluster_id, doc_index in enumerate(closest_docs):
        representatives.append({
            'Cluster_ID': cluster_id,
            'Representative_Comment': documents[doc_index]
        })
        
    return pd.DataFrame(representatives)

if __name__ == "__main__":
    reps_df = get_cluster_representatives(n_clusters=2)
    
    if not reps_df.empty:
        print("\n--- Cluster Representatives (Centroids) ---")
        # Ensure pandas doesn't truncate the comment text in the terminal
        pd.set_option('display.max_colwidth', None)
        print(reps_df.to_string(index=False))