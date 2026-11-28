# audit a made-up sales sheet with five seeded problems.
# my own checker (not Excel's); values come from LibreOffice.
import sys, openpyxl
from openpyxl.formula.translate import Translator
sys.path.insert(0, "assets")
from common import calc
from audit_lib import refs, cells_of, precedents, dependents

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sales"
ws.append(["item", "units", "price", "total", "share"])
rows = [("pen", 10, 12), ("book", 3, 85), ("bag", 2, 240),
        ("lamp", 4, 150), ("desk", 1, 900), ("chair", 5, 400),
        ("shelf", 2, 650)]
for i, (n, u, p) in enumerate(rows, 2):
    ws.cell(i, 1, n); ws.cell(i, 2, u); ws.cell(i, 3, p)
    ws.cell(i, 4, f"=B{i}*C{i}")
    ws.cell(i, 5, f"=D{i}/$D$10")
ws["D5"] = 600                      # problem 1: typed over a formula
ws["B6"] = "1"                      # problem 2: number stored as text
ws["C7"] = None                     # problem 3: empty price
ws["A10"] = "total"
ws["D10"] = "=SUM(D2:D8)"
ws["A9"] = "late item"; ws["B9"] = 2; ws["C9"] = 100
ws["D9"] = "=B9*C9"                 # problem 4: below the SUM range
ws["E9"] = "=D9/$D$10"
ws["E4"] = "=D4/D10"                # problem 5: missing dollar
wb.save("data/audit.xlsx")
vals = calc("data/audit.xlsx")["Sales"]
print("values before: D2..D9 =", [vals[f"D{r}"].value for r in range(2, 10)], "| total D10 =", vals["D10"].value)
print("E4 before:", round(vals["E4"].value, 4), "| E2 before:", round(vals["E2"].value, 4))

def rel(f, origin):
    # formula moved to one far cell (Z100): same text means same pattern
    return Translator(f, origin=origin).translate_formula("Z100")

print("-- error values")
for row in vals.iter_rows():
    for c in row:
        if isinstance(c.value, str) and c.value.startswith("#"):
            print(c.coordinate, c.value)
print("-- numbers stored as text")
for row in ws.iter_rows():
    for c in row:
        if isinstance(c.value, str) and not c.value.startswith("=") \
                and c.value.replace(".", "", 1).isdigit():
            print(c.coordinate, repr(c.value))
print("-- inconsistent with the column pattern")
for col in "DE":
    pats = {}
    for r in range(2, 10):
        f = ws[f"{col}{r}"].value
        if isinstance(f, str) and f.startswith("="):
            pats.setdefault(rel(f, f"{col}{r}"), []).append(f"{col}{r}")
        else:
            pats.setdefault("(not a formula)", []).append(f"{col}{r}")
    main = max(pats, key=lambda k: len(pats[k]))
    for k, v in pats.items():
        if k != main:
            print("column", col, "main pattern", main, "| differs:", v, k)
print("-- formulas that point at empty cells")
for row in ws.iter_rows():
    for c in row:
        if isinstance(c.value, str) and c.value.startswith("="):
            for sh, a, b in refs(c.value, "Sales"):
                for x in cells_of(a, b):
                    if ws[x].value is None:
                        print(c.coordinate, c.value, "points at empty", x)
print("-- SUM ranges that stop short of a number next to them")
f = ws["D10"].value
for sh, a, b in refs(f, "Sales"):
    last = int("".join(ch for ch in b if ch.isdigit()))
    nxt = ws[f"D{last + 1}"].value
    if nxt is not None and last + 1 < 10:
        print("D10", f, "ends at", b, "but D%d holds" % (last + 1), nxt)
print("-- trace (precedents and dependents, my script)")
print("precedents of D10:", [c for s, c in precedents(wb, "Sales", "D10")])
print("direct precedents of E2:", precedents(wb, "Sales", "E2"))
print("dependents of D10:", [c for s, c in dependents(wb, "Sales", "D10")])
print("dependents of B2:", dependents(wb, "Sales", "B2"))

# fix all five and recalculate
ws["D5"] = "=B5*C5"
ws["B6"] = 1
ws["C7"] = 400
ws["D10"] = "=SUM(D2:D9)"
ws["E4"] = "=D4/$D$10"
wb.save("data/audit_fixed.xlsx")
v2 = calc("data/audit_fixed.xlsx")["Sales"]
print("values after: D2..D9 =", [v2[f"D{r}"].value for r in range(2, 10)], "| total D10 =", v2["D10"].value)
print("shares E2..E9 sum =", round(sum(v2[f"E{r}"].value for r in range(2, 10)), 4))
print("shares before E2..E9 sum =", round(sum(vals[f"E{r}"].value for r in range(2, 10)), 4))
