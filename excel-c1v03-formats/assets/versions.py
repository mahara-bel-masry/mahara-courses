import sys, openpyxl, subprocess

print(
    "Python",
    sys.version.split()[0],
    "| openpyxl",
    openpyxl.__version__,
)
print(
    subprocess.run(
        ["soffice", "--version"],
        capture_output=True,
        text=True,
    ).stdout.strip()
)
