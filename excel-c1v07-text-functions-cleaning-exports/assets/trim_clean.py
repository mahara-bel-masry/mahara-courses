# what TRIM and CLEAN do to a messy export, measured in LibreOffice
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc

NB = "\u00a0"
cases = [
    ("two spaces inside", "Cairo  Branch"),
    ("lead and trail", "  Cairo Branch  "),
    ("tab at the end", "Cairo Branch\t"),
    ("line break inside", "Cairo\nBranch"),
    ("nonbreaking space", "Cairo" + NB + "Branch"),
    ("nbsp at the end", "Cairo Branch" + NB),
]
wb = openpyxl.Workbook()
ws = wb.active
for r, (_, v) in enumerate(cases, 1):
    ws.cell(r, 1, v)
    ws.cell(r, 2, f"=LEN(A{r})")
    ws.cell(r, 3, f"=TRIM(A{r})")
    ws.cell(r, 4, f"=LEN(C{r})")
    ws.cell(r, 5, f"=CLEAN(A{r})")
    ws.cell(r, 6, f"=LEN(E{r})")
    ws.cell(r, 7, f"=TRIM(CLEAN(A{r}))")
    ws.cell(r, 8, f"=LEN(G{r})")
    ws.cell(r, 9, f'=TRIM(SUBSTITUTE(A{r},CHAR(160)," "))')
    ws.cell(r, 10, f"=LEN(I{r})")
    ws.cell(r, 11, f'=TRIM(SUBSTITUTE(A{r},_xlfn.UNICHAR(160)," "))')
    ws.cell(r, 12, f"=LEN(K{r})")
    ws.cell(r, 13, f"=CLEAN(A{r})")
wb.save("data/trim_clean.xlsx")
w = calc("data/trim_clean.xlsx").active
print("case | LEN | TRIM len | CLEAN len | TRIM(CLEAN) len | CHAR160 fix len | UNICHAR160 fix len")
for r, (n, v) in enumerate(cases, 1):
    g = lambda c: w.cell(r, c).value
    print(n, "|", g(2), "|", g(4), "|", g(6), "|", g(8), "|", g(10), "|", g(12))
wb2 = openpyxl.Workbook()
w2 = wb2.active
w2["A1"] = "=_xlfn.UNICODE(CHAR(160))"
w2["A2"] = "=_xlfn.UNICODE(_xlfn.UNICHAR(160))"
w2["A3"] = "=_xlfn.UNICODE(CHAR(9))"
wb2.save("data/char160.xlsx")
c = calc("data/char160.xlsx").active
print("UNICODE of CHAR(160) in this LibreOffice ->", c["A1"].value)
print("UNICODE of UNICHAR(160) ->", c["A2"].value)
print("text after CLEAN, line break case ->", repr(w.cell(4, 13).value))
