# edge cases: blank cells, an error value, numbers
# stored as text (invented data, LibreOffice)
import openpyxl, sys
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill

sys.path.insert(0, "assets")
from common import view

red = PatternFill("solid", start_color="FFC7CE")
wb = openpyxl.Workbook()
ws = wb.active
ws["A1"] = 3
ws["A3"] = 8
ws["B1"] = 3
ws["B2"] = "=1/0"
ws["B3"] = 8
ws["C1"] = 30
ws["C2"] = "50"
ws["C3"] = 50
add = ws.conditional_formatting.add
add("A1:A3", CellIsRule("lessThan", ["5"], fill=red))
add("B1:B3", CellIsRule("lessThan", ["5"], fill=red))
add("C1:C3", CellIsRule("greaterThan", ["40"], fill=red))
wb.save("data/edge.xlsx")
g = view("data/edge.xlsx")[0]
f = lambda c: [bool(r[c]["bg"]) for r in g]
print("blank A2, rule <5 hits A1,A2,A3:", f(0))
print("error B2, rule <5 hits B1,B2,B3:", f(1))
print("text 50 in C2, rule >40:", f(2))
c2 = ws["C2"].value
print("C2 is text:", isinstance(c2, str))
