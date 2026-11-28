# solution: clean the six problems, show before and after
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid

NB = "\u00a0"
wb = openpyxl.load_workbook("lab/lab_export.xlsx")
ws = wb.active
b = csvgrid("lab/lab_export.xlsx")
print("before: total amount", b[0][7], "| A-103 row", b[1][7],
      "| A-101 row", b[2][7])
ws["I1"] = "code clean"
ws["J1"] = "customer clean"
ws["K1"] = "amount clean"
ws["L1"] = "phone clean"
ws["M1"] = "label"
for r in range(2, 7):
    ws[f"I{r}"] = f'=TRIM(SUBSTITUTE(A{r},_xlfn.UNICHAR(160)," "))'
    ws[f"J{r}"] = f'=TRIM(CLEAN(SUBSTITUTE(B{r},CHAR(10)," ")))'
    ws[f"K{r}"] = f'=VALUE(SUBSTITUTE(C{r},",",""))'
    ws[f"L{r}"] = f'=SUBSTITUTE(TRIM(CLEAN(D{r})),"-","")'
    ws[f"M{r}"] = f'=_xlfn.TEXTJOIN(" | ",TRUE,I{r},J{r},E{r})'
ws["H1"] = "=SUM(K2:K6)"
ws["H2"] = '=MATCH("A-103",I2:I6,0)'
ws["H3"] = '=MATCH("A-101",I2:I6,0)'
wb.save("lab/sol_export.xlsx")
a = csvgrid("lab/sol_export.xlsx")
print("after: total amount", a[0][7], "| A-103 row", a[1][7],
      "| A-101 row", a[2][7])
for r in range(1, 6):
    print("after row", r + 1, "|", " | ".join(a[r][8:13]))
