# Tables, structured references and named ranges: real run on LibreOffice 26.8.3 (invented data)
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.workbook.defined_name import DefinedName
wb=openpyxl.Workbook(); ws=wb.active; ws.title="sales"
ws.append(["order_id","city","qty","price","amount"])
data=[("A1","Cairo",5,100),("A2","Giza",7,50),("A3","Cairo",3,200),("A4","Fayoum",9,10)]
for i,(o,c,q,p) in enumerate(data,2):
    ws.append([o,c,q,p,f"=tblSales[[#This Row],[qty]]*tblSales[[#This Row],[price]]"])
t=Table(displayName="tblSales",ref="A1:E5"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2",showRowStripes=True); ws.add_table(t)
ws2=wb.create_sheet("report")
ws2["A1"]="rows";            ws2["B1"]="=ROWS(tblSales[qty])"
ws2["A2"]="qty total";       ws2["B2"]="=SUM(tblSales[qty])"
ws2["A3"]="revenue (column)";ws2["B3"]="=SUM(tblSales[amount])"
ws2["A4"]="Cairo qty";       ws2["B4"]='=SUMIFS(tblSales[qty],tblSales[city],"Cairo")'
ws2["A5"]="header text";     ws2["B5"]="=INDEX(tblSales[[#Headers],[city]],1)"
ws2["A6"]="named range";     ws2["B6"]="=SUM(Qty)"
ws2["A7"]="named constant";  ws2["B7"]="=B3*(1+VAT)"
ws2["A8"]="name from sheet scope"; ws2["B8"]="=SUM(sales!Prices)"
wb.defined_names["Qty"]=DefinedName("Qty",attr_text="sales!$C$2:$C$5")
wb.defined_names["VAT"]=DefinedName("VAT",attr_text="0.14")
ws.defined_names["Prices"]=DefinedName("Prices",attr_text="sales!$D$2:$D$5")
wb.save("data/t1.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out","data/t1.xlsx"],capture_output=True,timeout=90)
r=openpyxl.load_workbook("data/out/t1.xlsx",data_only=True)
for row in r["report"].iter_rows(min_row=1,max_row=8,values_only=True): print(row[0],"->",row[1])
print("amount column:",[c.value for c in r["sales"]["E"][1:]])
