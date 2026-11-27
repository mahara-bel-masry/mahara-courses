# two more traps with real results (LibreOffice 26.8.3, invented numbers)
import openpyxl, subprocess
wb=openpyxl.Workbook(); ws=wb.active
for i,v in enumerate([4,6,None,8],1): ws.cell(i,1,v)          # blank cell
for i,v in enumerate([4,6,0,8],1): ws.cell(i,2,v)             # explicit zero
ws["D1"]="=AVERAGE(A1:A4)"; ws["D2"]="=AVERAGE(B1:B4)"; ws["D3"]="=COUNT(A1:A4)"; ws["D4"]="=COUNTBLANK(A1:A4)"
for i,(o,q) in enumerate([("A1","5"),("A2","7"),("A2","7"),("A3","3")],1): ws.cell(i,6,o); ws.cell(i,7,int(q))   # A2 appears twice
ws["I1"]="=SUM(G1:G4)"; ws["I2"]='=SUMPRODUCT((MATCH(F1:F4,F1:F4,0)=ROW(F1:F4))*G1:G4)'; ws["I3"]="=ROWS(F1:F4)-SUMPRODUCT(1/COUNTIF(F1:F4,F1:F4))"
wb.save("data/h4.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out4","data/h4.xlsx"],capture_output=True,timeout=90)
r=openpyxl.load_workbook("data/out4/h4.xlsx",data_only=True).active
print("AVERAGE with blank cell :",r["D1"].value)
print("AVERAGE with zero       :",r["D2"].value)
print("COUNT with blank        :",r["D3"].value,"COUNTBLANK:",r["D4"].value)
print("SUM with a repeated order:",r["I1"].value)
print("SUM counting each order once:",r["I2"].value)
print("duplicate rows found     :",r["I3"].value)
