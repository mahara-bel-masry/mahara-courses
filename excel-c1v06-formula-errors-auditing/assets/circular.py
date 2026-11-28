# circular references: direct, range that includes itself, indirect loop
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc, csvgrid
wb = openpyxl.Workbook()
ws = wb.active
ws["A1"] = "=A1+A2"; ws["A2"] = 5
ws["C1"] = 1; ws["C2"] = 2; ws["C3"] = "=SUM(C1:C3)"
ws["E1"] = "=F1+1"; ws["F1"] = "=E1+1"
ws["H1"] = 4; ws["H2"] = "=H1*2"
wb.save("data/circular.xlsx")
w = calc("data/circular.xlsx").active
g = csvgrid("data/circular.xlsx")
pos = {"A1": (0, 0), "C3": (2, 2), "E1": (0, 4), "F1": (0, 5), "H2": (1, 7)}
for c, (r, k) in pos.items():
    print(c, ws[c].value, "-> shown:", g[r][k], "| saved as:", w[c].value)
