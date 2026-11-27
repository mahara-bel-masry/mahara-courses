import sqlite3
prompt = "Table sales(city, amount). Write SQL: total amount per city."
ai_sql = "SELECT city, SUM(amount) FROM sales GROUP BY city"
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE sales(city TEXT, amount INT)")
db.executemany("INSERT INTO sales VALUES (?, ?)",
               [("cairo", 100), ("giza", 70), ("giza", 5)])
print(sorted(db.execute(ai_sql).fetchall()))
