# Data Analysis & BI diploma: research file v2.2
Research date: 2026-11-27 (all fetches done today). Author: second Mahara producer. Replaces v2.1. Status: planned. v2.2 changes: the per-ad table now lists every keyword counted (ETL and Looker/Qlik added), recomputed from the saved ad texts; the raw hit log is ads-keyword-hit-log.txt (same folder).
Changes vs v1: 38 ads (was 14) from Wuzzuf, LinkedIn, Indeed Egypt, Wellfound and Gulf boards; dates and levels per ad; competitor table; more certs; Excel and LibreOffice versions verified; video count lives in the outline only (excel-course-outline-v4.4.md: 31 videos, 29.9 h, a plan estimate).

## 1. Job ads
Method: every ad page was fetched and read as text (web_fetch). Keywords were matched case-insensitively against the full text (for example "power bi", "\bsql\b", "pivot"). Counts are LOWER BOUNDS: a tool named differently, or a page the fetcher cut short, is missed. Level is set by the years the ad asks for: Junior 0-2, Mid 2-5, Senior 5+ (a Cairo bank LinkedIn post is titled "Senior" but asks 2-3 years, counted Mid). Posting age comes from the page ("posted 5 months ago", a date, or "undated" when the page gives none; Wuzzuf ages are rounded). LinkedIn items marked "post" are recruiter hiring posts, not full ads. The sample is what search surfaced, not a random sample. Salaries: none collected, none stated.

Sample: 38 ads. Egypt 24 (Wuzzuf 15, Indeed EG 5, LinkedIn posts 3, Take-Off 1), Gulf 9 (Saudi and UAE), global remote 5 (Wellfound, US/EU/India based). Levels: Junior 8, Mid 17, Senior 10, unstated 3. Dated within the last 60 days: 15 (7 undated).

| Keyword | All 38 | Junior 8 | Mid 17 | Senior 10 | Egypt 24 | Gulf 9 | Last 60 days 15 |
|---|---|---|---|---|---|---|---|
| Power BI | 36 | 8 | 15 | 10 | 23 | 8 | 15 |
| SQL | 34 | 8 | 16 | 9 | 20 | 9 | 14 |
| Excel | 33 | 8 | 15 | 8 | 21 | 9 | 11 |
| Statistics | 21 | 6 | 10 | 5 | 12 | 8 | 9 |
| Tableau | 18 | 2 | 9 | 6 | 9 | 4 | 9 |
| Python | 18 | 2 | 9 | 6 | 9 | 6 | 8 |
| Power Query | 13 | 4 | 7 | 2 | 9 | 4 | 3 |
| PivotTable | 12 | 4 | 5 | 2 | 8 | 3 | 4 |
| DAX | 11 | 3 | 6 | 2 | 7 | 4 | 3 |
| ETL | 8 | 2 | 5 | 1 | 6 | 0 | 2 |
| Looker/Qlik | 8 | 1 | 5 | 1 | 3 | 2 | 4 |
| VBA/macro | 2 | 0 | 1 | 1 | 2 | 0 | 0 |
(Global remote 5: SQL 5, Power BI 5, Tableau 5, Excel 3, Python 3.)

What changed from v1 (14 ads said Excel 14/14): with 38 ads Excel is 33/38 and only 11 of the 15 recent ads. Power BI (36) and SQL (34) lead. Excel stays core but is no longer the clear first. So the diploma order stays Excel, SQL, Power BI because in my opinion Excel is the easiest first step (opinion, not measured), but Power BI and SQL get more depth, and Tableau is added as an optional short course because 18/38 name it (Tableau Desktop Specialist cert exists). Statistics asked in 21/38 and goes to its own course (see outline). VBA is nearly absent (2/38), so automation gets one section, not a course.

Per-ad table:
| # | Source | Region | Level (by years asked) | Posted | Keywords found | URL |
|---|---|---|---|---|---|---|
| 1 | Wuzzuf | Egypt | Senior | ~1 month | Excel, SQL, PBI, Tab, Piv | https://wuzzuf.net/jobs/p/dsxu2oogjuqo-senior-data-analyst-surgitech-cairo-egypt |
| 2 | Wuzzuf | Egypt | Mid | ~7 months | Excel, SQL, PBI, Tab, Py, PQ, DAX, Stat, ETL | https://wuzzuf.net/jobs/p/fzv9lnkvfsdn-data-analyst-zinoxmaster-cairo-egypt |
| 3 | Wuzzuf | Egypt | Senior | ~3 months | Excel, SQL, PBI, Py, PQ, DAX, Piv, VBA | https://wuzzuf.net/jobs/p/fii9e7ajad4m-senior-data-analyst-bi-automation-ai-driven-analytics-sky-restaurants-giza-egypt |
| 4 | Wuzzuf | Egypt | Junior | ~6 months | Excel, SQL, PBI, Tab, PQ, Piv, Stat, ETL, Looker/Qlik | https://wuzzuf.net/jobs/p/4m4sgsl4q0f7-data-analyst-analytics-knowledge-delivery-epsilonai-cairo-egypt |
| 5 | Wuzzuf | Egypt | Mid | ~6 months | Excel, SQL, PBI, Stat | https://wuzzuf.net/jobs/p/zadedm6ciygi-data-analyst-orchidia-pharmaceutical-industries-cairo-egypt |
| 6 | Wuzzuf | Egypt | Mid | ~1 year | Excel, SQL, PBI, PQ, DAX, Piv, Stat | https://wuzzuf.net/jobs/p/zb0s8o5r59sy-data-analyst-arma-hsa-cairo-egypt |
| 7 | Wuzzuf | Egypt | Senior | ~5 months | Excel, SQL, PBI, Tab, Py, Stat | https://wuzzuf.net/jobs/p/nhnpku0woshl-data-analyst-cairo-egypt |
| 8 | Wuzzuf | Egypt | Mid | ~9 months | Excel, SQL, PBI, Tab, Py, Stat, ETL, Looker/Qlik | https://wuzzuf.net/jobs/p/pt8vw0hn23aw-data-analyst-national-technology-group-giza-egypt |
| 9 | Wuzzuf | Egypt | Mid | ~2 years | Excel, SQL, PBI, Py, PQ, DAX, ETL | https://wuzzuf.net/jobs/p/1WhRT9rSVulx-Power-BI-Data-Analyst-Zeina-Group-Giza-Egypt |
| 10 | opus.sa | Gulf | Junior | 2026-10-26 | Excel, SQL, PBI, Py, PQ, DAX, Piv, Stat | https://www.opus.sa/en/job/data-analyst-hamad-bin-abdullah-al-manea-company |
| 11 | aehiring | Gulf | Senior | 2026-11-17 | Excel, SQL, PBI, Py, PQ, DAX, Stat | https://aehiring.com/saudi-arabia/5524/data-analyst-riyadh-saudi-arabia/ |
| 12 | Qarera | Gulf | Senior | 2026-11-04 | Excel, SQL, PBI, Stat | https://www.qarera.com/job/2675955 |
| 13 | Souq Junction | Gulf | Junior | 2026-11-16 | Excel, SQL, PBI, DAX, Stat | https://souqjunction.com/job/data-analyst-saudi-national-talents-sea-sa847732 |
| 14 | Assystem | Gulf | Mid | undated | Excel, SQL, PBI, PQ, DAX, Piv | https://www.assystem.com/en/career/offer/power-bi-dashboard-consultant-data-analytics/ |
| 15 | LinkedIn job | Gulf | Mid | ~4 months | Excel, SQL, Tab, Py, Stat, Looker/Qlik | https://www.linkedin.com/jobs/view/data-analyst-on-site-in-dubai-at-puffy-4432184841 |
| 16 | LinkedIn post | Egypt | Mid | 2026-10-03 | SQL, PBI | https://www.linkedin.com/posts/hiisham-mahmooud_were-hiring-a-senior-data-analyst-to-join-activity-7512109895983333376-QtQ_ |
| 17 | LinkedIn post | Egypt | Mid | 2026-11-01 | SQL, PBI, Tab, Py, Stat, ETL, Looker/Qlik | https://www.linkedin.com/posts/mohamed-elkadey-ab9164188_hiring-businessintelligence-dataanalytics-activity-7522623041642774528-LDiQ |
| 18 | LinkedIn post | Egypt | unstated | 2026-10-11 | PBI | https://www.linkedin.com/posts/hasnaa-hashim-a441071b6_hiring-salesdataanalyst-powerbi-activity-7514974493585567744-q8zB |
| 19 | LinkedIn post | Gulf | Senior | 2026-10-22 | Excel, SQL, PBI, Tab, Py, Stat | https://www.linkedin.com/posts/khaleejcareers_hiring-dataanalyst-dubaijobs-activity-7518883900836958208-PG15 |
| 20 | LinkedIn post | Gulf | Mid | 2026-11-03 | Excel, SQL, PBI, Tab, Py, PQ, Piv, Stat, Looker/Qlik | https://www.linkedin.com/posts/fama-group-uae_hiring-financeanalyst-dataanalyst-activity-7523364950988369921-rtZu |
| 21 | LinkedIn post | Gulf | Senior | 2026-11-09 | Excel, SQL, PBI, Tab, Py, Stat | https://www.linkedin.com/posts/talentac-budsbear-llc_dubaijobs-uaejobs-jobsindubai-activity-7525508400168833024-Yzka |
| 22 | Indeed EG | Egypt | Mid | undated | Excel, SQL, PBI, Tab, Py, Stat | https://eg.indeed.com/viewjob?from=serp&jk=2e98abb4eb44e01d&vjs=3 |
| 23 | Indeed EG | Egypt | Senior | undated | Excel, PBI | https://eg.indeed.com/viewjob?from=serp&jk=663ee8ce791d2f71&vjs=3 |
| 24 | Indeed EG | Egypt | unstated | undated | Excel, PBI, Piv | https://eg.indeed.com/viewjob?from=serp&jk=81b60809caa5fdd3&vjs=3 |
| 25 | Indeed EG | Egypt | Mid | undated | Excel, SQL, PBI, PQ, DAX | https://eg.indeed.com/viewjob?from=serp&jk=d8e3d898a815445d&vjs=3 |
| 26 | Indeed EG | Egypt | Mid | undated | Excel, SQL, Tab, VBA | https://eg.indeed.com/viewjob?from=serp&jk=ff44333fa5f78535&vjs=3 |
| 27 | Wellfound | Global remote | Mid | ~2 weeks | Excel, SQL, PBI, Tab, Looker/Qlik | https://wellfound.com/jobs/5041992-data-analyst |
| 28 | Wellfound | Global remote | Mid | ~4 weeks | Excel, SQL, PBI, Tab, Py, Piv, Stat, ETL | https://wellfound.com/jobs/4903543-data-analyst |
| 29 | Wellfound | Global remote | Senior | ~3 months | SQL, PBI, Tab, Py, ETL, Looker/Qlik | https://wellfound.com/jobs/4643340-senior-data-analyst-bi |
| 30 | Wellfound | Global remote | unstated | ~2 weeks | Excel, SQL, PBI, Tab, Py, Looker/Qlik | https://wellfound.com/jobs/5023985-business-intelligence-analyst |
| 31 | Wellfound | Global remote | Senior | ~3 weeks | SQL, PBI, Tab | https://wellfound.com/jobs/4995138-data-analyst-v-us |
| 32 | Wuzzuf | Egypt | Junior | ~5 months | Excel, SQL, PBI, Stat, ETL | https://wuzzuf.net/jobs/p/640syestbqib-junior-data-analyst-carina-wear-cairo-egypt |
| 33 | Wuzzuf | Egypt | Junior | ~9 months | Excel, SQL, PBI, PQ, Stat | https://wuzzuf.net/jobs/p/deipudnut5wh-junior-data-analyst-wadi-group-giza-egypt |
| 34 | Wuzzuf | Egypt | Junior | ~1 year | Excel, SQL, PBI, Tab | https://wuzzuf.net/jobs/p/7cg451fy7uxz-junior-data-analyst-yodawy-giza-egypt |
| 35 | Take-Off | Egypt | Junior | undated | Excel, SQL, PBI, Py, Piv, Stat | https://www.takeoff-egypt.com/jobs/junior-data-analyst-paymob-cairo-3bbda99e |
| 36 | Wuzzuf | Egypt | Mid | ~7 months | Excel, SQL, PBI, Py, DAX, Piv | https://wuzzuf.net/jobs/p/485eob7kytt8-data-analyst-sprix-cairo-egypt |
| 37 | Wuzzuf | Egypt | Mid | ~4 years (old) | Excel, PBI, PQ, Stat | https://wuzzuf.net/jobs/p/0T6a4KDMsFNn-Mid-Senior-Data-Analyst-Worex-Cairo-Egypt |
| 38 | Wuzzuf | Egypt | Junior | ~4 months | Excel, SQL, PBI, PQ, DAX, Piv | https://wuzzuf.net/jobs/p/pyqhdkta1ch6-hr-data-analyst-amreyah-cement-cairo-egypt |

## 2. Competitors (from pages fetched today; not from watching their videos)
| Path | Language | Size | Price | Project | Career part on page | Source |
|---|---|---|---|---|---|---|
| NU Professional Diploma in Data Analysis | not stated on page | 100 contact hours, 4 months | not on page | "practical projects" | words found: 2 | https://nu.edu.eg/all-programs/professional-diploma-data-analysis |
| predev Academy data analysis (Excel, Power Query, SQL, Power BI) | Arabic | 20 lectures, 40 hours | not checked | final project | none found | https://predevacademy.com/ar/courses/data-analysis-fundamentals |
| Machinfy data analysis diploma (6 tools) | Arabic | 6 months plan, hours not on page | 4900 EGP (struck 7500), or 898.33 EGP/month for 6 | churn dashboard, sales dashboard, capstone | none found | https://machinfy.com/ar/courses/data-analysis-Journey?view=instructor |
| almentor "Mastering data analysis" | Arabic | parts of 6h34, 5h59, 1h31 seen | not checked | not seen | none found | https://www.almentor.net/bundles/mastering-data-analysis |
| STJ Egypt beginners course | Arabic | 28 lessons, 31h55m | not checked | Walmart Power BI project, SQL project | words found: 3 | https://www.stjegypt.com/public/course/n/514 |
| Egypt 24 academy path | Arabic | 5 courses, about 15 hours, free, path certificate | free | not seen | none found | https://eg-24.com/courses/paths/data-analysis/ |
| Gomaa Intelligence | Arabic | 14 lessons + graduation project, "recording in progress" | to be announced | graduation project | none found | https://solutions.gomaaintelligence.me/foundations/course/ |
| Udemy Data Analysis Masterclass (Excel, SQL, Power BI, Python) | Arabic text seen | not read | not checked | hands-on projects | 2 words | https://www.udemy.com/course/data-analysis-masterclass-excel-sql-powerbi-python/ (rating 4.1 from 37, 199 students) |
| Google Data Analytics Certificate (Coursera) | English | 6 months at 10 h/week, beginner | subscription (price not checked) | capstone | yes (career resources) | https://www.coursera.org/professional-certificates/google-data-analytics (3,931,788 enrolled) |
| Luke Barousse Excel for Data Analytics | English | not checked | free | files on GitHub (1220 stars, no tests) | none | https://github.com/lukebarousse/Excel_Data_Analytics_Course |
| Route Academy Data Analysis diploma | Arabic (LinkedIn post) | grads post "6-month" diplomas | NOT obtained | NOT obtained | NOT obtained | NOT OBTAINABLE after 6 attempts: route.com.eg has no DNS record, routeacademy.net is a parked domain (cloud browser), www.routeacademy.net/diplomas 404, routeeg.com lists branch addresses only, Route's own LinkedIn post (2026-01-17) has no syllabus, web fetch of Route sites failed. https://ae.linkedin.com/posts/routeacademy_data-analysis-diploma-activity-7418398716606316544-tLz3 |
| EBI (Egypt) Data Analysis and Data Science Track | English (PDF) | 106 hours virtual; 30 h is analysis and visualisation | not on page | end-to-end project | none seen | https://ebi.gov.eg/wp-content/uploads/2024/11/Data-Analysis-and-Data-Science-Track.pdf (SPSS and Python, statistics, ML; no Excel/Power BI/SQL listed) |
| IBS Academy data analysis diploma | Arabic | 21 training hours, 7 lectures, live remote | USD 350 | not seen | none seen | https://ibsacademy.org/course-725-data-analysis-diploma.html |
ITI: no ITI Data Analysis syllabus page was found by search (results were Indian institutes with similar names), so ITI is not claimed.
Gaps seen on the pages above (page text only, not the videos): none of the 9 readable pages mentions GitHub. "Test" and "documentation" words appear on 3 pages only in the sense of quizzes and generic docs, not unit tests, CI or model review. Career words (CV, interview, LinkedIn, portfolio, freelance) appear on only 4 of 9 pages and as a single mention, not a module. Projects listed are dashboards and one SQL project. Size: the diploma-size competitors are about 31-100 hours. Course 1 plans 31 videos for Excel (29.9 h by the outline, a plan estimate), so it must earn that depth through the minute plans in the outline. Route's syllabus could not be obtained (see table); the Egyptian syllabi actually read are NU (100 h), EBI (106 h), predev (40 h), STJ (31h55), IBS (21 h), Machinfy, Egypt 24.

## 3. Certifications (official pages)
- PL-300 Power BI Data Analyst: skills measured as of April 20 2026 (Prepare 25-30%, Model 25-30%, Visualize 25-30%, Manage and secure 15-20%); renewal every 12 months (free online renewal assessment per Microsoft; price per country, not stated on page). https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-300/
- MO-211 Excel Expert (Microsoft 365 Apps): no retirement date on the page today; domains 10-15 / 30-35 / 25-30 / 25-30. Price per country. https://learn.microsoft.com/en-us/credentials/certifications/exams/mo-211/
- DP-900 Azure Data Fundamentals: price per country on page. https://learn.microsoft.com/en-us/credentials/certifications/exams/dp-900/ (optional, not covered).
- Tableau Desktop Specialist: registration fee USD 75 plus taxes. https://www.tableau.com/learn/certification/desktop-specialist (validity not stated on the page read).
- Google Data Analytics Certificate: see competitors table.
Not claimed: exact PL-300 and MO-211 USD prices (page shows price by country only).

## 4. Lab runtime, end-of-life and versions (all fetched 2026-11-27)
- Python 3.10.12 (machine default) is END OF LIFE since 2026-10-01 per https://devguide.python.org/versions/ (3.10 row "end-of-life", 2026-10-01) and https://endoflife.date/python . Not used for teaching. Installed supported Python 3.13.18 (security support until 2029-10 per the same pages; latest 3.13.18 on 2026-10-25) in user space with uv: `uv python install 3.13`, venv at /downloads/dabi/venv313, then `uv pip install pandas openpyxl` giving pandas 3.1.1, openpyxl 3.1.5, numpy 2.5.5. (pandas 3.x needs Python 3.11 or newer; confirmed pip could not see pandas 3 on 3.10.)
- LibreOffice 7.3.7.2 (machine default) ended support 2022-11-30 per https://endoflife.date/libreoffice (page updated 2026-11-14). Installed LibreOffice 26.8.3 (supported until 2027-06-13 per the same page) without root: downloaded the official deb tarball LibreOffice_26.8.3_Linux_x86-64_deb.tar.gz from download.documentfoundation.org/libreoffice/stable/26.8.3/deb/x86_64/ (221 MB), unpacked the core, calc, en-us, images, fonts, pyuno, python-script and nlpsolver debs with `dpkg -x` into /downloads/dabi/lo/root. `soffice --version` prints LibreOffice 26.8.3.1. It bundles Python 3.13.18 for UNO scripts. Note: LibreOffice 26.2 support ends 2026-11-30, so 26.8 is the right pick.
- Smoke tests on this runtime (today): XLOOKUP, LET, SORT, UNIQUE, FILTER all return correct values in LO 26.8.3 when the xlsx has the _xlfn prefixes (XLOOKUP 30, LET 130, SORT 5, UNIQUE 3, FILTER sum 25 on a 4-row test). Without prefixes they show #NAME?, so test files must be written with prefixes (note for scripts). Excel Table with structured reference: =SUM(tblSales[qty]) gives 15 and SUMIFS(tblSales[qty],tblSales[city],"Cairo") gives 8, correct. DataPilot (LibreOffice's PivotTable) via UNO: Alexandria 17, Cairo 41, Fayoum 6, Giza 28, total 92. Goal Seek via UNO: x=7 for x*x=49. Solver via UNO (CoinMP linear): maximise 3x+2y with x+y<=4, x<=3: x=3, y=1, objective 11. Chart object creation via UNO works (chart count 1; image export not yet tested). Arabic digits: format "#,##0.00" with ar-EG locale printed an odd value (12,345.68 for 1234567.5); NOT understood yet, so Arabic-Indic digits are marked [W] until a test passes. LibreOffice Basic macro run: not yet tested, so macros stay [W] until tested.
- Third-party function table for context: https://canispreadsheet.com/libreoffice-version-support.html (XLOOKUP/SORT/UNIQUE/LET supported since 24.8; FILTER and LAMBDA flagged "quirk"; our FILTER example worked).
- Microsoft Excel: current update post "What's New in Excel (November 2026)", Nov 24 2026: Copilot features (accounting skills [Frontier], PivotTable grouping [Insiders], read-only workbooks), descriptive error cards on Windows. https://techcommunity.microsoft.com/blog/excelblog/whats-new-in-excel-november-2026/4573867 . Course decision: Copilot in Excel is OUT OF SCOPE for Course 1 (most items are Frontier/Insiders preview); to be revisited when generally available, and the intro video says so.
- No Excel installed. Every ribbon and dialog name in scripts comes from the Microsoft Support pages listed per video in the outline (all 40 pages fetched and loaded today).

## 5. Official MO-211 objectives (PDF fetched in full today)
https://arch-center.azureedge.net/Learning/Credentials/MO-211_OD_MOS365_ExcelExpert.pdf . Domains: Manage workbook options and settings (10-15%); Manage and format data (30-35%); Create advanced formulas and macros (25-30%); Manage advanced charts and tables (25-30%). Full objective list is mapped video by video in the outline. Not in MO-211: Power Query and the Data Model (job-ad driven instead: Power Query 13/38 ads, DAX 11/38).

## 6. What changed vs v2
Route not obtainable (documented); EBI and IBS added; Python 3.13.18 and LibreOffice 26.8.3 installed and tested; EOL cited; MO-211 objectives mapped; Copilot scope stated; XLOOKUP and dynamic arrays now real runs.
