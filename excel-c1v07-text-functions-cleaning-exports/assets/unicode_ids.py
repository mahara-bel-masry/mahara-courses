# UNICODE of the last character, and a fixed MID position on ids of different lengths
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid
NB = "\u00a0"
last = [("nbsp at the end", "EG-CAI-00123" + NB), ("tab at the end", "EG-CAI-00123\t"),
        ("space at the end", "EG-CAI-00123 "), ("clean code", "EG-CAI-00123")]
ids = ["INV/2026/0042", "INV/26/0042", "INVOICE/2026/0042", "INV/2026/42"]
wb = openpyxl.Workbook(); ws = wb.active
for r, (_, v) in enumerate(last, 1):
    ws.cell(r, 1, v)
    ws.cell(r, 2, f"=LEN(A{r})")
    ws.cell(r, 3, f"=_xlfn.UNICODE(RIGHT(A{r},1))")
for r, v in enumerate(ids, 6):
    ws.cell(r, 1, v)
    ws.cell(r, 2, f"=LEN(A{r})")
    ws.cell(r, 3, f"=MID(A{r},5,4)")
    ws.cell(r, 4, f'=MID(A{r},FIND("/",A{r})+1,FIND("/",A{r},FIND("/",A{r})+1)-FIND("/",A{r})-1)')
wb.save("data/unicode_ids.xlsx")
g = csvgrid("data/unicode_ids.xlsx")
for i, (n, _) in enumerate(last):
    print(n, "| LEN", g[i][1], "| UNICODE of last char", g[i][2])
for i, v in enumerate(ids, 5):
    print("id", v, "| LEN", g[i][1], "| MID 5,4 ->", repr(g[i][2]), "| year by FIND ->", repr(g[i][3]))
