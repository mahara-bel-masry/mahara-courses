# unit text inside a number cell: real run on LibreOffice 26.8.3 (invented values)
import openpyxl, subprocess
wb=openpyxl.Workbook(); ws=wb.active
vals=["120 EGP","250 EGP","80 EGP"]
for i,v in enumerate(vals,1): ws.cell(i,1,v)
for i in range(1,4):
    ws.cell(i,2,f"=VALUE(A{i})"); ws.cell(i,3,f'=VALUE(SUBSTITUTE(A{i}," EGP",""))')
ws["E1"]="=SUM(A1:A3)"; ws["E2"]="=SUM(C1:C3)"; ws["E3"]="=COUNT(A1:A3)"
wb.save("data/h6.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out6","data/h6.xlsx"],capture_output=True,timeout=90)
r=openpyxl.load_workbook("data/out6/h6.xlsx",data_only=True).active
print("SUM of the text cells    :",r["E1"].value,"  COUNT:",r["E3"].value)
print("VALUE on '120 EGP'       :",r["B1"].value)
print("after SUBSTITUTE + VALUE :",[r[f"C{i}"].value for i in (1,2,3)]," sum:",r["E2"].value)
