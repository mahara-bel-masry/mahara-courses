# the format changes display, not value; leading zeros
# as text vs format; TEXT function; ROUND vs format
# (LibreOffice 26.8.3.1, invented)
import openpyxl, subprocess, os, sys

sys.path.insert(0, "assets")
from common import shown

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "v"
ws["A1"] = 2.456
ws["A1"].number_format = "0.0"
ws["A2"] = 2.456
ws["A2"].number_format = "0.0"
ws["A3"] = 2.456
ws["A3"].number_format = "0.0"
ws["B1"] = "=A1+A2+A3"
ws["B1"].number_format = "0.0"
ws["B2"] = "=ROUND(A1,1)+ROUND(A2,1)+ROUND(A3,1)"
ws["B2"].number_format = "0.0"
ws["C1"] = "=A1*1000"
ws["C1"].number_format = "General"
ws["D1"] = '=TEXT(1234.5,"#,##0.00")'
ws["D2"] = '=TEXT(0.256,"0.0%")'
ws["D3"] = '=TEXT(7,"000")'
ws["D4"] = "=ISNUMBER(D3)"
ws["E1"] = "00123"
ws["E2"] = 123
ws["E2"].number_format = "00000"
ws["E3"] = "=E2+1"
ws["E4"] = "=ISNUMBER(E1)"
wb.save("data/text_and_value.xlsx")
os.makedirs("data/out3", exist_ok=True)
subprocess.run(
    [
        "soffice",
        "--headless",
        "--convert-to",
        "xlsx:Calc MS Excel 2007 XML",
        "--outdir",
        "data/out3",
        "data/text_and_value.xlsx",
    ],
    capture_output=True,
    timeout=120,
)
x = openpyxl.load_workbook(
    "data/out3/text_and_value.xlsx", data_only=True
).active
print(
    "A1 stored value:",
    x["A1"].value,
    "| A1 displayed with format 0.0 as:",
    shown("data/text_and_value.xlsx")["v"][0][0],
)
print(
    "sum of three displayed 2.5 cells, unrounded:",
    x["B1"].value,
    "| sum of ROUND:",
    x["B2"].value,
)
print("A1*1000 =", x["C1"].value)
print(
    "TEXT results:",
    x["D1"].value,
    "|",
    x["D2"].value,
    "|",
    x["D3"].value,
    "| ISNUMBER(TEXT(...)):",
    x["D4"].value,
)
print(
    "typed text 00123 is kept as:",
    repr(x["E1"].value),
    "| ISNUMBER:",
    x["E4"].value,
)
print(
    "number 123 with format 00000, +1 gives:",
    x["E3"].value,
    "(value is still a number)",
)
