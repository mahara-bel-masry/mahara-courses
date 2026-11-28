# versions used for every run in this lesson
import sys, subprocess, openpyxl

print("python", sys.version.split()[0])
print("openpyxl", openpyxl.__version__)
v = subprocess.run(
    ["soffice", "--version"],
    capture_output=True,
    text=True,
).stdout.split()
print("libreoffice", v[1])
