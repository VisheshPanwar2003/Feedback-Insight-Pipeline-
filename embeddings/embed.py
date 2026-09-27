import sqlite3
import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import sys
import os

# Ensure Python can find our project modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import DB_PATH, CHROMA_PATH, EMBEDDING_MODEL

def generate_and_store_embeddings():
    """Generates text embeddings and stores them in a local vector database."""
    print("Fetching unstructured text from SQLite...")
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT feedback_id, comment_text, category, rating FROM feedback", conn)
    conn.close()

    if df.empty:
        print("Error: No data found in SQLite.")
        return

    print(f"Initializing ChromaDB vector store at {CHROMA_PATH}...")
    chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
    
    # Initialize the open-source Transformer model
    print(f"Loading embedding model: {EMBEDDING_MODEL} (This may take a moment to download on first run)...")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)
    
    # Create or connect to the collection
    collection = chroma_client.get_or_create_collection(
        name="feedback_semantic_search",
        embedding_function=sentence_transformer_ef
    )
    
    # ChromaDB requires IDs to be strings
    documents = df['comment_text'].tolist()
    ids = [str(fid) for fid in df['feedback_id'].tolist()] 
    metadatas = df[['category', 'rating']].to_dict('records')

    print(f"Vectorizing {len(documents)} feedback comments...")
    collection.upsert(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )
    
    print("Success! Vectors stored in ChromaDB.")
    print(f"Total documents in vector collection: {collection.count()}")
    
    # Test a quick semantic search
    test_query = "The app is crashing"
    print(f"\n--- Testing Semantic Retrieval for: '{test_query}' ---")
    results = collection.query(
        query_texts=[test_query],
        n_results=1
    )
    print(f"Top Match: {results['documents'][0][0]}")
    print(f"Metadata: {results['metadatas'][0][0]}")

if __name__ == "__main__":
    generate_and_store_embeddings()