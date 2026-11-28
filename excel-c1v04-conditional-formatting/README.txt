Excel C1 video 4 lesson files (conditional formatting).
Run everything from THIS folder (the one that holds assets, run, data, lab). Paths inside the scripts are relative.
Setup: Python 3.13, pip install openpyxl==3.1.5 ; LibreOffice 26.8.3.1 (soffice on PATH) is used to read the colours it draws (HTML export). Logged versions: run/versions.out.
Example: python assets/highlight.py (compare with run/highlight.out). Other scripts: extra_rules (between, blanks, dates), topavg, formula_rules, scales_bars, priority, edge_cases, scenario. Logs are in run/*.out.
Lab: python lab/make_lab.py ; solution: python lab/make_solution.py ; logs in run/lab.out and run/solution.out
All results come from Python and LibreOffice, not Microsoft Excel. All data is made up.
LibreOffice HTML export does not show data bars or icons: those two are only read back from the saved file (rule type), not seen.
First-match-wins behaviour is what LibreOffice did. It is not claimed for Excel.
The first sentence of the video is in script/00-opening-line.txt.
