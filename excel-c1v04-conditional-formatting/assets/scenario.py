# imagined company: an invoice tracker with three
# rules, and a rules list read back from the file
import openpyxl, sys, datetime as dt
from openpyxl.formatting.rule import (
    FormulaRule,
    CellIsRule,
)
from openpyxl.styles import PatternFill, Font

sys.path.insert(0, "assets")
from common import view

red = PatternFill("solid", start_color="FFC7CE")
yel = PatternFill("solid", start_color="FFEB9C")
inv = [
    ("INV01", 4200, "Paid", 3),
    ("INV02", 15800, "Open", 5),
    ("INV03", 9900, "Open", 12),
    ("INV04", 22000, "Open", 20),
    ("INV02", 7300, "Paid", 8),
    ("INV05", 12100, "Open", 2),
    ("INV06", 640, "Open", 25),
]
ref = dt.date(2026, 3, 15)
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "tracker"
ws["F1"] = ref
for i, (a, b, c, d) in enumerate(inv, 2):
    ws.cell(i, 1, a)
    ws.cell(i, 2, b)
    ws.cell(i, 3, c)
    ws.cell(i, 4, ref + dt.timedelta(days=d - 10))
ws.conditional_formatting.add(
    "A2:D8",
    FormulaRule(
        ['AND($C2<>"Paid",$D2<$F$1)'],
        fill=red,
    ),
)
ws.conditional_formatting.add(
    "B2:B8",
    CellIsRule(
        "greaterThan",
        ["10000"],
        font=Font(bold=True),
    ),
)
ws.conditional_formatting.add(
    "A2:A8",
    FormulaRule(
        ["COUNTIF($A$2:$A$8,A2)>1"],
        fill=yel,
    ),
)
wb.save("data/tracker.xlsx")
g = view("data/tracker.xlsx")[0]
for i, row in enumerate(inv):
    r = g[i + 1]
    due = ws.cell(i + 2, 4).value.day
    print(
        row[0],
        row[2],
        "due",
        due,
        "A:" + (r[0]["bg"] or "-"),
        "B bold:" + str(r[1]["b"]),
    )
over = sum(1 for r in g[1:8] if r[0]["bg"] == "FFC7CE")
print("rows marked overdue:", over)
print("--- rules read back from the file ---")
wb2 = openpyxl.load_workbook("data/tracker.xlsx")
for rng, rules in wb2["tracker"].conditional_formatting._cf_rules.items():
    for r in rules:
        print(rng.sqref, r.type, r.priority, r.formula)
