import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE tickets(id INTEGER PRIMARY KEY, client TEXT, hours REAL);
INSERT INTO tickets VALUES (1,'Clinic A',2.5),(2,'Shop B',1.0),
 (3,'Clinic A',4.0),(4,'Shop B',0.5),(5,'Gym C',3.0);
""")
a = "SELECT COUNT(*), SUM(hours), AVG(hours) FROM tickets"
b = "SELECT client, COUNT(*), SUM(hours) FROM tickets GROUP BY client"
c = """SELECT client, SUM(hours) AS total FROM tickets
GROUP BY client HAVING total > 3"""
print(db.execute(a).fetchall())
print(sorted(db.execute(b).fetchall()))
print(sorted(db.execute(c).fetchall()))
