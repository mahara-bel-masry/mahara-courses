import sqlite3

conn = sqlite3.connect(":memory:")
conn.executescript(open("schema.sql").read())
conn.execute("INSERT INTO customers VALUES (1, 'Mona', 'Cairo')")
try:
    conn.execute("INSERT INTO orders VALUES (10, 99, 5.0)")
except sqlite3.IntegrityError as error:
    print("IntegrityError:", error)
try:
    conn.execute("INSERT INTO customers VALUES (2, NULL, 'Giza')")
except sqlite3.IntegrityError as error:
    print("IntegrityError:", error)
try:
    conn.execute("INSERT INTO customers VALUES (1, 'Dup', 'Giza')")
except sqlite3.IntegrityError as error:
    print("IntegrityError:", error)
