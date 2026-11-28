# parentheses for negatives, underscore spacing,
# backslash literal, text prefix, zero-hiding, units
# (invented values, LibreOffice 26.8.3.1)
import openpyxl, sys

sys.path.insert(0, "assets")
from common import shown

cases = [
    (1234.5, "#,##0.00_);(#,##0.00)"),
    (-1234.5, "#,##0.00_);(#,##0.00)"),
    (25, '0" kg"'),
    (25, "0\\ \\k\\g"),
    ("Cairo", '"city: "@'),
    (0, "0;-0;;@"),
    (5, "0;-0;;@"),
    (0, "#,##0;-#,##0;"),
    (7, ";;;"),
    (1234.5, "0.0,"),
    (1500, '0.0,"K"'),
    (1500000, '0.0,,"M"'),
    (0.5, "# ?/?"),
    (0.5, "0%"),
    (1234.5, "@"),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "e"
for i, (v, f) in enumerate(cases, 1):
    ws.cell(i, 1, v).number_format = f
wb.save("data/extras.xlsx")
for (v, f), r in zip(
    cases, shown("data/extras.xlsx")["e"]
):
    print(
        f"value={v!r} format={f} "
        f"shown={(r[0] if r else '')!r}"
    )
