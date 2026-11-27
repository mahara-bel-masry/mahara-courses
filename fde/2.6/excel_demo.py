from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.append(["id", "total"])
ws.append(["A1", 448.5])
ws.append(["A2", 1250.5])
wb.save("orders.xlsx")
ws = load_workbook("orders.xlsx").active
for row in ws.iter_rows(min_row=2, values_only=True):
    print(row)
