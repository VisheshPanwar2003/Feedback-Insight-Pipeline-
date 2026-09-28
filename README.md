# Feedback Insight Pipeline

An end-to-end, hybrid analytics pipeline that combines traditional relational data processing (SQL/Pandas) with advanced Natural Language Processing (Semantic Search, Vector Clustering) and Large Language Models (LLMs). This system automatically ingests raw customer feedback, computes quantitative performance metrics, mathematically clusters unstructured text to identify core qualitative themes, and synthesizes the findings into a human-readable AI executive summary.

## Tech Stack
* **Data Processing & Analytics:** Python, Pandas, NumPy
* **Storage & Vectorization:** SQLite, ChromaDB, HuggingFace (`sentence-transformers`)
* **Machine Learning & NLP:** Scikit-Learn (K-Means Clustering, Silhouette Scoring)
* **Generative AI:** Google Gemini API (`google-genai`)

## System Architecture

```text
feedback-insight-pipeline/
├── analytics/
│   └── trends.py           # SQL aggregation and Pandas threshold filtering
├── clustering/
│   ├── cluster.py          # K-Means semantic grouping
│   └── interpret.py        # Centroid extraction via pairwise distances
├── config/
│   └── settings.py         # Centralized paths and model configurations
├── data/
│   └── raw_feedback.csv    # Unstructured raw dataset
├── database/
│   ├── db.py               # SQLite initialization and DataFrame loader
│   └── schema.sql          # Relational table schema
├── embeddings/
│   └── embed.py            # Transformer-based vector generation and ChromaDB upsert
├── evaluation/
│   └── evaluate.py         # Silhouette scoring for cluster coherence
├── ingestion/
│   └── clean.py            # Data sanitization, deduplication, and bounds checking
├── llm/
│   └── explain.py          # Gemini API integration and dynamic prompting
├── tests/
│   └── test_trends.py      # Unit tests for analytics logic
├── .env                    # Environment variables (API keys)
├── .gitignore              # Git exclusions
├── main.py                 # Master pipeline orchestrator
└── requirements.txt        # Project dependencies

Setup & Execution (Windows)
1. Clone and Install Dependencies

PowerShell
git clone [https://github.com/YOUR-USERNAME/Feedback-Insight-Pipeline.git](https://github.com/YOUR-USERNAME/Feedback-Insight-Pipeline.git)
cd Feedback-Insight-Pipeline
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
2. Configure Environment
Create a .env file in the root directory and add your Google Gemini API key:

Plaintext
GEMINI_API_KEY=your_actual_api_key_here
3. Run the Pipeline
Execute the pipeline in the following sequence to build the local databases and generate the final report:

PowerShell
# Step 1: Clean data and load into SQLite
python database/db.py

# Step 2: Generate HuggingFace embeddings and store in ChromaDB
python embeddings/embed.py

# Step 3: Run the orchestrator for full quantitative + qualitative analysis
python main.py
