import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, client TEXT, total REAL);
INSERT INTO orders VALUES (1,'Clinic A',100),(2,'Clinic A',50),
 (3,'Shop B',70),(4,'Shop B',30);
""")
a = """SELECT id, client, total,
 SUM(total) OVER (PARTITION BY client ORDER BY id) AS running
FROM orders"""
b = """SELECT client, total FROM (
 SELECT client, total,
  ROW_NUMBER() OVER (PARTITION BY client ORDER BY total DESC) AS rn
 FROM orders) WHERE rn = 1"""
for r in db.execute(a): print(r)
print(sorted(db.execute(b).fetchall()))
