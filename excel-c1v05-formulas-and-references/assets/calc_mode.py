# what the calculation mode looks like inside the saved file
# (LibreOffice run only; no claim about Excel behaviour)
import sys, zipfile, re, openpyxl
from openpyxl.workbook.properties import CalcProperties
sys.path.insert(0, "assets")
from common import calc

for mode in ["auto", "manual"]:
    wb = openpyxl.Workbook()
    wb.calculation = CalcProperties(calcMode=mode, fullCalcOnLoad=False)
    ws = wb.active
    ws["A1"] = 4; ws["A2"] = "=A1*3"
    p = f"data/calc_{mode}.xlsx"
    wb.save(p)
    x = zipfile.ZipFile(p).read("xl/workbook.xml").decode()
    print(mode, "->", re.search(r"<calcPr[^>]*>", x).group(0))
    print("  LibreOffice read A2 =", calc(p).active["A2"].value)
