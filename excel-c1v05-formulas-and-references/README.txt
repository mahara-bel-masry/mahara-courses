Excel C1 video 5 lesson files (formulas and references).
Run everything from THIS folder (the one that holds assets, run, data, lab). Paths inside the scripts are relative.
Setup: Python 3.10, pip install openpyxl==3.1.5 ; LibreOffice 26.8.3.1 (soffice on PATH) recalculates each workbook so we can read the values it computed. Logged versions: run/versions.out.
Scripts and logs: copy_rules (four reference types, invoice), mixed_sheets (times table, other sheets, whole row and column), stale_values, calc_mode, mistakes, scenario, running. Logs are in run/*.out.
Lab: python lab/make_lab.py ; solution: python lab/make_solution.py ; logs in run/lab.out and run/solution.out
All results come from Python (openpyxl Translator for the copy step) and LibreOffice (the values), not Microsoft Excel. All data is made up. The tax rate and the exchange rate are invented.
Copying by dragging the fill handle, Fill Series, F4, calculation shortcuts and Manual calculation were NOT run. Those steps come from the Microsoft pages in c1..c7.txt and are marked untried in the narration.
The first sentence of the video is in script/00-opening-line.txt.
