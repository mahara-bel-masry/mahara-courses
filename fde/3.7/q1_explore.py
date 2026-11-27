import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE cust(id INTEGER PRIMARY KEY, nm TEXT, city TEXT);
CREATE TABLE inv(id INTEGER PRIMARY KEY, cust_id INTEGER REFERENCES cust(id),
                 amt REAL);
INSERT INTO cust VALUES (1,'Clinic A','Cairo'),(2,'Shop B','Giza');
INSERT INTO inv VALUES (1,1,100),(2,1,50),(3,2,70);
""")
t = "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
c = "PRAGMA table_info(inv)"
f = "PRAGMA foreign_key_list(inv)"
n = "SELECT COUNT(*) FROM inv"
s = "SELECT * FROM inv LIMIT 2"
print(db.execute(t).fetchall())
print([r[1] for r in db.execute(c).fetchall()])
print(db.execute(f).fetchall()[0][2:5])
print(db.execute(n).fetchone())
print(db.execute(s).fetchall())
