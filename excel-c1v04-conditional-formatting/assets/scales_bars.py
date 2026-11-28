# colour scale drawn by LibreOffice; data bar and
# icon set read back from the saved file
import openpyxl, sys, zipfile, re
from openpyxl.formatting.rule import (
    ColorScaleRule,
    DataBarRule,
    IconSetRule,
)

sys.path.insert(0, "assets")
from common import view

v = [5, 12, 30, 8, 45, 20, 12, 100]
wb = openpyxl.Workbook()
ws = wb.active
for i, x in enumerate(v, 1):
    for c in range(1, 5):
        ws.cell(i, c, x)
ws.conditional_formatting.add(
    "A1:A8",
    ColorScaleRule(
        start_type="min",
        start_color="F8696B",
        end_type="max",
        end_color="63BE7B",
    ),
)
ws.conditional_formatting.add(
    "B1:B8",
    ColorScaleRule(
        start_type="min",
        start_color="F8696B",
        mid_type="percentile",
        mid_value=50,
        mid_color="FFEB84",
        end_type="max",
        end_color="63BE7B",
    ),
)
ws.conditional_formatting.add(
    "C1:C8",
    DataBarRule(
        start_type="min",
        end_type="max",
        color="638EC6",
    ),
)
ws.conditional_formatting.add(
    "D1:D8",
    IconSetRule(
        "3TrafficLights1", "percent", [0, 33, 67]
    ),
)
wb.save("data/scales.xlsx")
g = view("data/scales.xlsx")[0]
print("values:", v)
print("2-colour scale:")
for x, r in zip(v, g):
    print(" ", x, r[0]["bg"])
print("min cell has start colour:", g[0][0]["bg"] == "F8696B")
print("max cell has end colour:", g[7][0]["bg"] == "63BE7B")
print("3-colour scale (min, middle, max):")
for x, r in zip(v, g):
    if x in (5, 20, 100):
        print(" ", x, r[1]["bg"])
z = zipfile.ZipFile("data/scales.xlsx")
s = z.read("xl/worksheets/sheet1.xml").decode()
print("rules saved in file:")
print(" ", sorted(set(re.findall(r'type="(\w+)"', s))))
print(" ", re.findall(r'iconSet="?(\w+)"?', s))
print("html shows data bars:", bool(g[0][2]["bg"]))
