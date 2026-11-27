# wide layout (months as columns) vs long layout (one row per city and month); LibreOffice 26.8.3, invented numbers
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
wb=openpyxl.Workbook()
w=wb.active; w.title="wide"
w.append(["city","Sep","Oct","Nov","Dec"])
for r in [("Cairo",10,12,15,18),("Giza",7,8,9,11),("Fayoum",3,4,6,5)]: w.append(list(r))
for i in range(2,5): w.cell(i,7,f"=SUM(B{i}:D{i})")      # total written when there were 3 months
l=wb.create_sheet("long"); l.append(["city","month","qty"])
for c,vals in [("Cairo",(10,12,15,18)),("Giza",(7,8,9,11)),("Fayoum",(3,4,6,5))]:
    for m,v in zip(("Sep","Oct","Nov","Dec"),vals): l.append([c,m,v])
t=Table(displayName="tblLong",ref="A1:C13"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); l.add_table(t)
r=wb.create_sheet("r")
r["A1"]="wide: Cairo total (formula covers Sep-Nov only)"; r["B1"]="=wide!G2"
r["A2"]="long: Cairo total (all months present)";           r["B2"]='=SUMIFS(tblLong[qty],tblLong[city],"Cairo")'
r["A3"]="long: Dec total of all cities";                    r["B3"]='=SUMIFS(tblLong[qty],tblLong[month],"Dec")'
r["A4"]="wide: Dec total of all cities";                    r["B4"]="=SUM(wide!E2:E4)"
wb.save("data/t6.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out6","data/t6.xlsx"],capture_output=True,timeout=90)
x=openpyxl.load_workbook("data/out6/t6.xlsx",data_only=True)["r"]
for i in range(1,5): print(f"{x.cell(i,1).value:55} -> {x.cell(i,2).value}")
