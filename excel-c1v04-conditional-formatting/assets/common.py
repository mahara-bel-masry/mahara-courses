# helper: save a workbook, let LibreOffice export it
# to HTML, and read back the colours it really drew
import re, os, subprocess, tempfile


def view(path):
    out = tempfile.mkdtemp()
    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "html",
            "--outdir",
            out,
            path,
        ],
        capture_output=True,
        timeout=120,
    )
    name = os.path.splitext(os.path.basename(path))[0]
    h = open(f"{out}/{name}.html", encoding="utf8").read()
    sheets = []
    for t in re.findall(r"<table.*?</table>", h, re.S):
        grid = []
        for r in re.findall(r"<tr.*?</tr>", t, re.S):
            row = []
            for td in re.findall(r"<td.*?</td>", r, re.S):
                bg = re.search(r'bgcolor="#(\w+)"', td)
                fc = re.search(r'<font color="#(\w+)"', td)
                row.append(
                    {
                        "bg": bg.group(1) if bg else "",
                        "fc": fc.group(1) if fc else "",
                        "b": "<b>" in td,
                    }
                )
            grid.append(row)
        sheets.append(grid)
    return sheets


def col(grid, c, r0=0, r1=None):
    # list of fills in column c (0 based)
    return [row[c]["bg"] for row in grid[r0:r1]]
