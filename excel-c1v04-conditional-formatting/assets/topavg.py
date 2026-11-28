# top/bottom, above average, duplicates, unique
# (invented numbers, LibreOffice 26.8.3.1)
import openpyxl, sys
from openpyxl.formatting.rule import Rule
from openpyxl.styles import PatternFill
from openpyxl.styles.differential import (
    DifferentialStyle,
)

sys.path.insert(0, "assets")
from common import view

dx = DifferentialStyle(
    fill=PatternFill("solid", bgColor="FFC7CE")
)
v = [5, 12, 30, 8, 45, 20, 12, 100]
wb = openpyxl.Workbook()
ws = wb.active
for i, x in enumerate(v, 1):
    for c in range(1, 8):
        ws.cell(i, c, x)
R = lambda **k: Rule(dxf=dx, **k)
add = ws.conditional_formatting.add
add("A1:A8", R(type="top10", rank=3))
add("B1:B8", R(type="top10", rank=2, bottom=True))
add(
    "C1:C8",
    R(type="top10", rank=25, percent=True),
)
add("D1:D8", R(type="aboveAverage"))
add(
    "E1:E8",
    R(type="aboveAverage", aboveAverage=False),
)
add("F1:F8", R(type="duplicateValues"))
add("G1:G8", R(type="uniqueValues"))
wb.save("data/topavg.xlsx")
g = view("data/topavg.xlsx")[0]
names = [
    "top 3",
    "bottom 2",
    "top 25 percent",
    "above average",
    "below average",
    "duplicates",
    "unique",
]
print("values:", v)
print("average:", sum(v) / len(v))
for c, n in enumerate(names):
    got = [x for x, r in zip(v, g) if r[c]["bg"]]
    print(n + ":", got)
