# diagnose types with formulas, real run on LibreOffice 26.8.3 (all data invented)
import openpyxl, subprocess
wb=openpyxl.load_workbook("data/raw.xlsx"); ws=wb["raw"]
ws["H1"]="type_of_qty"
for r in range(2,22): ws[f"H{r}"]=f'=IF(ISTEXT(D{r}),"TEXT",IF(ISNUMBER(D{r}),"number","other"))'
ws["J1"]="texts_in_qty";   ws["J2"]="=SUMPRODUCT(--ISTEXT(D2:D21))"
ws["K1"]="texts_in_price"; ws["K2"]="=SUMPRODUCT(--ISTEXT(E2:E21))"
ws["L1"]="dates_that_are_numbers"; ws["L2"]="=SUMPRODUCT(--ISNUMBER(B2:B21))"
ws["M1"]="phones_that_are_text";   ws["M2"]="=SUMPRODUCT(--ISTEXT(F2:F21))"
ws["N1"]="sum_after_VALUE"; ws["N2"]="=SUMPRODUCT(VALUE(D2:D21))"
ws["O1"]="revenue_after_VALUE"; ws["O2"]="=SUMPRODUCT(VALUE(D2:D21),VALUE(E2:E21))"
wb.save("data/h3.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML","--outdir","data/out3","data/h3.xlsx"],capture_output=True,timeout=90)
r=openpyxl.load_workbook("data/out3/h3.xlsx",data_only=True)["raw"]
print("rows flagged TEXT:", [r[f"A{i}"].value for i in range(2,22) if r[f"H{i}"].value=="TEXT"])
for c in "JKLMNO": print(r[f"{c}1"].value,"=",r[f"{c}2"].value)
