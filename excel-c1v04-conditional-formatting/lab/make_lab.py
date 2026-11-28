# makes the lab file: a stock list, no rules yet
# (invented data) tasks are printed below
import openpyxl

items = [
    ("Pen", "North", 40, 3),
    ("Pad", "South", 6, 12),
    ("Ink", "North", 9, 25),
    ("Tape", "South", 55, 4),
    ("Glue", "North", 7, 6),
    ("Clip", "South", 120, 1),
    ("Pen", "South", 15, 3),
    ("Pad", "North", 3, 12),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "stock"
ws.append(["item", "region", "qty", "price"])
for r in items:
    ws.append(list(r))
wb.save("lab/lab_cf.xlsx")
print("saved lab/lab_cf.xlsx with", len(items), "rows")
print("task 1: qty below 10 gets a red fill")
print("task 2: top 2 prices get bold")
print("task 3: whole row when South and qty below 10")
print("task 4: item names that repeat get a yellow fill")
