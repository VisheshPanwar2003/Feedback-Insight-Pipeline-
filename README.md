<<<<<<< Task-2
## Task 2: SQLite Database Setup

**Objective:** Persist cleaned feedback data in a relational database for structured querying and analytics.

**Tech Stack:** Python (`sqlite3`), SQL

**Key Implementations:**
* **Schema Design:** Designed a normalized schema (`database/schema.sql`) enforcing data types and constraints.
* **Idempotent Setup:** Implemented `DROP TABLE IF EXISTS` to allow repeated test runs during development.
* **Data Loading:** Engineered a loader script (`database/db.py`) to pipe cleaned Pandas DataFrames directly into SQLite using `.to_sql()`.
* **Verification:** Built an automated verification query to ensure data is correctly aggregated using SQL `GROUP BY`.
=======