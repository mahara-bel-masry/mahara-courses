# copy a formula two cells down and two cells right with the
# four reference types (the Microsoft table), using the
# openpyxl formula translator, then a real copy-down check
import sys, openpyxl
from openpyxl.formula.translate import Translator
sys.path.insert(0, "assets")
from common import calc

for f in ["=A1", "=$A$1", "=A$1", "=$A1"]:
    t = Translator(f, origin="A1").translate_formula("C3")
    print("copy from A1 to C3:", f, "->", t)

# invoice: price x qty x (1 + rate), rate in one cell
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Invoice"
ws.append(["item", "price", "qty", "line", "with tax"])
rows = [("pen", 12, 10), ("book", 85, 3), ("bag", 240, 2),
        ("lamp", 150, 4)]
for i, (n, p, q) in enumerate(rows, 2):
    ws.cell(i, 1, n); ws.cell(i, 2, p); ws.cell(i, 3, q)
    ws.cell(i, 4, f"=B{i}*C{i}")
ws["H1"] = "rate"
ws["H2"] = 0.1
ws["E2"] = "=D2*(1+H2)"
for i in range(3, 6):
    # what a drag down does to a relative H2
    ws.cell(i, 5, Translator("=D2*(1+H2)", origin="E2")
            .translate_formula(f"E{i}"))
ws["E7"] = "=D2*(1+$H$2)"
for i in range(3, 6):
    ws.cell(7 + i - 2, 5, Translator("=D2*(1+$H$2)", origin="E7")
            .translate_formula(f"E{7 + i - 2}"))
for r in range(2, 11):
    for c in "DE":
        v = ws[f"{c}{r}"].value
        if v:
            print(f"{c}{r}", v)
wb.save("data/invoice.xlsx")
w = calc("data/invoice.xlsx").active
print("relative rate column E2..E5 values:",
      [w[f"E{r}"].value for r in range(2, 6)])
print("absolute rate column E7..E10 values:",
      [w[f"E{r}"].value for r in range(7, 11)])
