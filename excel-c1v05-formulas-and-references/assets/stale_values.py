# a typed constant, a pasted value and a formula:
# change the input and see which one follows
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc

def build(price, path):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws["A1"] = "price"; ws["B1"] = price
    ws["A2"] = "qty"; ws["B2"] = 5
    ws["A3"] = "typed constant"; ws["B3"] = "=50*5"
    ws["A4"] = "pasted value"; ws["B4"] = 250
    ws["A5"] = "formula"; ws["B5"] = "=B1*B2"
    wb.save(path)
    w = calc(path).active
    print(f"price={price}:",
          {w[f"A{r}"].value: w[f"B{r}"].value for r in (3, 4, 5)})

build(50, "data/stale1.xlsx")
build(60, "data/stale2.xlsx")
