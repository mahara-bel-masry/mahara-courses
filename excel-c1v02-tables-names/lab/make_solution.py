# solution file for the video 2 lab, checked on LibreOffice 26.8.3 (invented data)
import openpyxl, subprocess, datetime as dt
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.workbook.defined_name import DefinedName
rows=[("C101",dt.date(2026,11,1),"Cairo",4,120),("C102",dt.date(2026,11,2),"Giza",2,300),("C103",dt.date(2026,11,2),"Fayoum",10,45),
("C104",dt.date(2026,11,3),"Cairo",1,800),("C105",dt.date(2026,11,4),"Alexandria",6,95),("C106",dt.date(2026,11,5),"Giza",3,210),
("C107",dt.date(2026,11,6),"Cairo",5,60),("C108",dt.date(2026,11,7),"Fayoum",2,330)]
def build(path,extra):
    wb=openpyxl.Workbook(); ws=wb.active; ws.title="orders"
    ws.append(["order_id","order_date","city","qty","price","amount"])
    allrows=rows+extra
    for r in allrows: ws.append(list(r)+["=tblOrders[[#This Row],[qty]]*tblOrders[[#This Row],[price]]"])
    t=Table(displayName="tblOrders",ref=f"A1:F{len(allrows)+1}"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); ws.add_table(t)
    wb.defined_names["VAT"]=DefinedName("VAT",attr_text="0.14")
    r=wb.create_sheet("report")
    f=[("total qty","=SUM(tblOrders[qty])"),("revenue","=SUM(tblOrders[amount])"),
       ("Alexandria",'=SUMIFS(tblOrders[amount],tblOrders[city],"Alexandria")'),("Cairo",'=SUMIFS(tblOrders[amount],tblOrders[city],"Cairo")'),
       ("Fayoum",'=SUMIFS(tblOrders[amount],tblOrders[city],"Fayoum")'),("Giza",'=SUMIFS(tblOrders[amount],tblOrders[city],"Giza")'),
       ("revenue with VAT","=B2*(1+VAT)"),("check: second method","=SUMPRODUCT(tblOrders[qty],tblOrders[price])")]
    for i,(a,b) in enumerate(f,1): r.cell(i,1,a); r.cell(i,2,b)
    wb.save(path)
for name,extra in (("sol",[]),("sol_plus_row",[("C109",dt.date(2026,11,8),"Cairo",2,50)])):
    build(f"lab/{name}.xlsx",extra)
    subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","lab/out",f"lab/{name}.xlsx"],capture_output=True,timeout=90)
    s=openpyxl.load_workbook(f"lab/out/{name}.xlsx",data_only=True)["report"]
    print(name,{s.cell(i,1).value:s.cell(i,2).value for i in range(1,9)})
