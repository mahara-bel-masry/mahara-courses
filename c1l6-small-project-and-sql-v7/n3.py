import sqlite3
exec(open("n0.py").read().split("print(")[0])
name = "Giza'; drop table sales; --"
try:
    cur.executescript("select * from branches "
        "where name = '" + name + "'")
except Exception as e:
    print("error:", type(e).__name__, e)
T = "select name from sqlite_master where type='table'"
print("executescript, tables after:", [r[0] for r in cur.execute(T)])
print("placeholder query:", cur.execute("select count(*) from branches "
    "where name = ?", (name,)).fetchone())
exec(open("n0.py").read().split("print(")[0])
try:
    cur.execute("select * from branches where name = '" + name + "'")
except Exception as e:
    print("plain execute:", type(e).__name__, e)
print("plain execute, tables after:", [r[0] for r in cur.execute(T)])
trick = "x' OR '1'='1"
q = "select name from branches where name = '" + trick + "'"
print("plain execute with OR trick:", cur.execute(q).fetchall())
print("placeholder with the same trick:", cur.execute(
    "select name from branches where name = ?", (trick,)).fetchall())
