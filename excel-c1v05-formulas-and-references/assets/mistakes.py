# common reference mistakes, shown with the translator
# and checked by LibreOffice
import sys, openpyxl
from openpyxl.formula.translate import Translator
sys.path.insert(0, "assets")
from common import calc

# 1 a total range that drifts when copied down
print("SUM(B2:B6) copied from B8 to B9:",
      Translator("=SUM(B2:B6)", origin="B8").translate_formula("B9"))
print("SUM($B$2:$B$6) copied from B8 to B9:",
      Translator("=SUM($B$2:$B$6)", origin="B8").translate_formula("B9"))
# 2 a share of the total with and without the dollar
print("B2/B8 copied from C2 to C3 (wrong):",
      Translator("=B2/B8", origin="C2").translate_formula("C3"))
print("B2/$B$8 copied from C2 to C3:",
      Translator("=B2/$B$8", origin="C2").translate_formula("C3"))
# 3 a dollar on the wrong part of a mixed reference
print("$A2*B$1 copied from B2 to C3:",
      Translator("=$A2*B$1", origin="B2").translate_formula("C3"))
print("A$2*$B1 copied from B2 to C3 (parts swapped):",
      Translator("=A$2*$B1", origin="B2").translate_formula("C3"))

wb = openpyxl.Workbook()
ws = wb.active
vals = [120, 80, 200, 50, 150]
for i, v in enumerate(vals, 2):
    ws.cell(i, 2, v)
ws["B8"] = "=SUM(B2:B6)"
ws["B9"] = Translator("=SUM(B2:B6)", origin="B8").translate_formula("B9")
for i in range(2, 7):
    ws.cell(i, 3, Translator("=B2/B8", origin="C2")
            .translate_formula(f"C{i}"))
    ws.cell(i, 4, Translator("=B2/$B$8", origin="D2")
            .translate_formula(f"D{i}"))
wb.save("data/mistakes.xlsx")
w = calc("data/mistakes.xlsx").active
print("total B8 =", w["B8"].value, "| drifted total B9 =", w["B9"].value,
      "(formula", ws["B9"].value + ")")
print("share without dollar C2..C6:",
      [(round(w.cell(r, 3).value, 3)
        if isinstance(w.cell(r, 3).value, (int, float))
        else str(w.cell(r, 3).value))
       for r in range(2, 7)])
print("share with dollar D2..D6:",
      [round(w.cell(r, 4).value, 3) for r in range(2, 7)])
print("formula in C3:", ws["C3"].value, "| D3:", ws["D3"].value)
