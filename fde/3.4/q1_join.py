import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE clients(id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders(id INTEGER PRIMARY KEY, client_id INTEGER, total REAL);
INSERT INTO clients VALUES (1,'Clinic A'),(2,'Shop B'),(3,'Gym C');
INSERT INTO orders VALUES (1,1,100),(2,1,50),(3,2,70);
""")
a = """SELECT c.name, o.total FROM clients c
JOIN orders o ON o.client_id = c.id"""
b = """SELECT c.name, o.total FROM clients c
LEFT JOIN orders o ON o.client_id = c.id"""
print(sorted(db.execute(a).fetchall()))
print(sorted(db.execute(b).fetchall(), key=str))
print(db.execute("SELECT COUNT(*) FROM clients, orders").fetchone())
