import csv

rows = [{"id": "A1", "city": "Cairo", "total": 448.5}, {"id": "A2", "city": "Giza", "total": 1250.5}]
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "city", "total"])
    writer.writeheader()
    writer.writerows(rows)
with open("out.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row["id"], row["total"])
