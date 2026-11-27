import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t (x INTEGER)")
conn.executemany("INSERT INTO t VALUES (?)", [(1,), (None,), (3,)])
print(conn.execute("SELECT COUNT(*), COUNT(x) FROM t").fetchall())
print(conn.execute("SELECT COUNT(*) FROM t WHERE x = NULL").fetchall())
print(conn.execute("SELECT COUNT(*) FROM t WHERE x IS NULL").fetchall())
