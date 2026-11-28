# solution: one formula, C5, with mixed references,
# then a second grid that adds tax using an absolute cell.
import sys, openpyxl
from openpyxl.formula.translate import Translator
sys.path.insert(0, "assets")
from common import calc

wb = openpyxl.load_workbook("lab/lab_refs.xlsx")
ws = wb["Lab"]
f = "=$B5*(1-C$3)"
print("one formula in C5:", f)
for i in range(5, 9):
    for j in range(3, 7):
        ws.cell(i, j, Translator(f, origin="C5")
                .translate_formula(ws.cell(i, j).coordinate))
print("F8 got:", ws["F8"].value, "| D6 got:", ws["D6"].value)
ws["A13"] = "with tax"
g = "=C5*(1+$B$11)"
for i in range(14, 18):
    for j in range(3, 7):
        ws.cell(i, j, Translator(g, origin="C5")
                .translate_formula(ws.cell(i - 9, j).coordinate)
                .replace(f"C{i-9}", ws.cell(i - 9, j).coordinate))
wb.save("lab/sol_refs.xlsx")
w = calc("lab/sol_refs.xlsx")["Lab"]
for i in range(5, 9):
    print(w.cell(i, 1).value, [w.cell(i, j).value for j in range(3, 7)])
print("tax grid formulas:", ws["C14"].value, ws["F17"].value)
for i in range(14, 18):
    print("tax", [round(w.cell(i, j).value, 2) for j in range(3, 7)])
