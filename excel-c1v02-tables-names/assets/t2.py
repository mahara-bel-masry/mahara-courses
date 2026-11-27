# a layout that breaks analysis: merged cell, blank row, two header rows (pandas sees what a Table would see)
import openpyxl, pandas as pd
wb=openpyxl.Workbook(); ws=wb.active
ws["A1"]="Sales report November (invented)"; ws.merge_cells("A1:D1")
ws.append(["city","qty","price","note"])
ws.append(["Cairo",5,100,None]); ws.append([None,None,None,None]); ws.append(["Giza",7,50,"call back"])
wb.save("data/bad_layout.xlsx")
bad=pd.read_excel("data/bad_layout.xlsx")
print("columns pandas sees:",list(bad.columns)); print(bad.to_string())
good=pd.read_excel("data/bad_layout.xlsx",header=1).dropna(how="all")
print("after skipping title row and blank row:"); print(good.to_string())
