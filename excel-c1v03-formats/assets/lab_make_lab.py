# builds lab_formats.xlsx: invented data, every column
# in General so the learner formats it (run from the
# folder root)
import openpyxl, datetime as dt

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "orders"
ws.append(
    [
        "order_no",
        "amount",
        "discount_rate",
        "ship_date",
        "work_hours",
        "phone_digits",
    ]
)
rows = [
    (
        7,
        1234.5,
        0.0825,
        dt.date(2026, 3, 7),
        1.5,
        1012345678,
    ),
    (
        42,
        98000,
        0.1,
        dt.date(2026, 3, 15),
        26.25,
        1098765432,
    ),
    (
        115,
        1250000,
        0.125,
        dt.date(2026, 4, 2),
        50.4,
        1055500123,
    ),
    (3, 0, 0, dt.date(2026, 4, 30), 0, 1000000001),
    (9, -300, 0.05, dt.date(2026, 5, 9), 8, 1120004567),
]
for r in rows:
    ws.append(list(r))
for col in "ABCDEF":
    for c in ws[col][1:]:
        c.number_format = "General"
wb.save("lab/lab_formats.xlsx")
print("lab_formats.xlsx rows:", len(rows))
import sys

sys.path.insert(0, "assets")
from common import shown

print("what the learner sees before formatting:")
for r in shown("lab/lab_formats.xlsx")["orders"]:
    print(" | ".join(r))
