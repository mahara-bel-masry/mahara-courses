# add formulas, let LibreOffice calculate them (real run, LibreOffice 26.8.3)
import subprocess, openpyxl
wb = openpyxl.load_workbook("data/raw.xlsx")
ws = wb["raw"]
ws["H1"] = "total_qty_SUM";   ws["H2"] = "=SUM(D2:D21)"
ws["I1"] = "count_numbers";   ws["I2"] = "=COUNT(D2:D21)"
ws["J1"] = "count_all";       ws["J2"] = "=COUNTA(D2:D21)"
wb.save("data/calc.xlsx")
subprocess.run(["soffice","--headless","--convert-to","xlsx:Calc MS Excel 2007 XML",
  "--outdir","data/out","data/calc.xlsx"],
  capture_output=True, timeout=90)
r = openpyxl.load_workbook("data/out/calc.xlsx", data_only=True)["raw"]
print("SUM  :", r["H2"].value)
print("COUNT:", r["I2"].value, "numbers")
print("COUNTA:", r["J2"].value, "cells")
print("text cells hidden from SUM:", r["J2"].value - r["I2"].value)
