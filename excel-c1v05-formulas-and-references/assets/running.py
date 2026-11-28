# running total with a mixed range, and a reference to another
# sheet copied down (translator for the copy, LibreOffice for values)
import sys, openpyxl
from openpyxl.formula.translate import Translator
sys.path.insert(0, "assets")
from common import calc

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sales"
sales = [300, 450, 200, 500, 350]
for i, v in enumerate(sales, 2):
    ws.cell(i, 1, f"day {i - 1}")
    ws.cell(i, 2, v)
    ws.cell(i, 3, Translator("=SUM($B$2:B2)", origin="C2")
            .translate_formula(f"C{i}"))
    ws.cell(i, 4, Translator("=SUM(B2:B2)", origin="D2")
            .translate_formula(f"D{i}"))
print("C2:", ws["C2"].value, "| C4:", ws["C4"].value, "| C6:", ws["C6"].value)
print("D2:", ws["D2"].value, "| D4:", ws["D4"].value, "| D6:", ws["D6"].value)
r = wb.create_sheet("Report")
r["A1"] = "Sales!B2 copied down:"
for i in range(2, 7):
    r.cell(i, 2, Translator("=Sales!B2", origin="B2")
           .translate_formula(f"B{i}"))
print("Report B2:", r["B2"].value, "| B6:", r["B6"].value)
wb.save("data/running.xlsx")
c = calc("data/running.xlsx")
s, rr = c["Sales"], c["Report"]
print("running total (anchored start):",
      [s[f"C{i}"].value for i in range(2, 7)])
print("no anchor (each row only itself):",
      [s[f"D{i}"].value for i in range(2, 7)])
print("Report column:", [rr[f"B{i}"].value for i in range(2, 7)])
