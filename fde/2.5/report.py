from helpers import clean_name, paid_total

rows = [
    {"status": "paid", "total": "448.5"},
    {"status": "pending", "total": "1250.5"},
    {"status": "paid", "total": "150.5"},
]
print(clean_name("  mona ali "))
print(paid_total(rows))
