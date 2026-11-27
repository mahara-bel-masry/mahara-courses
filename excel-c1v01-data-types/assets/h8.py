# find a repeated order id with COUNTIF, no sorting needed (lab2 file, invented data, LibreOffice 26.8.3)
import openpyxl, subprocess
wb=openpyxl.load_workbook("lab/lab2.xlsx"); ws=wb["raw"]
ws["F1"]="times_id_appears"
for r in range(2,14): ws[f"F{r}"]=f"=COUNTIF($A$2:$A$13,A{r})"
wb.save("data/h8.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out8","data/h8.xlsx"],capture_output=True,timeout=90)
r=openpyxl.load_workbook("data/out8/h8.xlsx",data_only=True)["raw"]
print("ids that appear more than once:",sorted({(r[f'A{i}'].value) for i in range(2,14) if r[f'F{i}'].value>1}), "rows:",[i for i in range(2,14) if r[f'F{i}'].value>1])
