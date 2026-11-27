import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE cust(id INTEGER PRIMARY KEY, nm TEXT);
CREATE TABLE inv(id INTEGER PRIMARY KEY, cust_id INTEGER, amt REAL, paid INT);
INSERT INTO cust VALUES (1,'Clinic A'),(2,'Shop B'),(3,'Gym C');
INSERT INTO inv VALUES (1,1,100,1),(2,1,50,0),(3,2,70,1);
""")
q1 = "SELECT SUM(amt) FROM inv WHERE paid = 0"
q2 = """SELECT c.nm, SUM(i.amt) FROM cust c
JOIN inv i ON i.cust_id = c.id GROUP BY c.nm ORDER BY 2 DESC LIMIT 1"""
q3 = """SELECT c.nm FROM cust c
LEFT JOIN inv i ON i.cust_id = c.id WHERE i.id IS NULL"""
for q in (q1, q2, q3):
    print(db.execute(q).fetchall())
