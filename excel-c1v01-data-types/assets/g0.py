# build an invented messy sales export (all data is made up)
import random, datetime as dt
from openpyxl import Workbook
random.seed(7)
wb = Workbook(); ws = wb.active; ws.title = "raw"
ws.append(["order_id","order_date","city","qty","unit_price","phone"])
cities = ["Cairo","Giza","Fayoum","Alexandria"]
for i in range(1, 21):
    d = dt.date(2026, 11, 1) + dt.timedelta(days=i)
    qty = random.randint(1, 9)
    price = random.choice([120, 250, 80, 410])
    # rows 4, 9, 15: numbers stored as TEXT, like a bad export
    q = str(qty) if i in (4, 9, 15) else qty
    p = f"{price}" if i in (4, 9, 15) else price
    ws.append([f"A{1000+i}", d, random.choice(cities), q, p, "01012345678"])
wb.save("data/raw.xlsx")
print("saved raw.xlsx rows:", ws.max_row - 1)
for r in ws.iter_rows(min_row=2, max_row=6, values_only=True): print(r)
