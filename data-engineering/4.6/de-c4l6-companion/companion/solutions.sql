-- حلول تمارين الدرس 6 (منفذة على نسخة من quotes.db وقت التسجيل)

-- 1) اقتباسات Albert Einstein
SELECT quote_id, author, substr(text, 1, 50) AS quote_start
FROM quotes WHERE author = 'Albert Einstein' ORDER BY quote_id;

-- 2) كتاب لهم أكتر من اقتباس
SELECT author, COUNT(*) AS n
FROM quotes GROUP BY author HAVING COUNT(*) > 1 ORDER BY n DESC;

-- 3) التشغيلات الناجحة ومجموع الجديد
SELECT COUNT(*) AS ok_runs, SUM(quotes_new) AS total_new
FROM runs WHERE status = 'ok';

-- 4) أطول وأقصر اقتباس بالحروف
SELECT author, LENGTH(text) AS chars FROM quotes ORDER BY chars DESC LIMIT 1;
SELECT author, LENGTH(text) AS chars FROM quotes ORDER BY chars ASC LIMIT 1;

-- 5) تلميح الحل: أضف العمود في SCHEMA جوه السكربت:
--    text_len INTEGER NOT NULL
--    وبعدين في executemany خزن (run_id, t, a, len(t))
--    وجرب على نسخة: cp data/quotes.db /tmp/test.db
