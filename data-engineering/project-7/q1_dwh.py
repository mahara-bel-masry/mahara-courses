import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE dim_city(id INT, name TEXT)")
db.execute("CREATE TABLE fact_sales(city_id INT, total INT)")
DIM = [(1, "Cairo"), (2, "Giza")]
db.executemany("INSERT INTO dim_city VALUES (?, ?)", DIM)
FACT = [(1, 10), (1, 30), (2, 20)]
db.executemany("INSERT INTO fact_sales VALUES (?, ?)", FACT)
Q = "SELECT d.name, SUM(f.total) FROM fact_sales f "
Q += "JOIN dim_city d ON d.id = f.city_id GROUP BY d.name ORDER BY d.name"
print(db.execute(Q).fetchall())
