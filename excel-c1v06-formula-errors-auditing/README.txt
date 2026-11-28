Excel C1 video 6 lesson files (formula errors and auditing).
Run everything from THIS folder (the one that holds assets, run, data, lab). Paths inside the scripts are relative.
Setup: Python 3.10, pip install openpyxl==3.1.5 ; LibreOffice 26.8.3.1 (soffice on PATH) recalculates each workbook so we can read the values it computed. Logged versions: run/versions.out.
Scripts and logs: errors (seven error values, one error spreading, IF and IFERROR, blank versus zero), texts (numbers stored as text), audit (my own audit script on a made-up sales sheet, with a trace by my script), evaluate_steps (the Microsoft Evaluate Formula example done by hand in cells). Logs are in run/*.out. circular.py and run/circular.out are extra and are not used in the video.
Lab: python lab/make_lab.py ; solution: python lab/make_solution.py ; logs in run/lab.out and run/solution.out
All results come from Python (openpyxl) and LibreOffice (the values), not Microsoft Excel. All data is made up. The audit script is mine, not Excel's Error Checking.
Error Checking, Ignore Error, Trace Precedents and Dependents arrows, the Evaluate Formula dialog, the Watch Window and the #### column width were NOT run. They come from the Microsoft pages in microsoft-pages/ (list in ms-urls.txt) and are marked untried in the narration.
On screen the code panels wrap lines longer than 80 characters for display only. The files here are the originals.
The first sentence of the video is in script/00-opening-line.txt.
