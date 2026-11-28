# LEFT, MID and RIGHT on fixed-position codes, plus the edge cases
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid, calc

wb = openpyxl.Workbook()
ws = wb.active
codes = ["EG-CAI-00123", "EG-ALX-00045", "EG-GIZ-00871"]
for r, c in enumerate(codes, 1):
    ws.cell(r, 1, c)
    ws.cell(r, 2, f"=LEFT(A{r},2)")
    ws.cell(r, 3, f"=MID(A{r},4,3)")
    ws.cell(r, 4, f"=RIGHT(A{r},5)")
    ws.cell(r, 5, f"=ISNUMBER(D{r})")
    ws.cell(r, 6, f"=VALUE(D{r})")
    ws.cell(r, 7, f"=ISNUMBER(F{r})")
edge = [
    "LEFT(A1,50)", "LEFT(A1)", "RIGHT(A1)", "MID(A1,50,3)",
    "MID(A1,10,50)", "MID(A1,0,3)", "MID(A1,4,-1)", "LEFT(A1,0)",
]
for i, e in enumerate(edge, 5):
    ws.cell(i, 1, "=" + e)
ws["A14"] = "=SUM(D1:D3)"
ws["A15"] = "=SUM(F1:F3)"
wb.save("data/extract.xlsx")
g = csvgrid("data/extract.xlsx")
print("code | LEFT 2 | MID 4,3 | RIGHT 5 | ISNUMBER(RIGHT) | VALUE | ISNUMBER")
for r in range(3):
    print(*g[r][:7], sep=" | ")
for i, e in enumerate(edge, 5):
    print(e, "->", repr(g[i - 1][0]))
print("SUM of the RIGHT texts ->", g[13][0])
print("SUM of the VALUE numbers ->", g[14][0])
