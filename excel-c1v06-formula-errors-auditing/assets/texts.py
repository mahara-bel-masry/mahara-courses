# numbers stored as text: what SUM and + do in LibreOffice
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc
wb = openpyxl.Workbook()
ws = wb.active
for r, v in enumerate([10, "20", 30, "40"], 1):
    ws.cell(r, 1, v)
ws["C1"] = "=SUM(A1:A4)"
ws["C2"] = "=A1+A2"
ws["C3"] = "=COUNT(A1:A4)"
ws["C4"] = "=COUNTA(A1:A4)"
ws["C5"] = "=ISNUMBER(A2)"
ws["C6"] = "=VALUE(A2)+A1"
wb.save("data/texts.xlsx")
w = calc("data/texts.xlsx").active
for r, l in enumerate(["SUM(A1:A4) with two text numbers", "A1+A2 (10 plus text 20)", "COUNT", "COUNTA", "ISNUMBER(A2)", "VALUE(A2)+A1"], 1):
    print(l, "->", w.cell(r, 3).value)
