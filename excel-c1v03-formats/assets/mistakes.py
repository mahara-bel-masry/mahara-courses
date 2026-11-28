# mistakes demo: m after h vs alone, narrow column,
# numbers stored as text, hidden values (invented
# data, LibreOffice 26.8.3.1)
import openpyxl, sys, datetime as dt, subprocess, os

sys.path.insert(0, "assets")
from common import shown

d = dt.datetime(2026, 3, 7, 16, 36, 3)
fm = [
    "mm",
    "m",
    "hh:mm",
    "h:mm:ss",
    "mm:ss",
    "dd/mm",
    "mmm",
]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "m"
for i, f in enumerate(fm, 1):
    ws.cell(i, 1, d).number_format = f
ws2 = wb.create_sheet("narrow")
ws2["A1"] = d
ws2["A1"].number_format = "dd/mm/yyyy"
ws2["B1"] = d
ws2["B1"].number_format = "dd/mm/yyyy"
ws2.column_dimensions["A"].width = 3
ws2.column_dimensions["B"].width = 14
ws3 = wb.create_sheet("text")
ws3["A1"] = 5
ws3["A2"] = 7
ws3["A3"] = "9"
ws3["A4"] = "=SUM(A1:A3)"
ws3["A5"] = "=COUNT(A1:A3)"
ws3["A6"] = "=A3+1"
ws3["A7"] = "=ISTEXT(A3)"
wb.save("data/mistakes.xlsx")
res = shown("data/mistakes.xlsx")
for f, r in zip(fm, res["m"]):
    print(f"format={f} shown={r[0]}")
print(
    "narrow column A (width 3) shows:",
    res["narrow"][0][0],
    "| wide column B (width 14) shows:",
    res["narrow"][0][1],
)
os.makedirs("data/out_m", exist_ok=True)
subprocess.run(
    [
        "soffice",
        "--headless",
        "--convert-to",
        "xlsx:Calc MS Excel 2007 XML",
        "--outdir",
        "data/out_m",
        "data/mistakes.xlsx",
    ],
    capture_output=True,
    timeout=120,
)
x = openpyxl.load_workbook(
    "data/out_m/mistakes.xlsx", data_only=True
)["text"]
print(
    "cells 5, 7 and the text 9: SUM =",
    x["A4"].value,
    "| COUNT =",
    x["A5"].value,
    "| text 9 plus 1 =",
    x["A6"].value,
    "| ISTEXT =",
    x["A7"].value,
)

# more mistakes: percent typed as 25, date as text
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "p"
ws["A1"] = 25
ws["A1"].number_format = "0%"
ws["A2"] = 0.25
ws["A2"].number_format = "0%"
ws["A3"] = "2026-03-07"
ws["A4"] = dt.date(2026, 3, 7)
ws["A4"].number_format = "dd/mm/yyyy"
ws["B3"] = "=ISNUMBER(A3)"
ws["B4"] = "=ISNUMBER(A4)"
ws["C4"] = "=A4"
ws["C4"].number_format = "0"
wb.save("data/mistakes2.xlsx")
r2 = shown("data/mistakes2.xlsx")["p"]
print("pct 25 with 0% shows:", r2[0][0])
print("pct 0.25 with 0% shows:", r2[1][0])
print("text date A3 shows:", r2[2][0])
print("ISNUMBER text date:", r2[2][1])
print("ISNUMBER real date:", r2[3][1])
print("real date with 0 format:", r2[3][2])
