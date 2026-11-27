import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE sales(month INTEGER, rep TEXT, amount INTEGER);
INSERT INTO sales VALUES (1,'Ali',100),(2,'Ali',150),(3,'Ali',120),
 (1,'Mona',90),(2,'Mona',200),(3,'Mona',60);
""")
run = """SELECT month, amount,
  SUM(amount) OVER (ORDER BY month) AS running
FROM sales WHERE rep = 'Ali'"""
rank = """SELECT rep, amount,
  RANK() OVER (ORDER BY amount DESC) AS pos
FROM sales WHERE month = 2"""
lag = """SELECT month, amount,
  amount - LAG(amount) OVER (ORDER BY month) AS change
FROM sales WHERE rep = 'Mona'"""
for q in (run, rank, lag):
    print(db.execute(q).fetchall())
