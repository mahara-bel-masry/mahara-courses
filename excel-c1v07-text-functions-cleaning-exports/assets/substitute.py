# SUBSTITUTE: all matches, one instance, case, removing characters
import sys, openpyxl
sys.path.insert(0, "assets")
from common import csvgrid

wb = openpyxl.Workbook()
ws = wb.active
ws["A1"] = "010-1234-5678"
ws["A2"] = "Quarter 1, 2011"
ws["A3"] = "cairo CAIRO Cairo"
ws["A4"] = "1,250"
ws["A5"] = "A-B-C-D"
f = [
    ('SUBSTITUTE(A1,"-","")', "remove every dash"),
    ('SUBSTITUTE(A1,"-"," ",2)', "only the second dash"),
    ('SUBSTITUTE(A2,"1","2",1)', "first instance of 1"),
    ('SUBSTITUTE(A2,"1","2",3)', "third instance of 1"),
    ('SUBSTITUTE(A2,"1","2",9)', "instance that does not exist"),
    ('SUBSTITUTE(A3,"cairo","X")', "lower case only"),
    ('SUBSTITUTE(A3,"Cairo","X")', "capital C only"),
    ('SUBSTITUTE(A4,",","")', "text left after removing the comma"),
    ('ISNUMBER(SUBSTITUTE(A4,",",""))', "is that result a number"),
    ('VALUE(SUBSTITUTE(A4,",",""))*2', "number after VALUE, times 2"),
    ('SUBSTITUTE(A5,"-",", ")', "dash to comma and space"),
]
for i, (x, _) in enumerate(f, 1):
    ws.cell(i, 4, "=" + x)
wb.save("data/substitute.xlsx")
g = csvgrid("data/substitute.xlsx")
for i, (x, d) in enumerate(f, 1):
    print(x, "->", repr(g[i - 1][3]), "|", d)
