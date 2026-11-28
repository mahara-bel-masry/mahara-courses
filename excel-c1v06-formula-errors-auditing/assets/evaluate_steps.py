# the Microsoft Evaluate Formula example, done by hand in cells:
# =IF(AVERAGE(D2:D5)>50,SUM(E2:E5),0). The step cells are mine;
# this is NOT the Evaluate Formula dialog.
import sys, openpyxl
sys.path.insert(0, "assets")
from common import calc
wb = openpyxl.Workbook()
ws = wb.active
for r, (d, e) in enumerate([(55, 10), (35, 20), (45, 30), (25, 40)], 2):
    ws.cell(r, 4, d); ws.cell(r, 5, e)
ws["G1"] = "=IF(AVERAGE(D2:D5)>50,SUM(E2:E5),0)"
ws["G2"] = "=AVERAGE(D2:D5)"
ws["G3"] = "=G2>50"
ws["G4"] = "=SUM(E2:E5)"
ws["G5"] = "=IF(G3,G4,0)"
wb.save("data/evaluate.xlsx")
w = calc("data/evaluate.xlsx").active
print("whole formula G1 ->", w["G1"].value)
print("step 1 AVERAGE(D2:D5) ->", w["G2"].value)
print("step 2 average > 50 ->", w["G3"].value)
print("SUM(E2:E5), not needed when step 2 is False ->", w["G4"].value)
print("step 3 IF(step2, sum, 0) ->", w["G5"].value)
