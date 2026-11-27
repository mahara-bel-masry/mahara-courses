# four more mistakes, run in LibreOffice 26.8.3 (invented data): number stored as text, trailing space, hidden rows, name pointing at deleted cells
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.workbook.defined_name import DefinedName
def conv(src,out):
    subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir",out,src],capture_output=True,timeout=90)
def base(rows):
    wb=openpyxl.Workbook(); ws=wb.active; ws.title="sales"
    ws.append(["city","qty"])
    for r in rows: ws.append(list(r))
    t=Table(displayName="tblSales",ref=f"A1:B{len(rows)+1}"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); ws.add_table(t)
    return wb,ws
# 1 one quantity stored as text
wb,ws=base([("Cairo",5),("Giza",7),("Cairo","3"),("Giza",4)])
ws["D1"]="=SUM(tblSales[qty])"; ws["D2"]="=COUNT(tblSales[qty])"; ws["D3"]="=COUNTA(tblSales[qty])"
wb.save("data/t11a.xlsx"); conv("data/t11a.xlsx","data/out11")
x=openpyxl.load_workbook("data/out11/t11a.xlsx",data_only=True).active
print("text quantity | SUM:",x["D1"].value,"| COUNT:",x["D2"].value,"| COUNTA:",x["D3"].value)
# 2 trailing space in a city name
wb,ws=base([("Cairo",5),("Giza",7),("Cairo ",3),("Giza",4)])
ws["D1"]='=SUMIFS(tblSales[qty],tblSales[city],"Cairo")'; ws["D2"]="=SUM(tblSales[qty])"
ws["D3"]='=SUMPRODUCT((TRIM(tblSales[city])="Cairo")*tblSales[qty])'
wb.save("data/t11b.xlsx"); conv("data/t11b.xlsx","data/out11")
x=openpyxl.load_workbook("data/out11/t11b.xlsx",data_only=True).active
print("rows:",[(r[0].value,r[1].value) for r in x.iter_rows(min_row=2,max_row=5,max_col=2)])
print("trailing space | SUMIFS Cairo:",x["D1"].value,"| SUM all:",x["D2"].value,"| Cairo with TRIM:",x["D3"].value)
# 3 hidden rows
wb,ws=base([("Cairo",5),("Giza",7),("Cairo",3),("Giza",4)])
ws.row_dimensions[3].hidden=True; ws.row_dimensions[4].hidden=True
ws["D1"]="=SUM(tblSales[qty])"; ws["D2"]="=SUBTOTAL(109,tblSales[qty])"
wb.save("data/t11c.xlsx"); conv("data/t11c.xlsx","data/out11")
x=openpyxl.load_workbook("data/out11/t11c.xlsx",data_only=True).active
print("two rows hidden | SUM:",x["D1"].value,"| SUBTOTAL 109:",x["D2"].value)
# 4 a name that points at deleted cells
wb,ws=base([("Cairo",5),("Giza",7)])
wb.defined_names["Qty"]=DefinedName("Qty",attr_text="sales!#REF!")
ws["D1"]="=SUM(Qty)"; ws["D2"]="=SUM(tblSales[qty])"
wb.save("data/t11d.xlsx"); conv("data/t11d.xlsx","data/out11")
x=openpyxl.load_workbook("data/out11/t11d.xlsx",data_only=True).active
print("name on deleted cells | SUM(Qty):",x["D1"].value,"| SUM(tblSales[qty]):",x["D2"].value)
