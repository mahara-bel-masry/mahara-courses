import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE sales(day TEXT, total INTEGER)")
ROWS = [("2026-01", 10), ("2026-01", 5), ("2026-02", 7)]
db.executemany("INSERT INTO sales VALUES (?, ?)", ROWS)
db.execute("CREATE INDEX idx_day ON sales(day)")
Q = "EXPLAIN QUERY PLAN SELECT * FROM sales WHERE day = '2026-02'"
print(db.execute(Q).fetchone()[3])
Q2 = "SELECT SUM(total) FROM sales WHERE day = '2026-01'"
print(db.execute(Q2).fetchone())
