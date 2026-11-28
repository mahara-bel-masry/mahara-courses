# regional settings tests that LibreOffice can run:
# decimal/list separators in CSV, Arabic-Indic digits
# in a format, RTL sheet flag
import openpyxl, subprocess, os, csv, sys

sys.path.insert(0, "assets")
from common import shown

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "r"
ws["A1"] = 1234.5
ws["A1"].number_format = "#,##0.00"
ws["B1"] = "text, with comma"
ws["C1"] = 3.25
ws["A2"] = 1234567
ws["A2"].number_format = (
    "[$-2000401]0"  # Arabic-Indic digits locale tag
)
ws["A3"] = 1234567
ws["A3"].number_format = "0"
ws.sheet_view.rightToLeft = True
wb.save("data/t4.xlsx")
print(
    "rightToLeft flag written by openpyxl, read back:",
    openpyxl.load_workbook(
        "data/t4.xlsx"
    ).active.sheet_view.rightToLeft,
)
rows = shown("data/t4.xlsx")["r"]
print("displayed A1..C1:", rows[0])
print("A2 with [$-2000401]0 shown as:", rows[1][0])
print("A3 plain 0 shown as:", rows[2][0])
# csv with semicolon separator vs comma on read-back
open("data/semi.csv", "w", encoding="utf8").write(
    "a;b\n1,5;2,5\n"
)
open("data/comma.csv", "w", encoding="utf8").write(
    "a,b\n1.5,2.5\n"
)
print(
    "semicolon file read with comma delimiter:",
    list(
        csv.reader(open("data/semi.csv"), delimiter=",")
    ),
)
print(
    "semicolon file read with semicolon delimiter:",
    list(
        csv.reader(open("data/semi.csv"), delimiter=";")
    ),
)
print(
    "comma file read with comma delimiter:",
    list(
        csv.reader(
            open("data/comma.csv"), delimiter=","
        )
    ),
)
