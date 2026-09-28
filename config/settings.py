import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database paths
DB_PATH = os.path.join(BASE_DIR, 'feedback.sqlite3')
CHROMA_PATH = os.path.join(BASE_DIR, 'chroma_db')

# HuggingFace open-source embedding model
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'