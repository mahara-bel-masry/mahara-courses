# applies one format per column, saves
# sol_formats.xlsx, prints the strings LibreOffice
# displays (invented data)
import openpyxl, sys

sys.path.insert(0, "assets")
from common import shown

wb = openpyxl.load_workbook("lab/lab_formats.xlsx")
ws = wb.active
fm = {
    "A": '"ORD"00000',
    "B": '#,##0.00;[Red]-#,##0.00;"-"',
    "C": "0.0%",
    "D": "dd/mm/yyyy",
    "E": "[h]:mm",
    "F": "0000000000",
}
for col, f in fm.items():
    for c in ws[col][1:]:
        c.number_format = f
ws["H1"] = "=SUM(B2:B6)"
ws["H1"].number_format = "#,##0.00"
wb.save("lab/sol_formats.xlsx")
rows = shown("lab/sol_formats.xlsx")["orders"]
for r in rows:
    print(" | ".join(r))
v = openpyxl.load_workbook(
    "lab/sol_formats.xlsx"
).active
print(
    "stored values unchanged:",
    [c.value for c in v[3]][:3],
)
