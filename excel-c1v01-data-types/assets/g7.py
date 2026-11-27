# the trap: plain read_excel hides the text numbers, openpyxl shows them
import pandas as pd, openpyxl
plain = pd.read_excel("data/raw.xlsx")
print("pandas plain qty dtype:", plain["qty"].dtype, "(looks clean, it is not)")
ws = openpyxl.load_workbook("data/raw.xlsx")["raw"]
txt = [ws.cell(r,1).value for r in range(2, ws.max_row+1) if isinstance(ws.cell(r,4).value, str)]
print("openpyxl sees text qty in:", txt)
