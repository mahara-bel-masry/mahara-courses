# formula rules: whole row, a missing $, AND/OR,
# banding (invented orders, LibreOffice)
import openpyxl, sys
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import PatternFill

sys.path.insert(0, "assets")
from common import view

yel = PatternFill("solid", start_color="FFEB9C")
rows = [
    ("A1", "Paid", 4200),
    ("A2", "Late", 15800),
    ("A3", "Open", 9900),
    ("A4", "Late", 22000),
    ("A5", "Paid", 10000),
]


def book(path):
    wb = openpyxl.Workbook()
    ws = wb.active
    for i, r in enumerate(rows, 1):
        for c, x in enumerate(r, 1):
            ws.cell(i, c, x)
    return wb, ws


def run(path, rng, f, what):
    wb, ws = book(path)
    ws.conditional_formatting.add(
        rng, FormulaRule([f], fill=yel)
    )
    wb.save(path)
    g = view(path)[0]
    cells = [
        "ABC"[c] + str(r + 1)
        for r in range(5)
        for c in range(3)
        if g[r][c]["bg"]
    ]
    print(what, "->", " ".join(cells))


run("data/f1.xlsx", "A1:C5", '$B1="Late"', "row rule")
run("data/f2.xlsx", "A1:C5", 'B1="Late"', "no dollar")
run(
    "data/f3.xlsx",
    "A1:C5",
    'AND($B1="Late",$C1>20000)',
    "AND",
)
run(
    "data/f4.xlsx",
    "A1:C5",
    'OR($B1="Paid",$C1>20000)',
    "OR",
)
run(
    "data/f5.xlsx",
    "A1:C5",
    "MOD(ROW(),2)=0",
    "banding",
)
