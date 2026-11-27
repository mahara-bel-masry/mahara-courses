import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE dim_item(id INTEGER PRIMARY KEY, name TEXT)")
db.execute("CREATE TABLE fact_sales(item_id INTEGER, qty INTEGER)")
ITEMS = [(1, "Pen"), (2, "Book")]
SALES = [(1, 5), (2, 3), (1, 2)]
db.executemany("INSERT INTO dim_item VALUES (?, ?)", ITEMS)
db.executemany("INSERT INTO fact_sales VALUES (?, ?)", SALES)
Q = ("SELECT d.name, SUM(f.qty) FROM fact_sales f "
     "JOIN dim_item d ON d.id = f.item_id "
     "GROUP BY d.name ORDER BY d.name")
for row in db.execute(Q):
    print(row)
