# leading space before a number: VALUE and TRIM on LibreOffice 26.8.3 (invented value)
import openpyxl, subprocess
wb=openpyxl.Workbook(); ws=wb.active
ws["A1"]=" 7"; ws["B1"]="=VALUE(A1)"; ws["C1"]="=VALUE(TRIM(A1))"; ws["D1"]="=LEN(A1)"; ws["E1"]="=ISTEXT(A1)"
wb.save("data/h7.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out7","data/h7.xlsx"],capture_output=True,timeout=90)
r=openpyxl.load_workbook("data/out7/h7.xlsx",data_only=True).active
print("text ' 7': ISTEXT",r["E1"].value,"LEN",r["D1"].value,"VALUE",r["B1"].value,"VALUE(TRIM)",r["C1"].value)
