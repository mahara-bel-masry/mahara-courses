# Course 2: SQL للمحللين, outline v2 (v1 PASS as a plan; video 33 split in two, 34-36 renumbered 35-37, per reviewer) (new standard, inside the Data Analysis & BI diploma)
Diploma: Data Analysis & BI, Course 2 of 5. Status: planned (user order 2:03 AM Nov 28: SQL is taught fully in this diploma, not linked to the Data Engineering diploma; and 2:04 AM: "explain SQL and upload it in order").
Count: 37 lesson videos, 2135 min = 35.58 h, say "about 36 hours" (plan estimate, not a measurement). Course intro video 0 (about 5 min, counted separately, text to the reviewer first) makes 38 with the intro. Every lesson is 50 to 70 min, one goal, numbered, 8 parts, opens with one line saying what we will explain, then 4 s cover + explainer (Canva).
Research: dabi-research-v2.2.md (38 ads) + sql-dialect-hit-log.txt (same 38 ads re-fetched Nov 28 02:04, per-ad dialect and topic hits) + smoke_sql.log (real runs).

## Research results that decide the content (lower bounds, small sample, collected by me)
Ads with SQL: 34 of 38. Engines named across the 38 ads: SQL Server (SQL Server, T-SQL, SSMS, SSIS) 8, Oracle 5, BigQuery 3, MySQL 2, Snowflake 2, Redshift 1, PostgreSQL 0. Topics named: KPI 18, joins 13, query optimisation or indexing 12, window functions 3, data warehouse 2, stored procedures 1. Per-ad table in sql-dialect-hit-log.txt. Ads often write "SQL" without an engine, so no engine is claimed as the market standard.
Decisions from that: (1) teach standard SQL first on one free local engine; (2) joins, KPIs and performance get full videos (14-17, 26-27, 32); (3) window functions are taught fully even though only 3 ads name them (an analyst skill that interview questions use, my opinion, not measured); (4) two videos on engine differences (33 T-SQL and Oracle, 34 MySQL, PostgreSQL, BigQuery) written from vendor pages, no claim that it was run; (5) stored procedures and other engine-specific features are NOT taught (1 ad), named in videos 33 and 34 only.

## Lab engine and labels
Engine: SQLite 3.53.1 through Python 3.13.18 [R], free, runs on any computer (learner needs SQLite 3.39 or newer for RIGHT/FULL JOIN (the intro and every description say so); SQLite 3.37.2 on my other Python printed "RIGHT and FULL OUTER JOINs are not currently supported", see smoke_sql_py310.log; SQLite 3.39.0 release notes list the support, https://www.sqlite.org/releaselog/3_39_0.html). Window functions need 3.25+ (https://www.sqlite.org/windowfunctions.html). Smoke runs: smoke_sql_py313.log (window functions, CTE, recursive CTE, LEFT/RIGHT/FULL JOIN, EXCEPT, date all [R]).
Labels: [R] real run on SQLite 3.53.1, [W] written from vendor docs, not run (video 33 and the TOP/FETCH FIRST lines in video 2). [L] not used. Nothing was run on SQL Server, Oracle, MySQL, PostgreSQL or BigQuery and the videos say so. Data and companies are invented and say so. DuckDB 1.5.6 is NOT part of the course; I only used it once as a cross-check of the smoke queries (same results where SQLite supports them).
Narration is digit-free. Every number in narration appears in a saved log in the package (run/*.out).

## Boundary vs the Data Engineering diploma
The user's order: this diploma must stand on its own. No video and no description sends the learner to the DE diploma for SQL basics. DE keeps its own short SQL videos; nothing here depends on them. (Memo for main: the earlier boundary table row "reference the DE SQL videos" is withdrawn.)

## Video list
| # | One goal | Min | Label | Sources |
|---|---|---|---|---|
| 1 | What a database is: tables, rows, columns, the lab database, run your first query | 55 | R | sqlite.org lang_select |
| 2 | SELECT: columns, aliases, expressions, DISTINCT, LIMIT (and TOP / FETCH FIRST in other engines) | 55 | R, W for TOP and FETCH FIRST | SQLite SELECT; Microsoft Learn TOP; Oracle row limiting |
| 3 | WHERE: comparisons, AND/OR/NOT, IN, BETWEEN, LIKE | 60 | R | SQLite SELECT |
| 4 | ORDER BY, sorting rules, ties, NULL position, paging with LIMIT/OFFSET | 50 | R | SQLite SELECT |
| 5 | Data types and casting: text, numbers, dates stored as text, CAST, what SQLite does differently | 60 | R | SQLite datatype page |
| 6 | Text functions: LENGTH, SUBSTR, TRIM, REPLACE, UPPER/LOWER, concatenation, LIKE vs INSTR | 55 | R | SQLite core functions |
| 7 | Date and time functions: date(), strftime, month buckets, date differences | 55 | R | SQLite date and time functions |
| 8 | CASE expressions: buckets, flags, conditional counts | 55 | R | SQLite expression syntax |
| 9 | NULL in depth: three-valued logic, IS NULL, COALESCE, NULLIF, NULL in sums and counts | 50 | R | SQLite expression syntax |
| 10 | Aggregates: COUNT, SUM, AVG, MIN, MAX; COUNT(*) vs COUNT(column) vs COUNT(DISTINCT) | 60 | R | SQLite aggregate functions |
| 11 | GROUP BY: one and many columns, group labels, a report table | 60 | R | SQLite SELECT |
| 12 | HAVING, WHERE vs HAVING, and the order a query runs in | 55 | R | SQLite SELECT |
| 13 | Keys and relationships: primary key, foreign key, reading a schema and an ERD | 50 | R | SQLite foreign keys |
| 14 | INNER JOIN: one key, many keys, joining three tables | 65 | R | SQLite SELECT (join) |
| 15 | LEFT, RIGHT and FULL joins, and the anti-join (rows with no match) | 65 | R, SQLite 3.39+ | SQLite 3.39.0 release notes |
| 16 | Join traps: fan-out, double counting, duplicate keys, many-to-many | 60 | R |  |
| 17 | Self join, cross join, and a calendar table | 55 | R |  |
| 18 | UNION, UNION ALL, INTERSECT, EXCEPT | 50 | R | SQLite compound SELECT |
| 19 | Subqueries: scalar, IN, EXISTS, correlated | 60 | R | SQLite SELECT |
| 20 | CTEs: readable queries, several CTEs, recursive CTE intro | 60 | R | SQLite WITH clause |
| 21 | Window functions 1: OVER, PARTITION BY, ROW_NUMBER, RANK, DENSE_RANK | 65 | R | SQLite window functions |
| 22 | Window functions 2: LAG, LEAD, month over month, year over year | 60 | R | SQLite window functions |
| 23 | Window functions 3: running totals, moving averages, frames | 60 | R | SQLite window functions |
| 24 | Top N per group, removing duplicates, first and last row per customer | 55 | R |  |
| 25 | Time series in SQL: daily to monthly, gaps, comparing periods | 65 | R |  |
| 26 | KPIs and ratios: conversion, average order value, safe division, percent of total | 60 | R |  |
| 27 | Cohorts and retention: first order month, cohort table, funnel steps | 65 | R |  |
| 28 | Cleaning data in SQL: duplicates, trimming, standardising, validation queries | 60 | R |  |
| 29 | Reconcile SQL with Excel: control totals, matching numbers, difference queries | 55 | R |  |
| 30 | Create tables and change data: CREATE, INSERT, UPDATE, DELETE, constraints, transactions | 60 | R | SQLite CREATE TABLE and transactions |
| 31 | Views and temporary tables: reusable queries | 50 | R | SQLite CREATE VIEW |
| 32 | Indexes and performance: EXPLAIN QUERY PLAN, when an index helps | 55 | R | SQLite query planner |
| 33 | Other engines 1: what changes in SQL Server (T-SQL) and Oracle: row limiting, dates, strings, NULL and empty string, quoting; stored procedures only named, not taught | 55 | W (every line cites the vendor page; narration says it was not run) | Microsoft Learn T-SQL; Oracle docs |
| 34 | Other engines 2: what changes in MySQL, PostgreSQL and BigQuery, and the stored procedures / engine-specific features we do not teach | 50 | W (same rule) | MySQL, PostgreSQL, BigQuery docs |
| 35 | Writing queries others can read: style, comments, testing queries, Git for SQL files | 50 | R |  |
| 36 | Capstone 1: brief, invented database, the KPI queries step by step | 70 | R |  |
| 37 | Capstone 2: check queries, report pack, README, release | 65 | R |  |

## Density budget (each line sums to the table minutes; a script under 50 min gets a real extra section, never padding)
Order: hook, map, concept + live, mistakes, company scenario, lab + solution, summary + quiz, next.
1 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
2 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
3 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
4 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
5 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
6 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
7 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
8 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
9 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
10 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
11 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
12 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
13 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
14 (65): hook 2, map 3, concept + live 24, mistakes 9, scenario 8, lab 13, summary + quiz 5, next 1. Sum 65.
15 (65): hook 2, map 3, concept + live 24, mistakes 9, scenario 8, lab 13, summary + quiz 5, next 1. Sum 65.
16 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
17 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
18 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
19 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
20 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
21 (65): hook 2, map 3, concept + live 24, mistakes 9, scenario 8, lab 13, summary + quiz 5, next 1. Sum 65.
22 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
23 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
24 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
25 (65): hook 2, map 3, concept + live 24, mistakes 9, scenario 8, lab 13, summary + quiz 5, next 1. Sum 65.
26 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
27 (65): hook 2, map 3, concept + live 24, mistakes 9, scenario 8, lab 13, summary + quiz 5, next 1. Sum 65.
28 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
29 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
30 (60): hook 2, map 3, concept + live 22, mistakes 9, scenario 7, lab 11, summary + quiz 5, next 1. Sum 60.
31 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
32 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
33 (55): hook 2, map 3, concept + live 20, mistakes 8, scenario 6, lab 10, summary + quiz 5, next 1. Sum 55.
34 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
35 (50): hook 2, map 3, concept + live 18, mistakes 7, scenario 5, lab 9, summary + quiz 5, next 1. Sum 50.
36 (70): hook 2, brief 5, invented database and generator 10, KPI queries step by step 38, mistakes 5, hand-off 8, summary 2. Sum 70.
37 (65): hook 2, check queries 15, report pack 15, README and screenshots 15, release 8, mistakes 5, summary 5. Sum 65.

## Diploma map and hours (plan estimates, each course outline measures its own number)
C1 Excel: 31 videos, 29.9 h (measured from outline v4.5 table, 1795 min). C2 SQL: 37 videos, 35.58 h. C3 Power BI and DAX: about 40 h (estimate, outline not written). C4 Statistics for analysts: about 28 h (estimate). C5 Career and capstone: about 28 h (estimate). Total about 161 h (over 150 h, but only C1 and C2 are measured; the three other numbers are plan estimates and will be replaced by their outlines). Optional Tableau short course is not counted.
The 19 held short SQL packages (about 1 min each) are retired by this course; decision needed from main to confirm they never publish.

## Order and publishing
Diploma order: diploma intro (video 0), Excel C1 intro + 31, SQL C2 intro + 37, then C3-C5. Publishing is strictly in this order after reviewer PASS and the user's listen. Production order inside C2: intro text for the reviewer first, then videos 1, 2, 3 ... one video at a time with the new-diploma standard (research, script text to the reviewer before voicing, one-line opener sent as text before voicing, Canva cover, GitHub folder byte-identical to the package zip).

## Open points for the reviewer
1. SQLite as the lab engine (instead of SQL Server) given SQL Server is named most often in the ads (8 of 38). My reason: free, local, real runs possible here, and standard SQL carries over. Video 33 covers the differences from vendor pages.
2. Whether 37 videos and about 36 h is the right size for SQL (the diploma total needs to stay over 150 h).
3. Resolved: video 33 is split (33 T-SQL and Oracle, 34 the rest).
