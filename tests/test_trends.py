import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analytics.trends import identify_critical_issues

def test_identify_critical_issues():
    # 1. Arrange: Create mock data
    mock_data = pd.DataFrame({
        'year_month': ['2026-03', '2026-03'],
        'category': ['ui', 'bugs'],
        'avg_rating': [4.5, 2.0],
        'volume': [10, 5]
    })
    
    # 2. Act: Run the function
    critical = identify_critical_issues(mock_data, rating_threshold=3.0)
    
    # 3. Assert: Verify the output
    assert len(critical) == 1, "Failure: Should only identify one critical issue."
    assert critical.iloc[0]['category'] == 'bugs', "Failure: Should identify 'bugs' as critical."
    
    print("test_identify_critical_issues: PASSED")

if __name__ == "__main__":
    test_identify_critical_issues()