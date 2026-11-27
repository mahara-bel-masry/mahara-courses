# one hand-typed value inside a calculated column, caught by a second method (LibreOffice 26.8.3, invented data)
import openpyxl, subprocess
from openpyxl.worksheet.table import Table, TableStyleInfo
wb=openpyxl.Workbook(); ws=wb.active; ws.title="o"
ws.append(["qty","price","amount"])
for i,(q,p) in enumerate([(2,50),(3,40),(1,120),(4,25)],start=2):
    ws.append([q,p,f"=A{i}*B{i}"])
ws["C3"]=500   # someone typed over the formula in one row
t=Table(displayName="tblO",ref="A1:C5"); t.tableStyleInfo=TableStyleInfo(name="TableStyleMedium2"); ws.add_table(t)
ws["E1"]="=SUM(tblO[amount])"; ws["E2"]="=SUMPRODUCT(tblO[qty],tblO[price])"; ws["E3"]="=E1-E2"
wb.save("data/t10.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out10","data/t10.xlsx"],capture_output=True,timeout=90)
x=openpyxl.load_workbook("data/out10/t10.xlsx",data_only=True)["o"]
print("SUM(amount) =",x["E1"].value,"| SUMPRODUCT(qty,price) =",x["E2"].value,"| difference =",x["E3"].value)
