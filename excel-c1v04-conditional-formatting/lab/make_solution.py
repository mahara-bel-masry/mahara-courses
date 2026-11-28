# solution: the four rules, checked with the
# colours LibreOffice really draws (invented data)
import openpyxl, sys
from openpyxl.formatting.rule import (
    CellIsRule,
    FormulaRule,
    Rule,
)
from openpyxl.styles import PatternFill, Font
from openpyxl.styles.differential import (
    DifferentialStyle,
)

sys.path.insert(0, "assets")
from common import view

red = PatternFill("solid", start_color="FFC7CE")
yel = PatternFill("solid", start_color="FFEB9C")
org = PatternFill("solid", start_color="F8CBAD")
wb = openpyxl.load_workbook("lab/lab_cf.xlsx")
ws = wb["stock"]
add = ws.conditional_formatting.add
add(
    "A2:D9",
    FormulaRule(
        ['AND($B2="South",$C2<10)'], fill=org
    ),
)
add("C2:C9", CellIsRule("lessThan", ["10"], fill=red))
dx = DifferentialStyle(font=Font(bold=True))
add("D2:D9", Rule(type="top10", rank=2, dxf=dx))
add(
    "A2:A9",
    FormulaRule(
        ["COUNTIF($A$2:$A$9,A2)>1"], fill=yel
    ),
)
wb.save("lab/sol_cf.xlsx")
g = view("lab/sol_cf.xlsx")[0]
name = lambda r: ws.cell(r + 2, 1).value
for i in range(8):
    r = g[i + 1]
    print(
        name(i),
        ws.cell(i + 2, 2).value,
        ws.cell(i + 2, 3).value,
        "A:" + (r[0]["bg"] or "-"),
        "C:" + (r[2]["bg"] or "-"),
        "D bold:" + str(r[3]["b"]),
    )
