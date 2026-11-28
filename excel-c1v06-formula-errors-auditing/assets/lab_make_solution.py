# solution: fix the six problems and show before and after
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc, csvgrid
wb = openpyxl.load_workbook("lab/lab_audit.xlsx")
ws = wb["Orders"]
b = calc("lab/lab_audit.xlsx")["Orders"]
g = csvgrid("lab/lab_audit.xlsx")
print("before: totals D2..D8", [b[f"D{r}"].value for r in range(2, 9)])
print("before: D10", b["D10"].value, "| H2 shown:", g[1][7])
print("before: shares sum", round(sum(b[f"E{r}"].value for r in (2, 3, 4, 5, 6, 7, 8)), 4))
ws["D4"] = "=B4*C4"                       # 1
ws["B5"] = 3                              # 2
ws["C6"] = 35                             # 3
ws["E3"] = "=D3/$D$10"                    # 4
ws["D10"] = "=SUM(D2:D8)"                 # 5
ws["H2"] = '=IFERROR(INDEX({"North","South"},MATCH(G2,{"o1","o2"},0)),"not found")'   # 6
wb.save("lab/sol_audit.xlsx")
a = calc("lab/sol_audit.xlsx")["Orders"]
print("after: totals D2..D8", [a[f"D{r}"].value for r in range(2, 9)])
print("after: D10", a["D10"].value, "| H2", a["H2"].value)
print("after: shares sum", round(sum(a[f"E{r}"].value for r in (2, 3, 4, 5, 6, 7, 8)), 4))
