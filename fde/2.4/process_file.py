import csv

with open("orders.csv", newline="") as f:
    rows = list(csv.DictReader(f))
total = 0
for row in rows:
    if row["status"] != "paid":
        continue
    total += float(row["total"])
print("rows:", len(rows))
print("paid total:", total)
