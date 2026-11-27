import csv

rows = list(csv.DictReader(open("sales.csv")))

unique = {}
for row in rows:
    unique.setdefault(row["order_id"], row)

orders = list(unique.values())
confirmed = [o for o in orders if o["status"] == "confirmed"]
total = sum(int(o["amount"]) for o in confirmed)

print(f"orders read: {len(rows)}")
print(f"unique orders: {len(orders)}")
print(f"confirmed orders: {len(confirmed)}")
print(f"total confirmed: {total} EGP")
