# two rules on the same cells: who wins, and what
# stop-if-true is saved as (LibreOffice)
import openpyxl, sys, zipfile, re
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill, Font

sys.path.insert(0, "assets")
from common import view

red = PatternFill("solid", start_color="FFC7CE")
grn = PatternFill("solid", start_color="C6EFCE")
v = [5, 15, 25]


def run(path, first, second, stop=False):
    wb = openpyxl.Workbook()
    ws = wb.active
    for i, x in enumerate(v, 1):
        ws.cell(i, 1, x)
    add = ws.conditional_formatting.add
    add("A1:A3", first)
    add("A1:A3", second)
    wb.save(path)
    g = view(path)[0]
    return [r[0]["bg"] or "none" for r in g]


a = CellIsRule("greaterThan", ["10"], fill=red)
b = CellIsRule("greaterThan", ["20"], fill=grn)
print("values:", v)
print("red >10 added first:", run("data/p1.xlsx", a, b))
a = CellIsRule("greaterThan", ["10"], fill=red)
b = CellIsRule("greaterThan", ["20"], fill=grn)
print("green >20 added first:", run("data/p2.xlsx", b, a))
a = CellIsRule(
    "greaterThan",
    ["10"],
    font=Font(bold=True),
)
b = CellIsRule("greaterThan", ["20"], fill=grn)
print("bold and fill:", run("data/p3.xlsx", a, b))
g = view("data/p3.xlsx")[0]
print("row 3 bold:", g[2][0]["b"], "fill:", g[2][0]["bg"])
for p in ("p1", "p2"):
    z = zipfile.ZipFile(f"data/{p}.xlsx")
    s = z.read("xl/worksheets/sheet1.xml").decode()
    print(p, "priorities:", re.findall(r'priority="(\d+)"', s))
