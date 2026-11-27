RAW = [("Pen", "25"), ("Book", "90"), ("Bag", "")]
def as_code(rows):
    out = []
    for n, p in rows:
        if p:
            out.append(int(p))
    return sum(out)
STEPS = [
    ("filter", "price != empty"),
    ("cast", "price int"),
    ("sum", "price"),
]
def as_steps(rows, steps):
    data = [{"price": p} for _, p in rows]
    for kind, _ in steps:
        if kind == "filter":
            data = [d for d in data if d["price"]]
        elif kind == "cast":
            data = [{"price": int(d["price"])} for d in data]
        elif kind == "sum":
            return sum(d["price"] for d in data)
print(as_code(RAW))
print(as_steps(RAW, STEPS))
print(as_code(RAW) == as_steps(RAW, STEPS))
