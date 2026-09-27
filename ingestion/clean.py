import pandas as pd

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Loads raw feedback CSV and applies strict cleaning rules."""
    print(f"Loading raw data from {filepath}...")
    df = pd.read_csv(filepath)
    
    # 1. Drop rows missing critical fields
    df = df.dropna(subset=['rating', 'comment_text'])
    
    # 2. Impute missing category and normalize casing
    df['category'] = df['category'].fillna('uncategorized')
    df['category'] = df['category'].str.lower().str.strip()
    
    # 3. Remove exact duplicates
    df = df.drop_duplicates()
    
    # 4. Filter ratings strictly to 1-5 bounds (handles anomalies like '6')
    df = df[df['rating'].between(1, 5)]
    df['rating'] = df['rating'].astype(int)
    
    # 5. Parse dates and derive year_month (YYYY-MM)
    df['date'] = pd.to_datetime(df['date'])
    df['year_month'] = df['date'].dt.to_period('M').astype(str)
    
    # Phase 1 Checkpoints (Assertions)
    assert df['rating'].isnull().sum() == 0, "Failure: Null ratings found after cleaning."
    assert df['rating'].between(1, 5).all(), "Failure: Ratings outside 1-5 bounds."
    assert df.duplicated().sum() == 0, "Failure: Duplicate rows remain."
    
    print(f"Cleaning complete. Final dataset shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Test the pipeline from the project root
    cleaned_df = load_and_clean_data('data/raw_feedback.csv')
    print("\nCleaned Data Sample:")
    print(cleaned_df.head())