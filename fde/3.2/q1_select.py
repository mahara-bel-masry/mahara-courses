import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE tickets(id INTEGER PRIMARY KEY, client TEXT, status TEXT, hours REAL);
INSERT INTO tickets VALUES (1,'Clinic A','open',2.5),(2,'Shop B','closed',1.0),
 (3,'Clinic A','open',4.0),(4,'Shop B','open',0.5);
""")
a = "SELECT client, hours FROM tickets"
b = "SELECT id FROM tickets WHERE status = 'open' AND hours > 1"
c = "SELECT id, hours FROM tickets ORDER BY hours DESC LIMIT 2"
d = "SELECT id FROM tickets WHERE client LIKE 'Clinic%'"
print(db.execute(a).fetchall())
print(db.execute(b).fetchall())
print(db.execute(c).fetchall())
print(db.execute(d).fetchall())
