# date and time formats, elapsed time, m after h
# (minutes) vs month (LibreOffice 26.8.3.1, invented
# values)
import openpyxl, sys, datetime as dt

sys.path.insert(0, "assets")
from common import shown

d = dt.datetime(2026, 3, 7, 16, 36, 3)
cases = [
    (d, "dd/mm/yyyy"),
    (d, "mm/dd/yyyy"),
    (d, "d-m-yy"),
    (d, "mmm"),
    (d, "mmmm"),
    (d, "ddd"),
    (d, "dddd"),
    (d, "yyyy-mm-dd"),
    (d, "h:mm AM/PM"),
    (d, "hh:mm"),
    (d, "h:mm:ss"),
    (d, "dd/mm/yyyy hh:mm"),
    (1.5, "h:mm"),
    (1.5, "[h]:mm"),
    (2.1, "[h]:mm"),
    (2.1, "h:mm"),
    (0.043, "[mm]:ss"),
    (3735.8 / 86400, "[ss].00"),
    (46088, "General"),
    (46088, "0"),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "d"
for i, (v, f) in enumerate(cases, 1):
    ws.cell(i, 1, v).number_format = f
wb.save("data/t2.xlsx")
rows = shown("data/t2.xlsx")["d"]
for (v, f), r in zip(cases, rows):
    print(f"value={str(v)} " f"format={f} shown={r[0]}")
x = openpyxl.load_workbook("data/t2.xlsx").active
print(
    "value read back by openpyxl," "first cell:",
    x["A1"].value,
    type(x["A1"].value).__name__,
)
print(
    "serial number of 2026-03-07,"
    "days since 1899-12-30:",
    (dt.date(2026, 3, 7) - dt.date(1899, 12, 30)).days,
)
