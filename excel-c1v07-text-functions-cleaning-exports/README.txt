Excel C1 video 7 lesson files (text functions and cleaning exports).
Run everything from THIS folder (the one that holds assets, run, data, lab). Paths inside the scripts are relative.
Setup: Python 3.10, pip install openpyxl==3.1.5 ; LibreOffice 7.3.7.2 (soffice on PATH) recalculates each workbook so we can read the values it computed. Logged versions: run/versions.out. Lessons 1 to 6 used LibreOffice 26.8.3.1; this lesson was run on 7.3.7.2 because the machine was restarted and only that build was available. The two versions were not compared.
Scripts and logs: trim_clean (TRIM and CLEAN on six cases), extract (LEFT, MID, RIGHT, edge cases, text versus number), substitute, textjoin, scenario (shop export), scenario2 (invoice export), unicode_ids (UNICODE of the last character, fixed MID position on ids of different length). Logs are in run/*.out.
Lab: python lab/make_lab.py ; solution: python lab/make_solution.py ; logs in run/lab.out and run/solution.out
All results come from Python (openpyxl) and LibreOffice (the values), not Microsoft Excel. All data is made up. TEXTJOIN, UNICHAR and UNICODE are written with the _xlfn. prefix in openpyxl; without it LibreOffice returned NAME.
In this LibreOffice, UNICODE of CHAR(160) is 65533 and UNICODE of UNICHAR(160) is 160, so the nonbreaking-space fix uses UNICHAR(160). Not tested in Excel.
The Microsoft Top ten page steps (backup, new column, formula, fill down, paste values, remove the original) and TEXTJOIN availability (Office 2019 or Microsoft 365) were NOT run. They come from the Microsoft Support pages linked in the video description.
On screen the code panels wrap lines longer than 80 characters for display only. The files here are the originals (assets_orig scripts are in assets/).
The first sentence of the video is in script/00-opening-line.txt.
