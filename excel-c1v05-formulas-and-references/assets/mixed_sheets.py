# mixed references (a times table), other sheets, quoted
# sheet names, 3-D range, whole row and whole column
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Table"
for j in range(1, 5):
    ws.cell(1, j + 1, j * 10)      # B1..E1 prices 10..40
for i in range(1, 4):
    ws.cell(i + 1, 1, i)           # A2..A4 qty 1..3
for i in range(2, 5):
    for j in range(2, 6):
        L = openpyxl.utils.get_column_letter(j)
        ws.cell(i, j, f"=$A{i}*{L}$1")
print("B2 formula", ws["B2"].value, "| E4 formula", ws["E4"].value)

for n, v in [("North", 100), ("South", 250), ("East", 75)]:
    s = wb.create_sheet(n)
    s["B5"] = v
t = wb.create_sheet("January Revenue")
t["A1"] = 500
t2 = wb.create_sheet("123")
t2["A1"] = 7
ws["G1"] = "=SUM(North:East!B5)"
ws["G2"] = "='January Revenue'!A1*2"
ws["G3"] = "='123'!A1+1"
ws["G4"] = "=North!B5+South!B5"
ws["G5"] = "=SUM(A2:A4)"
ws["G6"] = "=SUM(2:2)"
ws["G7"] = "=SUM(A:A)"
ws["G8"] = "=SUM(2:3)"
wb.save("data/mixed.xlsx")
w = calc("data/mixed.xlsx")["Table"]
print("times table values:")
for i in range(2, 5):
    print([w.cell(i, j).value for j in range(2, 6)])
for r, label in [(1, "SUM(North:East!B5)"),
                 (2, "'January Revenue'!A1*2"),
                 (3, "'123'!A1+1"), (4, "North+South"),
                 (5, "SUM(A2:A4)"), (6, "SUM(2:2) whole row 2"),
                 (7, "SUM(A:A) whole column A"),
                 (8, "SUM(2:3) rows 2 to 3")]:
    print(label, "=", w[f"G{r}"].value)
