# number, percent, thousands scaling, sections,
# conditions, text, leading zeros, phone (LibreOffice
# 26.8.3.1, invented values)
import openpyxl, sys

sys.path.insert(0, "assets")
from common import shown

cases = [
    (1234567.891, "General"),
    (1234567.891, "#,##0.00"),
    (1234567.891, "0"),
    (0.08, "0%"),
    (2.8, "0%"),
    (0.0825, "0.0%"),
    (8.9, "#.00"),
    (8.9, "#.##"),
    (0.47, "#.##"),
    (0.47, "0.##"),
    (12000, "#,###"),
    (12000, "#,"),
    (12200000, '0.0,,"M"'),
    (12200000, "0.00E+00"),
    (1234.5, '#,##0.00" EGP"'),
    (-1234.5, "#,##0.00;[Red]-#,##0.00"),
    (0, '#,##0.00;-#,##0.00;"-"'),
    (-5, '0;-0;"zero";"text:"@'),
    (0, '0;-0;"zero";"text:"@'),
    ("abc", '0;-0;"zero";"text:"@'),
    (50, "[Red][<=100]0;[Blue][>100]0"),
    (150, "[Red][<=100]0;[Blue][>100]0"),
    (42, "00000"),
    (7, "000"),
    (123456789, "General"),
    (123456789012, "General"),
    (0.000012345, "General"),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "n"
for i, (v, f) in enumerate(cases, 1):
    ws.cell(i, 1, v)
    ws.cell(i, 2, f)
    ws.cell(i, 3, v).number_format = f
wb.save("data/t1.xlsx")
rows = shown("data/t1.xlsx")["n"]
for (v, f), r in zip(cases, rows):
    print(f"value={v!r} format={f} shown={r[2]}")
