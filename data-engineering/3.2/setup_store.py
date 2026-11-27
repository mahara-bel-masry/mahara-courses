import sqlite3


def make():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE sales (id INTEGER PRIMARY KEY, product TEXT, city TEXT, qty INTEGER, price REAL)")
    rows = [
        (1, "Laptop", "Cairo", 2, 900.0),
        (2, "Mouse", "Giza", 10, 12.5),
        (3, "Laptop", "Giza", 1, 900.0),
        (4, "Keyboard", "Cairo", 4, 30.0),
        (5, "Mouse", "Cairo", 6, 12.5),
        (6, "Monitor", "Alex", 3, 150.0),
    ]
    conn.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?)", rows)
    return conn
