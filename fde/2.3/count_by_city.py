orders = [
    {"id": "A1", "city": "Cairo", "total": 448.5},
    {"id": "A2", "city": "Giza", "total": 1250.5},
    {"id": "A3", "city": "Cairo", "total": 150.5},
    {"id": "A4", "city": "Alex", "total": 75.25},
]

per_city = {}
for order in orders:
    city = order["city"]
    per_city[city] = per_city.get(city, 0) + order["total"]

for city, total in per_city.items():
    print(f"{city:<6}{total:>9.2f}")
print("cities:", len(per_city))
