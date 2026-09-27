DROP TABLE IF EXISTS feedback;

CREATE TABLE feedback (
    feedback_id INTEGER PRIMARY KEY,
    rating INTEGER NOT NULL,
    date DATE NOT NULL,
    product TEXT NOT NULL,
    category TEXT NOT NULL,
    comment_text TEXT NOT NULL,
    year_month TEXT NOT NULL
);