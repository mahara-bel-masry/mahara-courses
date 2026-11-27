# the documented item specifiers from the Microsoft Support page, run on LibreOffice 26.8.3 (invented DeptSales-like table)
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
wb=openpyxl.Workbook(); ws=wb.active; ws.title="d"
ws.append(["Sales Person","Region","Sales Amount","% Commission","Commission Amount"])
data=[("Ali","North",260,0.1),("Mona","South",660,0.1),("Omar","East",940,0.15),("Sara","West",410,0.12),("Hany","North",730,0.13),("Dina","South",180,0.1),("Tarek","East",500,0.12)]
for i,(a,b,c,d) in enumerate(data,2): ws.append([a,b,c,d,f"=DeptSales[[#This Row],[Sales Amount]]*DeptSales[[#This Row],[% Commission]]"])
ws.append(["Total",None,"=SUBTOTAL(109,DeptSales[Sales Amount])",None,"=SUBTOTAL(109,DeptSales[Commission Amount])"])
t=Table(displayName="DeptSales",ref="A1:E9",totalsRowCount=1); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); ws.add_table(t)
r=wb.create_sheet("r")
tests=[("ROWS [#All],[Sales Amount]   (page: C1:C8 = 8 cells)","=ROWS(DeptSales[[#All],[Sales Amount]])"),
("ROWS [#Data],[Sales Amount]  (7 data rows)","=ROWS(DeptSales[[#Data],[Sales Amount]])"),
("[#Headers],[% Commission]    (page: D1)","=DeptSales[[#Headers],[% Commission]]"),
("COLUMNS [#All],[Sales Amount]:[% Commission] (page: C1:D8 = 2 columns)","=COLUMNS(DeptSales[[#All],[Sales Amount]:[% Commission]])"),
("ROWS [#Data],[% Commission]:[Commission Amount] (page: D2:E7 in its example)","=ROWS(DeptSales[[#Data],[% Commission]:[Commission Amount]])"),
("COLUMNS [#Headers],[Region]:[Commission Amount] (page: B1:E1 = 4)","=COLUMNS(DeptSales[[#Headers],[Region]:[Commission Amount]])"),
("[#Totals],[Sales Amount]","=DeptSales[[#Totals],[Sales Amount]]"),
("SUM data Sales Amount","=SUM(DeptSales[Sales Amount])"),
("SUM data Commission Amount","=SUM(DeptSales[Commission Amount])"),
("[#Headers],[#Data],[% Commission] rows (page: D1:D7 style)","=ROWS(DeptSales[[#Headers],[#Data],[% Commission]])")]
for i,(a,f) in enumerate(tests,1): r.cell(i,1,a); r.cell(i,2,f)
wb.save("data/t4.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out4","data/t4.xlsx"],capture_output=True,timeout=90)
x=openpyxl.load_workbook("data/out4/t4.xlsx",data_only=True)["r"]
for i in range(1,len(tests)+1): print(f"{x.cell(i,1).value:75} -> {x.cell(i,2).value}")
