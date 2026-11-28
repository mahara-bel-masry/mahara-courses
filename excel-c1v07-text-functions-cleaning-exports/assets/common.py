# helper: save a workbook, let LibreOffice recalculate it,
# and read back the values it really computed
import os, subprocess, tempfile, openpyxl


def calc(path):
    out = tempfile.mkdtemp()
    subprocess.run(
        ["soffice", "--headless", "--convert-to", "xlsx",
         "--outdir", out, path],
        capture_output=True, timeout=180,
    )
    return openpyxl.load_workbook(
        os.path.join(out, os.path.basename(path)),
        data_only=True,
    )


def csvgrid(path):
    # what LibreOffice shows in each cell (error codes included)
    import csv, io
    out = tempfile.mkdtemp()
    subprocess.run(
        ["soffice", "--headless", "--convert-to",
         "csv:Text - txt - csv (StarCalc):44,34,76,1,,0,false,true,false,false,false,-1",
         "--outdir", out, path],
        capture_output=True, timeout=180,
    )
    name = os.path.splitext(os.path.basename(path))[0]
    f = [x for x in os.listdir(out) if x.startswith(name)][0]
    return list(csv.reader(open(os.path.join(out, f), encoding="utf8")))
