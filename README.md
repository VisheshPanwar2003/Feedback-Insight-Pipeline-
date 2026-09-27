## Task 1: Project Scaffolding & Data Ingestion

**Objective:** Set up the project repository structure and build a robust data pipeline to clean raw customer feedback for downstream processing.

**Tech Stack:** Python, Pandas

**Key Implementations:**
* **Project Scaffolding:** Initialized the directory structure (`analytics/`, `clustering/`, `database/`, `embeddings/`, `evaluation/`, `llm/`) and placeholder files for future tasks.
* **Raw Data (`data/raw_feedback.csv`):** Ingested a sample dataset containing unstructured feedback, missing values, and anomalies to test the cleaning logic.
* **Cleaning Pipeline (`ingestion/clean.py`):**
  * **Missing Value Handling:** Dropped records with missing critical fields and imputed missing categories.
  * **Data Normalization:** Standardized text fields (lowercasing, stripping whitespace) for consistent grouping.
  * **Deduplication:** Identified and removed exact duplicate records.
  * **Outlier Handling:** Enforced strict boundaries on numerical data (filtering out ratings > 5).
  * **Feature Engineering:** Parsed raw dates and derived a `year_month` column for time-series analysis.
  * **Pipeline Validation:** Implemented Python `assert` checkpoints to guarantee data integrity before downstream usage.