# second made-up export: invoice ids with slashes, amounts with commas and "EGP"
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid

NB = "\u00a0"
rows = [
    ("INV/2026/0042 ", "1,250 EGP"),
    ("INV/2026/0043", "980 EGP"),
    (NB + "INV/2025/0917", "12,400 EGP"),
    ("INV/2026/0044\t", "75 EGP"),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["id raw", "amount raw", "id", "year", "serial", "id dashed",
           "amount", "amount number"])
for r, (a, b) in enumerate(rows, 2):
    ws.cell(r, 1, a)
    ws.cell(r, 2, b)
    ws.cell(r, 3, f'=TRIM(CLEAN(SUBSTITUTE(A{r},_xlfn.UNICHAR(160)," ")))')
    ws.cell(r, 4, f"=VALUE(MID(C{r},5,4))")
    ws.cell(r, 5, f"=VALUE(RIGHT(C{r},4))")
    ws.cell(r, 6, f'=SUBSTITUTE(C{r},"/","-")')
    ws.cell(r, 7, f'=TRIM(SUBSTITUTE(SUBSTITUTE(B{r},"EGP",""),",",""))')
    ws.cell(r, 8, f"=VALUE(G{r})")
ws["J1"] = "=SUM(B2:B5)"
ws["J2"] = "=SUM(H2:H5)"
ws["J3"] = '=COUNTIF(D2:D5,2026)'
ws["J4"] = "=SUMPRODUCT(LEN(A2:A5))"
ws["J5"] = "=SUMPRODUCT(LEN(C2:C5))"
ws["J6"] = '=MATCH("INV/2026/0044",A2:A5,0)'
ws["J7"] = '=MATCH("INV/2026/0044",C2:C5,0)'
wb.save("data/scenario2.xlsx")
g = csvgrid("data/scenario2.xlsx")
for r in range(1, 5):
    print("row", r + 1, "|", " | ".join(repr(x) for x in g[r][2:8]))
for i, n in enumerate(["SUM raw amounts", "SUM clean amounts",
                       "COUNTIF year 2026", "total length raw ids",
                       "total length clean ids", "MATCH raw id",
                       "MATCH clean id"]):
    print(n, "->", g[i][9])
