import json, sqlite3
docs = [
    {"id": 1, "name": "Clinic A", "tags": ["vip", "cairo"]},
    {"id": 2, "name": "Shop B", "phone": "0100"},
]
text = json.dumps(docs)
back = json.loads(text)
print([sorted(d.keys()) for d in back])
print([d["name"] for d in back if "vip" in d.get("tags", [])])
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE c(id INTEGER, name TEXT, phone TEXT)")
db.execute("INSERT INTO c VALUES (2, 'Shop B', '0100')")
print(db.execute("SELECT name FROM c WHERE phone = '0100'").fetchall())
