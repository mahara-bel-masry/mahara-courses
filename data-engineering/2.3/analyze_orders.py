lines = [
    "ORD-7001 | 3 | 150.50",
    "ORD-7002 | 1 | 75.25",
    "ORD-7001 | 2 | 150.50",
]

orders = []
for line in lines:
    parts = line.split("|")
    order = {
        "id": parts[0].strip(),
        "qty": int(parts[1].strip()),
        "price": float(parts[2].strip()),
    }
    orders.append(order)

unique_ids = set()
for order in orders:
    unique_ids.add(order["id"])

total = 0
for order in orders:
    total += order["qty"] * order["price"]

print(f"line items: {len(orders)}")
print(f"unique orders: {len(unique_ids)}")
print(f"total sales: {total:.2f} EGP")
