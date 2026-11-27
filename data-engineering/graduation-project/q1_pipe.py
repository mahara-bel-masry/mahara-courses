import json, sqlite3
api = [{"id": 1, "amount": "100"}, {"id": 2, "amount": "250"},
       {"id": 2, "amount": "250"}, {"id": 3, "amount": None}]
open("raw.json", "w").write(json.dumps(api))
raw = json.load(open("raw.json"))
seen, clean = set(), []
for r in raw:
    if r["amount"] is None or r["id"] in seen:
        continue
    seen.add(r["id"])
    clean.append((r["id"], int(r["amount"])))
db = sqlite3.connect(":memory:")
db.execute("create table sales (id int, amount int)")
db.executemany("insert into sales values (?, ?)", clean)
total = db.execute("select sum(amount) from sales").fetchone()[0]
assert total == 350
print("rows", len(clean), "total", total)
