# discount per order = amount * discount_rate; total
# shown by format vs total after ROUND per row
# (invented data, LibreOffice 26.8.3.1)
import openpyxl, subprocess, os

src = openpyxl.load_workbook(
    "lab/lab_formats.xlsx"
).active
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "d"
ws.append(
    ["amount", "rate", "discount", "discount_rounded"]
)
for r in range(2, 7):
    n = r
    ws.append(
        [
            src.cell(r, 2).value,
            src.cell(r, 3).value,
            f"=A{n}*B{n}",
            f"=ROUND(A{n}*B{n},2)",
        ]
    )
ws["C7"] = "=SUM(C2:C6)"
ws["D7"] = "=SUM(D2:D6)"
ws["E7"] = "=C7-D7"
for row in ws["C2:D7"]:
    for c in row:
        c.number_format = "#,##0.00"
wb.save("data/t7.xlsx")
os.makedirs("data/out7", exist_ok=True)
subprocess.run(
    [
        "soffice",
        "--headless",
        "--convert-to",
        "xlsx:Calc MS Excel 2007 XML",
        "--outdir",
        "data/out7",
        "data/t7.xlsx",
    ],
    capture_output=True,
    timeout=120,
)
x = openpyxl.load_workbook(
    "data/out7/t7.xlsx", data_only=True
).active
for r in range(2, 7):
    print(
        "row",
        r - 1,
        "discount:",
        x.cell(r, 3).value,
        "| rounded:",
        x.cell(r, 4).value,
    )
print(
    "sum of discounts:",
    x["C7"].value,
    "| sum of rounded:",
    x["D7"].value,
    "| difference:",
    x["E7"].value,
)
print(
    "sum of discounts shown with"
    "#,##0.00 would read:",
    f"{x['C7'].value:,.2f}",
    "| sum of rounded:",
    f"{x['D7'].value:,.2f}",
)
print(
    "sum cells equal as stored values:",
    x["C7"].value == x["D7"].value,
)
