import sqlite3
import pandas as pd
import os
import sys

# Ensure Python can find the database module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db import DB_PATH

def get_monthly_category_trends() -> pd.DataFrame:
    """Queries the database to calculate average rating per category per month."""
    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT 
            year_month, 
            category, 
            ROUND(AVG(rating), 2) as avg_rating,
            COUNT(feedback_id) as volume
        FROM feedback
        GROUP BY year_month, category
        ORDER BY year_month, category;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def identify_critical_issues(trends_df: pd.DataFrame, rating_threshold: float = 3.0) -> pd.DataFrame:
    """Filters trends to identify categories with poor average ratings."""
    critical = trends_df[trends_df['avg_rating'] < rating_threshold]
    return critical.sort_values(by='avg_rating', ascending=True)

if __name__ == "__main__":
    print("--- Monthly Feedback Trends ---")
    trends = get_monthly_category_trends()
    print(trends.to_string(index=False))
    
    print("\n--- Critical Issues (Avg Rating < 3.0) ---")
    critical_issues = identify_critical_issues(trends)
    if critical_issues.empty:
        print("No critical issues found.")
    else:
        print(critical_issues.to_string(index=False))