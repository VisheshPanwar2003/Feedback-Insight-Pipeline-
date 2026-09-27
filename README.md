## Task 1: Data Ingestion & Cleaning Pipeline

**Objective:** Establish a robust data pipeline to ingest raw customer feedback and sanitize it for downstream database storage and NLP processing.

**Tech Stack:** Python, Pandas

**Key Implementations:**
* **Missing Value Handling:** Dropped records with missing critical fields (ratings, comments) and imputed missing categorical data (e.g., labeling missing categories as 'uncategorized').
* **Data Normalization:** Standardized text fields by lowercasing and stripping whitespace to ensure consistent grouping later in the pipeline.
* **Deduplication:** Identified and removed exact duplicate records to prevent skewed analytics.
* **Outlier Handling & Constraints:** Enforced strict boundaries on numerical data, filtering out invalid ratings (e.g., ratings > 5).
* **Feature Engineering:** Parsed raw date strings into datetime objects and derived a `year_month` column to enable time-series trend analysis.
* **Pipeline Validation:** Implemented strict Python `assert` checkpoints to guarantee data integrity (zero nulls, bounded ratings, no duplicates) before passing data to the next phase.