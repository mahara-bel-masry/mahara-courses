# highlight rules: greater than, between, text,
# blanks, dates (invented orders, LibreOffice)
import openpyxl, sys, datetime as dt
from openpyxl.formatting.rule import (
    CellIsRule,
    FormulaRule,
)
from openpyxl.styles import PatternFill

sys.path.insert(0, "assets")
from common import view

red = PatternFill("solid", start_color="FFC7CE")
grn = PatternFill("solid", start_color="C6EFCE")
yel = PatternFill("solid", start_color="FFEB9C")
amt = [4200, 15800, 9900, 22000, 10000, None, 7300]
sts = ["Paid", "Late", "Open", "Late", "Paid", "Open", "Late"]
wb = openpyxl.Workbook()
ws = wb.active
for i, (a, s) in enumerate(zip(amt, sts), 1):
    ws.cell(i, 1, a)
    ws.cell(i, 2, s)
    ws.cell(i, 3, dt.date(2026, 3, 1 + i * 4))
ws["E1"] = dt.date(2026, 3, 15)
ws.conditional_formatting.add(
    "A1:A7",
    CellIsRule("greaterThan", ["10000"], fill=red),
)
ws.conditional_formatting.add(
    "B1:B7",
    CellIsRule("equal", ['"Late"'], fill=yel),
)
ws.conditional_formatting.add(
    "C1:C7",
    FormulaRule(["C1<$E$1"], fill=grn),
)
wb.save("data/highlight.xlsx")
g = view("data/highlight.xlsx")[0]
hit = lambda c: [i + 1 for i, r in enumerate(g) if r[c]["bg"]][:7]
print("amounts", amt)
print("rule >10000 hits rows:", hit(0))
print("rule =Late hits rows:", hit(1))
print("dates before 15 Mar hit rows:", hit(2))
print("blank cell row 6 filled:", bool(g[5][0]["bg"]))
