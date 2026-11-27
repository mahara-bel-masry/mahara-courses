# Table with 4 rows, structured references,
# real run on LibreOffice (invented data)
import openpyxl, subprocess
from openpyxl.worksheet.table import Table
from openpyxl.worksheet.table import TableStyleInfo
wb = openpyxl.Workbook(); ws = wb.active
ws.title = "sales"
ws.append(["order_id", "city", "qty"])
rows = [("A1","Cairo",5), ("A2","Giza",7),
        ("A3","Cairo",3), ("A4","Fayoum",9)]
for r in rows:
    ws.append(list(r))
t = Table(displayName="tblSales", ref="A1:C5")
t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2")
ws.add_table(t)
ws["E1"] = "=SUM(tblSales[qty])"
ws["E2"] = ('=SUMIFS(tblSales[qty],'
            'tblSales[city],"Cairo")')
wb.save("data/i1.xlsx")
subprocess.run(["soffice", "--headless", "--convert-to",
    "xlsx:Calc MS Excel 2007 XML",
    "--outdir", "data/out_i1", "data/i1.xlsx"],
    capture_output=True, timeout=90)
x = openpyxl.load_workbook("data/out_i1/i1.xlsx",
    data_only=True)["sales"]
print("rows in tblSales:", ws.max_row - 1)
print("SUM(tblSales[qty]) =", x["E1"].value)
print("SUMIFS Cairo =", x["E2"].value)
