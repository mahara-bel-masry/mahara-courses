# rules not run before: between numbers, blanks vs
# a cell with a space, dates (fixed dates, no TODAY)
import openpyxl, sys, datetime as dt
from openpyxl.formatting.rule import CellIsRule, Rule
from openpyxl.styles import PatternFill
from openpyxl.styles.differential import (
    DifferentialStyle,
)

sys.path.insert(0, "assets")
from common import view

red = PatternFill("solid", start_color="FFC7CE")
grn = PatternFill("solid", start_color="C6EFCE")
yel = PatternFill("solid", start_color="FFEB9C")
amt = [4200, 15800, 9900, 22000, 10000, None, 7300, " "]
wb = openpyxl.Workbook()
ws = wb.active
for i, a in enumerate(amt, 1):
    if a is not None:
        ws.cell(i, 1, a)
        ws.cell(i, 2, a)
    ws.cell(i, 3, dt.date(2026, 3, 1 + i * 3))
    ws.cell(i, 4, dt.date(2026, 3, 1 + i * 3))
ws.conditional_formatting.add(
    "A1:A8",
    CellIsRule(
        "between", ["5000", "12000"], fill=red
    ),
)
dx = DifferentialStyle(fill=yel)
ws.conditional_formatting.add(
    "B1:B8",
    Rule(
        type="containsBlanks",
        formula=["LEN(TRIM(B1))=0"],
        dxf=dx,
    ),
)
ws.conditional_formatting.add(
    "C1:C8",
    CellIsRule(
        "between",
        ["DATE(2026,3,10)", "DATE(2026,3,20)"],
        fill=grn,
    ),
)
ws.conditional_formatting.add(
    "D1:D8",
    CellIsRule(
        "equal", ["DATE(2026,3,16)"], fill=grn
    ),
)
for i, a in enumerate(amt, 1):
    if a is not None:
        ws.cell(i, 5, a)
ws.conditional_formatting.add(
    "E1:E8",
    Rule(
        type="expression",
        formula=["ISBLANK(E1)"],
        dxf=dx,
    ),
)
wb.save("data/extra.xlsx")
g = view("data/extra.xlsx")[0]
hit = lambda c: [i + 1 for i, r in enumerate(g) if r[c]["bg"]][:8]
print("values:", [a for a in amt])
print("between 5000 and 12000 hits rows:", hit(0))
print("blanks rule (LEN TRIM = 0) hits rows:", hit(1))
print("ISBLANK rule hits rows:", hit(4))
print("row 6 is empty, row 8 holds one space")
print(
    "dates:",
    [str(ws.cell(i, 3).value.day) for i in range(1, 9)],
)
print("between 10 Mar and 20 Mar hits rows:", hit(2))
print("equal 16 Mar hits rows:", hit(3))
wb2 = openpyxl.load_workbook("data/extra.xlsx")
for rng, rules in wb2["Sheet"].conditional_formatting._cf_rules.items():
    for r in rules:
        print("saved", rng.sqref, r.type, r.operator, r.formula)
