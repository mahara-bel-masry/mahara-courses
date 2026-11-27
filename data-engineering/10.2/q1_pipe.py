import sqlite3
def extract():
    return [("cairo", 100), ("giza", 80), ("cairo", 50)]
def transform(rows):
    return [(c, a * 2) for c, a in rows]
def load(rows):
    db = sqlite3.connect(":memory:")
    db.execute("create table s(city, amount)")
    db.executemany("insert into s values (?,?)", rows)
    q = "select city, sum(amount) from s group by city"
    return db.execute(q).fetchall()
pipeline = [extract, transform, load]
data = None
for step in pipeline:
    print("run", step.__name__)
    data = step() if data is None else step(data)
print(sorted(data))
