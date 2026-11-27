# wrong column name or wrong table name in a structured reference (LibreOffice 26.8.3, invented data)
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
wb=openpyxl.Workbook(); ws=wb.active; ws.title="sales"
ws.append(["city","qty"])
for r in [("Cairo",5),("Giza",7)]: ws.append(list(r))
t=Table(displayName="tblSales",ref="A1:B3"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); ws.add_table(t)
ws["D1"]="=SUM(tblSales[qty])"; ws["D2"]="=SUM(tblSales[qtyy])"; ws["D3"]="=SUM(tblSale[qty])"
wb.save("data/t7.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out7","data/t7.xlsx"],capture_output=True,timeout=90)
x=openpyxl.load_workbook("data/out7/t7.xlsx",data_only=True).active
print("correct:",x["D1"].value,"| wrong column name:",x["D2"].value,"| wrong table name:",x["D3"].value)
