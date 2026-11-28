# helper: write cells with number formats, let
# LibreOffice show them as text (CSV "as shown"),
# return the displayed strings
import openpyxl, subprocess, csv, os, shutil


def shown(path_xlsx, outdir="data/csv"):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(
        [
            "soffice",
            "--headless",
            "--convert-to",
            "csv:Text - txt - csv (StarCalc):"
            "44,34,76,1,,0,false,true,true,false,false,-1",
            "--outdir",
            outdir,
            path_xlsx,
        ],
        capture_output=True,
        timeout=120,
    )
    # -1 = every sheet to its own csv file
    base = os.path.splitext(
        os.path.basename(path_xlsx)
    )[0]
    res = {}
    for f in sorted(os.listdir(outdir)):
        if f.startswith(base + "-") and f.endswith(
            ".csv"
        ):
            res[f[len(base) + 1 : -4]] = list(
                csv.reader(
                    open(
                        os.path.join(outdir, f),
                        encoding="utf8",
                    )
                )
            )
    return res
