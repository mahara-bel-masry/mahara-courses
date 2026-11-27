-- استعلامات كورس 3 على البيانات اللي سحبناها فعلا
-- 1) عدد التشغيلات وعدد الاقتباسات المخزنة
SELECT COUNT(*) AS runs_count FROM runs;
SELECT COUNT(*) AS quotes_count FROM quotes;

-- 2) كل تشغيلة: امتى ولقت كام وجديد كام
SELECT run_id, run_at_utc, status, quotes_found, quotes_new
FROM runs ORDER BY run_id;

-- 3) join: الاقتباسات مع وقت التشغيلة اللي جابتها
SELECT q.quote_id, r.run_at_utc, q.author, substr(q.text, 1, 40) AS quote_start
FROM quotes q JOIN runs r ON r.run_id = q.run_id
ORDER BY q.quote_id LIMIT 5;

-- 4) أكثر الكتاب ظهورا في اللي سحبناه
SELECT author, COUNT(*) AS n
FROM quotes GROUP BY author ORDER BY n DESC, author LIMIT 3;

-- 5) تجميع باليوم (بتوقيت UTC المخزن)
SELECT date(run_at_utc) AS day, COUNT(*) AS runs
FROM runs GROUP BY day ORDER BY day;
