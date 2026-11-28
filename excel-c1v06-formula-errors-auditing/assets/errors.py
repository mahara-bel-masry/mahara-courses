# seven error values from LibreOffice, one downstream error,
# and the blank-versus-zero average (LibreOffice, openpyxl 3.1.5)
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc, csvgrid

wb = openpyxl.Workbook()
ws = wb.active
ws["A1"] = 10; ws["A2"] = 0; ws["A3"] = "abc"
ws["C1"] = 5; ws["C2"] = 7
cases = {
    "DIV0": "=A1/A2",
    "NA": "=MATCH(99,C1:C2,0)",
    "NAME": "=SUMM(C1:C2)",
    "NULL": "=SUM(C1:C1 C2:C2)",
    "NUM": "=10^400",
    "NUM2": "=SQRT(-1)",
    "REF": "=INDEX(C1:C2,5)",
    "VALUE": "=A3*2",
}
for i, (k, f) in enumerate(cases.items(), 1):
    ws.cell(i, 5, k)
    ws.cell(i, 6, f)
ws["L1"] = 0
ws["H1"] = "=F1+1"          # downstream of the DIV0 cell
ws["H2"] = "=SUM(F1,5)"
ws["H3"] = "=IFERROR(F1,0)"
ws["H4"] = "=IF(A2,A1/A2,0)"
ws["H5"] = "=IFERROR(F2,\"no match\")"
ws["H6"] = "=SUM(F1:F8)"
ws["H7"] = "=AVERAGE(J1:J4)"
ws["H8"] = "=AVERAGE(K1:K4)"
for r, v in enumerate([10, 20, None, 30], 1):
    ws.cell(r, 10, v)
for r, v in enumerate([10, 20, 0, 30], 1):
    ws.cell(r, 11, v)
wb.save("data/errors.xlsx")
w = calc("data/errors.xlsx").active
g = csvgrid("data/errors.xlsx")
for i, k in enumerate(cases, 1):
    print(f"{k:6} {ws.cell(i, 6).value:22} -> shown:", g[i - 1][5],
          "| saved as:", w.cell(i, 6).value)
print("=F1+1 (cell that holds DIV0) ->", w["H1"].value)
print("=SUM(F1,5) ->", w["H2"].value)
print("=IFERROR(F1,0) ->", w["H3"].value)
print("=IF(A2,A1/A2,0) ->", w["H4"].value)
print("=IFERROR(MATCH miss,'no match') ->", w["H5"].value)
print("=SUM(F1:F8) over the eight cells ->", w["H6"].value)
print("average 10,20,blank,30 ->", w["H7"].value)
print("average 10,20,0,30 ->", w["H8"].value)
