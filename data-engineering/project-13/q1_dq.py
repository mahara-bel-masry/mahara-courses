rows = [{"id": 1, "age": 30}, {"id": 2, "age": None},
        {"id": 2, "age": 150}]

def check(rows):
    bad = []
    ids = set()
    for r in rows:
        if r["age"] is None:
            bad.append("missing age")
        elif r["age"] > 120:
            bad.append("age too big")
        if r["id"] in ids:
            bad.append("duplicate id")
        ids.add(r["id"])
    return bad

def test_check():
    assert check(rows) == ["missing age", "age too big", "duplicate id"]

test_check()
print("test passed")
print(check(rows))
