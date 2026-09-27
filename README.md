## Task 4: Text Embeddings & ChromaDB

**Objective:** Convert unstructured text into mathematical vectors to enable semantic search and clustering.

**Tech Stack:** Python, ChromaDB, HuggingFace (`sentence-transformers`)

**Key Implementations:**
* **Vectorization:** Integrated the `all-MiniLM-L6-v2` open-source Transformer model to convert text comments into 384-dimensional dense vectors.
* **Vector Database:** Initialized a local ChromaDB instance to store the embeddings alongside their SQL metadata (category, rating).
* **Semantic Retrieval:** Verified the pipeline by successfully querying "The app is crashing" to retrieve the comment "App crashes when I try to upload a photo."