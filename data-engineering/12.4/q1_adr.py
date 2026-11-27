gb = 50
a = {"name": "full scan", "gb_read": gb}
b = {"name": "partitioned", "gb_read": gb * 0.1}
price = 5
for d in (a, b):
    d["cost"] = d["gb_read"] / 1000 * price
    print(d["name"], round(d["cost"], 3))
best = min((a, b), key=lambda d: d["cost"])
print("ADR:", best["name"])
