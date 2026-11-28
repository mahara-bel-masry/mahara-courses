# scenario: a small shop prices items in dollars, one cell holds
# an invented exchange rate, a summary sheet reads the totals
import sys, openpyxl
from openpyxl.formula.translate import Translator
sys.path.insert(0, "assets")
from common import calc

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Prices"
ws["A1"] = "rate"; ws["B1"] = 50
ws.append([])
ws.append(["item", "usd", "qty", "egp each", "egp total"])
items = [("cable", 4, 20), ("mouse", 11, 6), ("stand", 18, 4),
         ("hub", 25, 3)]
for i, (n, u, q) in enumerate(items, 4):
    ws.cell(i, 1, n); ws.cell(i, 2, u); ws.cell(i, 3, q)
    ws.cell(i, 4, Translator("=B4*$B$1", origin="D4")
            .translate_formula(f"D{i}"))
    ws.cell(i, 5, Translator("=D4*C4", origin="E4")
            .translate_formula(f"E{i}"))
ws["E8"] = "=SUM(E4:E7)"
s = wb.create_sheet("Summary")
s["A1"] = "total egp"; s["B1"] = "=Prices!E8"
s["A2"] = "rate used"; s["B2"] = "=Prices!B1"
s["A3"] = "total usd"; s["B3"] = "=B1/B2"
wb.save("data/scenario.xlsx")
print("formulas D4:", ws["D4"].value, "D7:", ws["D7"].value,
      "E4:", ws["E4"].value, "E7:", ws["E7"].value)
w = calc("data/scenario.xlsx")
p, sm = w["Prices"], w["Summary"]
print("egp each:", [p[f"D{r}"].value for r in range(4, 8)])
print("egp total:", [p[f"E{r}"].value for r in range(4, 8)])
print("sum E8:", p["E8"].value, "| Summary B1,B2,B3:",
      sm["B1"].value, sm["B2"].value, sm["B3"].value)
# change the rate in the one cell
ws["B1"] = 55
wb.save("data/scenario_55.xlsx")
w = calc("data/scenario_55.xlsx")
print("after rate 55: E8 =", w["Prices"]["E8"].value,
      "| Summary B1 =", w["Summary"]["B1"].value,
      "| B3 =", w["Summary"]["B3"].value)

# the same sheet, but the rate reference is left relative
wb2 = openpyxl.load_workbook("data/scenario.xlsx")
w2 = wb2["Prices"]
for i in range(4, 8):
    w2.cell(i, 4, Translator("=B4*B1", origin="D4")
            .translate_formula(f"D{i}"))
print("relative rate, formulas D4..D7:",
      [w2[f"D{r}"].value for r in range(4, 8)])
wb2.save("data/scenario_rel.xlsx")
c = calc("data/scenario_rel.xlsx")["Prices"]
print("relative rate egp each:", [c[f"D{r}"].value for r in range(4, 8)])
print("relative rate E8:", c["E8"].value)
