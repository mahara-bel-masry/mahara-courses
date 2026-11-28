# re-run of the examples in Microsoft's "Review
# guidelines for customizing a number format" table;
# compare Microsoft's stated result with what
# LibreOffice displayed (invented cells, LibreOffice
# 26.8.3.1)
import openpyxl, sys

sys.path.insert(0, "assets")
from common import shown

cases = [
    (1234.59, "####.#", "1234.6"),
    (8.9, "#.000", "8.900"),
    (0.631, "0.#", "0.6"),
    (12, "#.0#", "12.0"),
    (1234.568, "#.0#", "1234.57"),
    (44.398, "???.???", "44.398"),
    (2.8, "???.???", "2.8 (aligned)"),
    (5.25, "# ???/???", "5 1/4"),
    (5.3, "# ???/???", "5 3/10"),
    (12000, "#,###", "12,000"),
    (12000, "#,", "12"),
    (12200000, '0.0,,"M"', "12.2M"),
    (12200000, "0.00E+00", "1.22E+07"),
    (12200000, "#0.0E+0", "12.2E+6"),
    (12345678901, "0.00E+00", "1.23E+10"),
    (32, '#\\"', '32"'),
    (
        125.74,
        '$0.00" Surplus";$-0.00" Shortage"',
        "$125.74 Surplus",
    ),
    (
        -125.74,
        '$0.00" Surplus";$-0.00" Shortage"',
        "$-125.74 Shortage",
    ),
    (8.9, "0.0?", "8.9"),
    (88.99, "0.0?", "88.99"),
    (0.08, "0%", "8%"),
]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "m"
for i, (v, f, e) in enumerate(cases, 1):
    ws.cell(i, 1, v).number_format = f
wb.save("data/t6.xlsx")
rows = shown("data/t6.xlsx")["m"]
same = 0
for (v, f, e), r in zip(cases, rows):
    norm = lambda s: " ".join(
        s.replace("\u2007", " ").split()
    )
    ok = norm(r[0]) == norm(e.split(" (")[0])
    same += ok
    print(
        f"value={v} format={f} "
        f"ms={e} "
        f"shown={r[0]!r} "
        f"{'same' if ok else 'DIFFERENT'}"
    )
print(
    "same (alignment spaces ignored):",
    same,
    "of",
    len(cases),
)
