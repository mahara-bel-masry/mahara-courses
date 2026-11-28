# lab file: a price list and discount percentages across the top.
# the student writes ONE formula in C5 and fills it right and down.
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Lab"
ws["A1"] = "Quote grid (all data is made up)"
ws["A3"] = "discount"
for j, d in enumerate([0, 0.05, 0.10, 0.15]):
    ws.cell(3, 3 + j, d)
ws["A4"] = "item"; ws["B4"] = "price"
for j in range(4):
    ws.cell(4, 3 + j, f"tier {j + 1}")
for i, (n, p) in enumerate([("chair", 800), ("desk", 2400),
                            ("shelf", 650), ("lamp", 300)], 5):
    ws.cell(i, 1, n); ws.cell(i, 2, p)
ws["A11"] = "tax rate"; ws["B11"] = 0.1
wb.save("lab/lab_refs.xlsx")
print("lab_refs.xlsx written")
