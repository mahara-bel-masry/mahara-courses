# SUBTOTAL(109) vs SUM when a row is hidden by hand (LibreOffice 26.8.3, invented numbers)
import openpyxl, subprocess
wb=openpyxl.Workbook(); ws=wb.active
for i,v in enumerate([10,20,30,40],1): ws.cell(i,1,v)
ws.row_dimensions[2].hidden=True
ws["C1"]="=SUM(A1:A4)"; ws["C2"]="=SUBTOTAL(9,A1:A4)"; ws["C3"]="=SUBTOTAL(109,A1:A4)"
wb.save("data/t5.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out5","data/t5.xlsx"],capture_output=True,timeout=90)
x=openpyxl.load_workbook("data/out5/t5.xlsx",data_only=True).active
print("row 2 (value 20) hidden by hand")
print("SUM          :",x["C1"].value); print("SUBTOTAL 9   :",x["C2"].value); print("SUBTOTAL 109 :",x["C3"].value)
