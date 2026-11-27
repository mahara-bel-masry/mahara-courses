# fixed range vs structured reference when the data grows, and a name typo (LibreOffice 26.8.3, invented data)
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.workbook.defined_name import DefinedName
def build(path,last_row):
    wb=openpyxl.Workbook(); ws=wb.active; ws.title="sales"
    ws.append(["order_id","city","qty"])
    for r in [("A1","Cairo",5),("A2","Giza",7),("A3","Cairo",3),("A4","Fayoum",9),("A5","Giza",4),("A6","Cairo",6)][:last_row-1]: ws.append(list(r))
    t=Table(displayName="tblSales",ref=f"A1:C{last_row}"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); ws.add_table(t)
    ws["E1"]="=SUM(C2:C5)"          # typed with cell addresses when the data had 4 rows
    ws["E2"]="=SUM(tblSales[qty])"  # structured reference
    wb.defined_names["Qty"]=DefinedName("Qty",attr_text="sales!$C$2:$C$5")
    ws["E3"]="=SUM(Qty)"            # name fixed to the old 4 rows
    ws["E4"]="=SUM(Qtyy)"           # typo in the name
    wb.save(path)
for n,last in (("g4",5),("g6",7)):
    build(f"data/{n}.xlsx",last)
    subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out3",f"data/{n}.xlsx"],capture_output=True,timeout=90)
    r=openpyxl.load_workbook(f"data/out3/{n}.xlsx",data_only=True)["sales"]
    print(f"table has {last-1} rows | fixed range SUM(C2:C5) = {r['E1'].value} | SUM(tblSales[qty]) = {r['E2'].value} | SUM(Qty) with old name = {r['E3'].value} | SUM(Qtyy) typo = {r['E4'].value}")
