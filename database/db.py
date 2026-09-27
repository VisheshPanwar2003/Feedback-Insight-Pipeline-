import sqlite3
import pandas as pd
import os
import sys

# Ensure Python can find the ingestion module from the project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ingestion.clean import load_and_clean_data

DB_PATH = 'feedback.sqlite3'
SCHEMA_PATH = 'database/schema.sql'

def init_db():
    """Initializes the database schema."""
    print("Initializing database schema...")
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Schema initialized.")

def load_dataframe_to_db(df: pd.DataFrame):
    """Loads a cleaned pandas DataFrame into the SQLite database."""
    print("Loading data into SQLite...")
    conn = sqlite3.connect(DB_PATH)
    
    # Write to SQL using append so it respects our schema constraints
    df.to_sql('feedback', conn, if_exists='append', index=False)
    conn.close()
    print("Data loaded successfully.")

def verify_db_contents() -> pd.DataFrame:
    """Runs a test query to ensure data is queryable via SQL."""
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT category, AVG(rating) as avg_rating, COUNT(*) as count 
        FROM feedback 
        GROUP BY category
    """
    result = pd.read_sql(query, conn)
    conn.close()
    return result

if __name__ == "__main__":
    # 1. Initialize the database
    init_db()
    
    # 2. Get the cleaned data
    df = load_and_clean_data('data/raw_feedback.csv')
    
    # 3. Load into SQLite
    load_dataframe_to_db(df)
    
    # 4. Run verification query
    print("\nDatabase Verification Query (Avg Rating by Category):")
    print(verify_db_contents())