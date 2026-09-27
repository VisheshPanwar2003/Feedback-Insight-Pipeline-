## Task 3: Structured Analytics Module

**Objective:** Compute quantitative trends to identify underperforming product categories.

**Tech Stack:** Python, Pandas, SQL

**Key Implementations:**
* **SQL Aggregation:** Extracted grouped time-series data calculating average ratings and volume per category.
* **Pandas Processing:** Built filtering logic (`identify_critical_issues`) to isolate categories falling below acceptable rating thresholds.
* **Unit Testing:** Implemented automated tests (`tests/test_trends.py`) to verify the Pandas filtering logic independently of the database.