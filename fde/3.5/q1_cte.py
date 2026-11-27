import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, client TEXT, total REAL);
INSERT INTO orders VALUES (1,'Clinic A',100),(2,'Clinic A',50),
 (3,'Shop B',70),(4,'Gym C',20);
""")
a = "SELECT AVG(total) FROM orders"
b = """SELECT id, total FROM orders
WHERE total > (SELECT AVG(total) FROM orders)"""
c = """WITH per_client AS (
  SELECT client, SUM(total) AS s FROM orders GROUP BY client)
SELECT client, s FROM per_client WHERE s > 60"""
print(db.execute(a).fetchone())
print(db.execute(b).fetchall())
print(sorted(db.execute(c).fetchall()))
