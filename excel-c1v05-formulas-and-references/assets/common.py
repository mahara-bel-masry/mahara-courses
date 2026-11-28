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
