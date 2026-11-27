order = {"id": "ORD-1", "city": "Cairo", "qty": 3}
print(order["city"])
order["status"] = "paid"
print(order)
print(order.get("phone"))
print(order.get("phone", "unknown"))
for key, value in order.items():
    print(key, "->", value)
