# lab file: a made-up orders sheet with six problems to find and fix.
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Orders"
ws.append(["order", "units", "price", "total", "share"])
data = [("o1", 6, 50), ("o2", 4, 75), ("o3", 10, 20), ("o4", 3, 120),
        ("o5", 8, 35), ("o6", 5, 60)]
for i, (o, u, p) in enumerate(data, 2):
    ws.cell(i, 1, o); ws.cell(i, 2, u); ws.cell(i, 3, p)
    ws.cell(i, 4, f"=B{i}*C{i}")
    ws.cell(i, 5, f"=D{i}/$D$10")
ws["D4"] = 200                 # 1 typed over a formula
ws["B5"] = "3"                 # 2 number stored as text
ws["C6"] = None                # 3 empty price
ws["E3"] = "=D3/D10"           # 4 missing dollar
ws["A8"] = "o7"; ws["B8"] = 2; ws["C8"] = 90
ws["D8"] = "=B8*C8"            # 5 below the SUM range
ws["E8"] = "=D8/$D$10"
ws["A10"] = "total"; ws["D10"] = "=SUM(D2:D7)"
ws["G1"] = "code"; ws["H1"] = "region"
ws["G2"] = "o3"; ws["H2"] = '=INDEX({"North","South"},MATCH(G2,{"o1","o2"},0))'   # 6 no match
wb.save("lab/lab_audit.xlsx")
print("lab_audit.xlsx written")
