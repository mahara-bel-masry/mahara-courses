# Course 1: Excel للتحليل والشغل, outline v4.5 (new standard)
Diploma: Data Analysis & BI, Course 1 of 5. Status: planned. Research: dabi-research-v2.2.md. ONE video count: 31 videos in this table, 1795 min = 29.9 h, say "about 30 hours" (the reviewer's 32 h estimate assumed 13a/13b and 3b stayed separate; the merges bring it to 29.9). Course intro video 0 is a required video and is counted separately from the 31 lesson videos: its text is 655 words; measured after voicing: narration 4:33 (273.4 s), 4:37 with the 4 s cover and explainer; the diploma intro (video 0 of the diploma, separate) measured 5:26 narration, 5:30 with cover; with the course intro the course has 32 videos. Career content lives in C5.
v4.3 default = the reviewer's recommendation: the four optional cuts (13c, 16b, 22b, 26c) and the under-50-minute merges (23b into 23, 26c into 26b, 3b into 3, Flash Fill into 12a, Fill Series into 5, 13a dropped as its own video).


## Labels (three only, on screen and in the description)
[R] real run: the computation or function ran for real on the lab runtime (LibreOffice 26.8.3 Calc, Python 3.13.18, pandas 3.1.1) and the function has Excel's documented behaviour (SUMIFS, IF, XLOOKUP...).
[L] local substitute: a different product feature stands in for the Excel feature (LibreOffice DataPilot for PivotTable, LibreOffice charts, Goal Seek, Solver, conditional formatting, LibreOffice Basic for macros). Screen says "picture is LibreOffice, Excel looks different".
[W] written, not run here: Excel-only steps and formulas (Power Query, Data Model, Office Scripts, Flash Fill, slicers, Evaluate Formula, Watch Window, GitHub Actions).
Pandas checks and any Python are for OUR verification of numbers only; learners need Excel only (capstone uses an in-workbook check sheet).
Lab runtime (cited in research v2.2 section 4): Python 3.13.18 (3.10 is EOL), LibreOffice 26.8.3 (7.3 is EOL).

## Diploma map
C1 Excel (this). C2 SQL for analysts. C3 Power BI and DAX (PL-300 mapped). C4 Statistics for analysts (business statistics in Excel/SQL; Python is optional there). C5 Career and capstone portfolio (CV, LinkedIn, GitHub, interview bank, mock interviews, freelancing, negotiation; salaries only with dated sources). Tableau optional after C3 (18/38 ads).
Existing held packages: Excel C1 (19 short packages), SQL C2 (19), Power BI C3 (19) were produced earlier at about one minute each and are NOT published (held by the user's 20-minute rule). This new standard replaces them. Decision needed from main: confirm those 57 held short packages are retired for this diploma (nothing of this diploma is live on the channel).


## Boundary vs what is published or queued (real DE titles supplied by main 16:16)
| Existing item (source) | Overlap risk | Rule for this diploma |
|---|---|---|
| DE diploma, 81 videos live incl. DE SQL | SQL basics, joins | C2 SQL for analysts teaches analyst reporting queries (cohorts, KPIs), references the DE SQL videos instead of repeating basics. Published DE videos: 21 tables/relations/constraints, 22 SELECT/WHERE/ORDER/GROUP BY, 23 JOIN + double-counting trap, 24 subqueries/CTEs, 25 window functions, 26 indexes, 27 normalization, 28 store DB project. C2 does not repeat them: it links 21-25 and adds analyst work only (KPI/cohort/retention queries, SQL against exported Excel data, reconciling SQL with a pivot). Python 9-20 (incl. 14 files CSV/JSON/Excel, 17 pandas cleaning): C1 never teaches Python. Git 36-41 (37 conflict resolution): video 27 teaches only analyst Git (init, add, commit, README, folders, push) and links 36-41. DE 81 capstone is a DE project: ours is a reporting capstone. |
| AI&DS C1 parts 1-6 (queued, one is "الجزء 6 | Python للـ Data Science | مشروع صغير وقواعد البيانات SQL") | pandas, SQL intro | This diploma uses Python only as our check; no Python teaching in C1. C4 Python part links to AI&DS C1. |
| AI&DS C2 parts 7-10 (queued; part 9 correlation and causation, part 10 linear regression) | statistics | C4 covers business statistics in Excel (descriptive, sampling, confidence, A/B reading), refers to AI&DS C2 for regression and probability theory. No regression lesson in C4. |
| First producer's Power BI outline v1 (held short package) | Power BI | C3 rebuilds it to the new standard; C1 video 19 only introduces the Data Model and says "continue in C3". |

## Objectives, prerequisites, outcomes

## Objectives, prerequisites, outcomes
Prerequisite: can open a file on a computer. Outcomes (measurable): (1) rebuild the capstone monthly sales report from the raw files in under 60 minutes with zero error cells and a matching in-workbook Check sheet; (2) catch the 5 data-type traps with the 5-check gate; (3) explain each formula aloud; (4) 50-question MO-211-style practice set (our own questions) 70%+; (5) one working GitHub repo with README. Assessment: 5-question quiz and a lab with solution file per video; final = capstone rebuild.

Structure of every video (8 parts): hook 2, map 3, concept + live 20-26, mistakes 8-10, company scenario 6-8, lab + solution 10-14, summary + quiz 5, next 1 (minutes are the targets; each video budget is below).

## Video list
| # | One goal | Min | Label | Sources |
|---|---|---|---|---|
| 1 | How Excel stores data: number, text, date; the 5 traps; COUNT vs COUNTA gate | 60 | R | Available number formats; Create and format tables |
| 2 | Tables, structured references, named ranges, a data-ready layout | 55 | R (structured refs tested: 15 and 8) | Create and format tables |
| 3 | Control how values display: number, date and time formats, custom formats, and the Egypt regional settings a Microsoft page documents (list separator, RTL sheet, date order) | 65 | R custom formats; L RTL sheet; W list separator, Arabic-Indic digits and RTL (documented only, not claimed to work) | Review guidelines for customizing a number format; Formula errors when list separator isn't set correctly; Add an editing or authoring language |
| 4 | Conditional formatting: custom rules, formula rules, data bars/colour scales/icon sets, manage rules | 55 | L | Use conditional formatting to highlight information; Use data bars, color scales, and icon sets |
| 5 | Formulas and references (relative, absolute, mixed), calculation options; Fill handle and Fill Series (moved from 13) | 55 | R | Overview of formulas in Excel |
| 6 | Formula errors and auditing: error types, Trace Precedents/Dependents, Error Checking, Evaluate Formula, Watch Window | 55 | R errors, L trace, W Evaluate Formula and Watch Window | Detect formula errors in Excel; Display the relationships between formulas and cells; Watch a formula and its result by using the Watch Window |
| 7 | Text functions and cleaning exports (LEFT, MID, TRIM, CLEAN, SUBSTITUTE, TEXTJOIN) | 60 | R | Text functions (reference) |
| 8 | Dates and time logic: TODAY, NOW, WEEKDAY, WORKDAY and WORKDAY.INTL with the Friday-Saturday Egypt weekend, EOMONTH, NETWORKDAYS, aging buckets | 55 | R | NETWORKDAYS function; EOMONTH function |
| 9 | Logic: IF, IFS, SWITCH, AND, OR, NOT, IFERROR | 60 | R | IFS function; SWITCH function |
| 10 | Conditional aggregation: SUMIF(S), COUNTIF(S), AVERAGEIF(S), MAXIFS, MINIFS, SUMPRODUCT, reconcile to a control total | 65 | R | SUMIFS function |
| 11 | Lookups: VLOOKUP, HLOOKUP, MATCH, INDEX, XLOOKUP, exact vs approximate, two-way lookup | 60 | R (XLOOKUP real on LO 26.8) | XLOOKUP function |
| 12a | Turn an export column into clean columns: Text to Columns and Flash Fill | 55 | W (Excel dialogs, cited per step); pandas shows the same split as our check | Split text into different columns https://support.microsoft.com/en-us/excel/get-started/split-text-into-different-columns-with-the-convert-text-to-columns-wizard ; Flash Fill https://support.microsoft.com/en-us/excel/using-flash-fill-in-excel |
| 12b | Data quality: Remove Duplicates, data validation, and the data-quality log | 60 | R duplicates check by formula; W dialogs | Filter for unique values or remove duplicate values; Apply data validation to cells |
| 13 | Summarise a sorted list with Subtotal and Group/Outline | 55 | L (LibreOffice Subtotals and Group) | Subtotals https://support.microsoft.com/en-us/excel/insert-subtotals-in-a-list-of-data-in-a-worksheet ; Group (outline-group page removed: the URL opens the PivotTable grouping page, so the Group/Outline part is cited by the Subtotals page only until a worksheet-outline page is found) |
| 14 | PivotTables: build, group dates, value field settings, calculated fields, slicers | 65 | L DataPilot (tested, total 92), W slicers and calculated fields UI | Create a PivotTable to analyze worksheet data |
| 18 | Power Query: repeatable ETL, merge vs append, a folder of files, query folding limits | 65 | W (pandas gives the same output) | About Power Query in Excel; Create, load, or edit a query |
| 19 | Data Model and relationships, intro to measures, when to move to Power BI | 55 | W | Create a relationship between tables in Excel |
| 17 | Dynamic arrays and LET: FILTER, SORT, SORTBY, UNIQUE, spill, compatibility with older Excel; RANDARRAY as the sample-data generator (moved from 13) | 55 | R on LO 26.8 (prefix note), W for spill behaviour display | FILTER function; SORT function; UNIQUE function |
| 15 | Charts that answer a question: chart choice, combo, dual-axis, design mistakes | 55 | L | Create a chart from start to finish |
| 16 | Read the spread of your data: Histogram and Box & Whisker charts | 50 | W (LibreOffice lacks both; every step cites its page; narration says no Excel was run) | Histogram https://support.microsoft.com/en-us/excel/create-a-histogram ; Box&Whisker https://support.microsoft.com/en-us/excel/create-a-box-and-whisker-chart |
| 20 | What-if: Goal Seek, Scenario Manager, data tables | 55 | L Goal Seek (x=7 tested), W Scenario Manager and data table UI | Introduction to What-If Analysis; Use Goal Seek; Calculate multiple results by using a data table |
| 21 | Solver: three models (product mix, staffing, transport), constraints, infeasible models, reading sensitivity | 60 | L (LO Solver tested: 3, 1, objective 11) | Define and solve a problem by using Solver |
| 22 | Loans and savings: PMT, NPER, FV with EGP examples | 55 | R, documented examples checked in LO (support_examples.log) | PMT, NPER, FV pages |
| 23 | Automate a repeated task: record, name, edit and safely run a macro; Office Scripts shown as the cloud alternative | 60 | W until a LibreOffice Basic run passes; every step cites its page; narration says no Excel was run | Quick start: Create a macro; Introduction to Office Scripts in Excel; Differences between Office Scripts and VBA macros |
| 24 | Dashboard design: layout, KPI cards, one-screen rule, colour accessibility; PivotChart drill down (moved from 16) | 60 | L | Create a PivotTable...; Create a chart from start to finish |
| 25 | Performance and file quality: calculation options, volatile functions, large files, workbook versions | 50 | R timing in LO | Overview of formulas in Excel (calc options) |
| 26a | Protect sheets, ranges and workbook structure | 50 | L | Protect a worksheet; Protect a workbook |
| 26b | Review a model: checklist, documentation, audit trail and workbook versions | 55 | R checklist; W Inquire and version history | Analyze a workbook with Spreadsheet Inquire; View previous versions of Office files |
| 27 | Git and GitHub basics for analysts: repo, commit, README, folders, what a GitHub Action is | 55 | R (git run locally, log smoke/smoke_git.log), W (Actions) | Pro Git https://git-scm.com/book/en/v2 ; GitHub quickstart https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories ; Actions https://docs.github.com/en/actions/get-started/understand-github-actions |
| 28 | Capstone 1: brief, invented 3 raw files, build the workbook step by step | 70 | R + L | all above |
| 29 | Capstone 2: Check sheet, README with screenshots, optional CI template, release | 65 | R, W for CI | all above |

## Density budgets (each line sums to the table minutes; no padding, a script under 50 min gets a real extra section)
2 (55): hook 2, map 3, Tables 14, structured refs 12, named ranges 7, mistakes 5, scenario 5, lab 5, summary 2.
3 (65): hook 2, map 3, values vs formats 8, number and date formats 9, custom formats with 3 examples 9, regional settings (list separator, RTL, date order, as documented) 10, mistakes 7, scenario 6, lab 9, summary 2.
4 (55): hook 2, map 3, rule types 6, 3 worked rules on 2 datasets 14, formula rules and managing rules 6, mistakes 5, scenario 5, lab 9, summary 5.
5 (55): hook 2, map 3, relative 8, absolute 7, mixed 7, fill handle and Fill Series 5, calc options 5, mistakes 5, scenario 5, lab 6, summary 2.
8 (55): hook 2, map 2, serial dates 6, WEEKDAY/WORKDAY/WORKDAY.INTL Fri-Sat 11, EOMONTH/NETWORKDAYS 7, aging buckets 7, mistakes 5, scenario and lab 10, summary 5.
9 (60): hook 2, map 3, IF 8, IFS and SWITCH 10, AND/OR/NOT 8, IFERROR 5, mistakes 6, scenario 6, lab 10, summary 2.
12a (55): hook 2, map 3, why exports are messy 5, Text to Columns on 3 export shapes 14, Flash Fill 10, mistakes 5, scenario 5, lab 9, summary 2.
12b (60): hook 2, map 3, Remove Duplicates and what counts as a duplicate 10, data validation 5 rule types 14, data-quality log 8, mistakes 5, scenario 6, lab 10, summary 2
13 (55): hook 2, map 3, sort first 4, Subtotal 12, Group and Outline 10, mistakes 5, scenario 5, lab 12, summary 2.
15 (55): hook 2, map 3, chart choice 10, combo and dual axis 10, design mistakes 8, scenario 6, lab 14, summary 2.
16 (50): hook 2, map 3, distributions 6, Histogram bins 10, Box & Whisker 9, mistakes 4, scenario 4, lab 10, summary 2.
17 (55): hook 2, map 3, FILTER 8, SORT/SORTBY 7, UNIQUE 6, LET 6, RANDARRAY sample data 5, compatibility and spill 5, mistakes 3, lab 8, summary 2.
21 (60): hook 2, map 2, model anatomy 6, three models 20, infeasible and sensitivity 7, mistakes 5, scenario 5, lab 9, summary 4.
22 (55): hook 2, map 3, PMT 10, NPER 8, FV 8, EGP examples 6, mistakes 5, scenario 5, lab 6, summary 2.
23 (60): hook 2, map 3, what a macro is and security 7, record and name 8, edit the code 10, copy between workbooks 5, Office Scripts as the cloud alternative 8, mistakes 4, lab 11, summary 2.
24 (60): hook 2, map 3, layout 8, KPI cards 8, PivotChart drill down 10, one-screen rule 5, accessible colours 5, mistakes 4, scenario 5, lab 8, summary 2.
25 (50): hook 2, map 3, calc modes 8, volatile functions 8, large files 8, mistakes 5, scenario 5, lab 9, summary 2. (hold: LO timing log first)
26a (50): hook 2, map 3, protect a worksheet 9, ranges 8, structure 6, passwords honesty 4, mistakes 4, scenario 4, lab 8, summary 2.
26b (55): hook 2, map 3, review checklist 14, documentation 8, audit trail 6, versions 6, mistakes 3, scenario 4, lab 7, summary 2.
28 (70): hook 2, brief 5, generator and raw files 10, build the workbook 38, mistakes 5, hand-off 8, summary 2.
29 (65): hook 2, Check sheet 15, README and screenshots 15, optional CI template 10, release 8, mistakes 5, lab 8, summary 2.
Others keep the density already accepted in REVIEW 1c.

## MO-211 objective map (official PDF) after the cuts
Workbook options: Copy macros, Enable macros 23; Reference data in other workbooks 5; Manage workbook versions 26b; Restrict editing, Protect worksheets and ranges, Protect structure 26a; Calculation options 5, 25.
Manage and format data: Flash Fill 12a; advanced Fill Series 5; RANDARRAY 17; Custom number formats 3; Data validation, Remove duplicates 12b; Group/ungroup, Subtotals 13; Conditional formatting rules 4.
Formulas and macros: IF/IFS/SWITCH/AND/OR/NOT 9; SUMIF(S), COUNTIF(S), AVERAGEIF(S), MAXIFS, MINIFS 10; LET, FILTER, SORTBY 17; lookups 11; NOW/TODAY, WEEKDAY/WORKDAY 8; Goal Seek and Scenario Manager 20; PMT 22; trace precedence/dependence, Watch Window, error checking, Evaluate Formula 6; record, name, edit macros 23.
Charts and tables: dual-axis and Combo 15; Box & Whisker and Histogram 16; PivotTables 14; PivotCharts create, options, styles, drill down 14 and 24.
UNCOVERED by design after the cuts (listed, not hidden): Consolidate (cut 13c), Funnel, Sunburst and Waterfall charts (cut 16b), forecast with AND/IF/NPER (cut 22b, NPER is taught as a function in 22). The learner who wants the MO-211 exam must study these from the Microsoft pages linked in the course repo; the course does not claim to cover the whole exam. Also not MO-211 but in the job ads: Power Query 18, Data Model 19, Solver 21, governance 26.

## Egypt and Arabic specifics (video 3 (one section) and elsewhere)
Arabic interface and RTL sheets, list separator semicolon vs comma (Microsoft Learn page above), Arabic-Indic digits, date order day/month/year and parsing, EGP currency, Friday-Saturday weekend in WORKDAY.INTL (video 8), Arabic text in LEFT/MID and TRIM, mixed RTL/LTR cell text. Each is labelled R, L or W as in the table; the Arabic-Indic digit run is not yet proven.


## Project (videos 28-29) and how it is built (pattern P)
How built, said in the video: we invented 3 raw files with a Python generator (seeded, so reproducible), built the workbook in LibreOffice step by step following the same steps the learner follows in Excel, wrote a Check sheet with formulas that recompute totals two independent ways, and verified the numbers with pandas. Repo: README with screenshots (labelled LibreOffice), sample-data statement, raw files, workbook, check template, docs, optional GitHub Actions workflow that runs the check script on the sample data ([W], not run here). Nothing is pushed to GitHub by me; the publisher flow does that after PASS.


## Evidence and logs
smoke_funcs.log (26 functions), smoke_uno.log (DataPilot, Solver, chart), smoke_git.log, support_examples.log (Microsoft Support documented examples vs LO 26.8.3). WORKDAY.INTL with weekend 0: Microsoft page says #NUM!, LibreOffice returns #VALUE!, not run in Excel; the lesson states both. Smoke tests for FORECAST/TREND not needed (22b cut). Tests for 12a, 13, 23 (LO Subtotals, Basic) will be run and logged before those scripts, and labels stay W until then. Arabic-Indic digits and RTL stay [W] and are never said to work on camera. Demo assets for video 1 were rerun on Python 3.13.18 / pandas 3.1.1 / LO 26.8.3: same results (SUM 84, COUNT 17, COUNTA 20, 3 text rows, total 92, revenue 18950), logs in x1/run26.
Scripting status after REVIEW 1e: allowed 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 21, 24, 27, then 28 and 29. Held: 3, 12a, 12b, 13, 16, 22, 23, 25, 26a, 26b. Video 0 intro: the user decides who voices it; not scripted.
Pattern AC applied: every split re-budgeted against 50-70 min and the objective map updated.

## References and alternatives
Microsoft Support pages in the table; Excel Nov 2026 update post (Copilot is out of scope for C1, stated in video 1). Alternatives named in one line: Google Sheets (QUERY, ARRAYFORMULA), LibreOffice Calc (free; 24.8+ has XLOOKUP/SORT/UNIQUE/LET).

12a rule (REVIEW 1f): narration says plainly that no Excel was run and that the pandas check is our check only.
