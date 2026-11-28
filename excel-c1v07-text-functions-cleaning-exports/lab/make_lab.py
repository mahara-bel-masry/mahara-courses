# lab file: a made-up orders export with six problems to find and fix
import openpyxl

NB = "\u00a0"
rows = [
    ("A-101 ", "Mona Hassan", "1,250", "010-1111-2222", "gift"),
    ("A-102", "Omar\nAli", "980", "011-3333-4444", ""),
    (NB + "A-103", "Sara Nabil", "2,400", "012-5555-6666", "late"),
    ("A-104", "Hany  Samir", "75", "015-7777-8888\t", ""),
    ("A-105", "Laila Adel", "3,100", "010-9999-0000", "gift"),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["code", "customer", "amount", "phone", "note"])
for r in rows:
    ws.append(list(r))
ws["G1"] = "total amount"
ws["H1"] = "=SUM(C2:C6)"
ws["G2"] = "row of A-103"
ws["H2"] = '=MATCH("A-103",A2:A6,0)'
ws["G3"] = "row of A-101"
ws["H3"] = '=MATCH("A-101",A2:A6,0)'
wb.save("lab/lab_export.xlsx")
print("lab_export.xlsx written")
