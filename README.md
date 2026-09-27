## Task 5: Semantic Clustering (Unsupervised ML)

**Objective:** Automatically categorize unstructured feedback into meaningful themes without relying on explicit tags or keywords.

**Tech Stack:** Python, `scikit-learn` (K-Means), Numpy

**Key Implementations:**
* **Unsupervised Grouping:** Applied K-Means clustering to the high-dimensional ChromaDB vectors to group comments with similar semantic meanings.
* **Array Handling:** Engineered robust data extraction from ChromaDB, handling multi-dimensional NumPy arrays safely for pipeline stability.
* **Insight Generation:** Successfully separated critical support issues from positive UX feedback entirely based on semantic vector proximity.