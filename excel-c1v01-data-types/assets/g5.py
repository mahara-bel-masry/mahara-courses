# Table = named range that grows; written structured reference (not run in Excel here)
# In Excel: select data, Ctrl+T, name it tblSales, then write
#   =SUM(tblSales[qty])
# Same total in pandas as the proof:
import pandas as pd
df = pd.read_excel("data/raw.xlsx", dtype=object)
df["qty"] = pd.to_numeric(df["qty"])
print("SUM(tblSales[qty]) should be:", int(df["qty"].sum()))
print("rows if a new row is added to the Table:", len(df) + 1)
