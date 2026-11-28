# TEXTJOIN: delimiter, ignore_empty, a range, and a blank cell
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid

wb = openpyxl.Workbook()
ws = wb.active
for r, v in enumerate(["Mona", None, "Cairo", "Egypt"], 1):
    ws.cell(r, 1, v)
f = [
    'TEXTJOIN(", ",TRUE,A1:A4)',
    'TEXTJOIN(", ",FALSE,A1:A4)',
    'TEXTJOIN("",TRUE,A1:A4)',
    'TEXTJOIN(" - ",TRUE,"a","b","c")',
    'TEXTJOIN(",",TRUE,A1,A2,A3)',
    'LEN(TEXTJOIN(", ",TRUE,A1:A4))',
    'LEN(TEXTJOIN(", ",FALSE,A1:A4))',
]
for i, x in enumerate(f, 1):
    ws.cell(i, 3, "=" + x.replace("TEXTJOIN", "_xlfn.TEXTJOIN"))
wb.save("data/textjoin.xlsx")
g = csvgrid("data/textjoin.xlsx")
for i, x in enumerate(f, 1):
    print(x, "->", repr(g[i - 1][2]))
