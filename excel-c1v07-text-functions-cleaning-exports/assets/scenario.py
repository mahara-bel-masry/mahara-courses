# a made-up shop export, cleaned with the six functions
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid

NB = "\u00a0"
rows = [
    (" EG-CAI-00123 ", "Mona  Hassan", "010-1234-5678\t"),
    ("EG-ALX-00045" + NB, "Omar\nAli", "011-2222-3333"),
    ("EG-GIZ-00871", "  Sara Nabil ", ""),
    (NB + "EG-CAI-00124", "Hany  Samir", "012-4444-5555"),
    ("EG-ALX-00046 ", "Laila Adel", "015-6666-7777\n"),
    ("EG-CAI-00125", "Karim  Fouad", "010-8888-9999"),
]
wb = openpyxl.Workbook()
ws = wb.active
hdr = ["code raw", "name raw", "phone raw", "code", "name", "phone",
       "country", "city", "serial", "label"]
ws.append(hdr)
for r, (a, b, c) in enumerate(rows, 2):
    ws.cell(r, 1, a)
    ws.cell(r, 2, b)
    ws.cell(r, 3, c)
    ws.cell(r, 4, f'=TRIM(SUBSTITUTE(A{r},_xlfn.UNICHAR(160)," "))')
    ws.cell(r, 5, f'=TRIM(CLEAN(SUBSTITUTE(B{r},CHAR(10)," ")))')
    ws.cell(r, 6, f'=SUBSTITUTE(TRIM(CLEAN(C{r})),"-","")')
    ws.cell(r, 7, f"=LEFT(D{r},2)")
    ws.cell(r, 8, f"=MID(D{r},4,3)")
    ws.cell(r, 9, f"=VALUE(RIGHT(D{r},5))")
    ws.cell(r, 10, f'=_xlfn.TEXTJOIN(" | ",TRUE,E{r},H{r},F{r})')
ws["L1"] = '=MATCH("EG-CAI-00123",A2:A7,0)'
ws["L2"] = '=MATCH("EG-CAI-00123",D2:D7,0)'
ws["L3"] = '=COUNTIF(A2:A7,"EG-CAI-*")'
ws["L4"] = '=COUNTIF(D2:D7,"EG-CAI-*")'
ws["L5"] = "=SUMPRODUCT(LEN(A2:A7))"
ws["L6"] = "=SUMPRODUCT(LEN(D2:D7))"
ws["L7"] = "=SUMPRODUCT(LEN(B2:B7))"
ws["L8"] = "=SUMPRODUCT(LEN(E2:E7))"
ws["N1"] = "=TRIM(CLEAN(B3))"
ws["O1"] = "=LEFT(A2,2)"
ws["O2"] = "=MID(A2,4,3)"
ws["O3"] = "=LEN(LEFT(A2,2))"
ws["O4"] = "=LEFT(D2,2)"
wb.save("data/scenario.xlsx")
g = csvgrid("data/scenario.xlsx")
for r in range(1, 7):
    print("row", r + 1, "|", " | ".join(g[r][3:10]))
print("name in row 3 with CLEAN only (no SUBSTITUTE) ->", g[0][13])
print("raw code in row 2: LEFT 2 ->", repr(g[0][14]), "| MID 4,3 ->", repr(g[1][14]))
print("cleaned code in row 2: LEFT 2 ->", repr(g[3][14]))
print("per-row LEN raw code ->", [len(g[i+1][0]) for i in range(6)], "| LEN clean code ->", [len(g[i+1][3]) for i in range(6)])
names = ["MATCH raw code", "MATCH cleaned code", "COUNTIF raw EG-CAI-",
         "COUNTIF cleaned EG-CAI-", "total length raw codes",
         "total length cleaned codes", "total length raw names",
         "total length cleaned names"]
for i, n in enumerate(names):
    print(n, "->", g[i][11])
