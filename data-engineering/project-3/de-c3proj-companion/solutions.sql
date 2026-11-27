-- ============================================
-- الحلول النموذجية المنفذة (راجعها بعد ما تحل بنفسك)
-- كل نتيجة هنا مطابقة للفيديو حرفيًا على نفس store.db
-- ملاحظة عامة: التجميع دايمًا على المعرف الثابت مع الاسم (GROUP BY id, name)
-- مش على الاسم لوحده ، عشان اسمين متشابهين في قاعدة حقيقية ما يندمجوش غلط.
-- وفي الترتيب التنازلي بنكسر التعادل بالمعرف عشان النتيجة تطلع ثابتة كل مرة.
-- ============================================

-- س1: أعلى 5 منتجات بالإيراد
-- الفكرة: الإيراد = مجموع الكمية في سعر البيع المخزن في السطر ، والتجميع على المنتج.
SELECT p.name, SUM(i.qty*i.unit_price) AS revenue FROM order_items i JOIN products p ON p.product_id=i.product_id GROUP BY p.product_id, p.name ORDER BY revenue DESC, p.product_id LIMIT 5;
-- المنفذ: شاشة 24 بوصة 130500 ، سماعة بلوتوث 62400 ، طابعة 25600 ، كيبورد 20300 ، حقيبة لابتوب 17100
-- خمس صفوف بالظبط (LIMIT 5) ، والإيراد هنا بلا تعادل فالترتيب محسوم.

-- س2: أعلى 5 منتجات بالكمية
SELECT p.name, SUM(i.qty) AS units FROM order_items i JOIN products p ON p.product_id=i.product_id GROUP BY p.product_id, p.name ORDER BY units DESC, p.product_id LIMIT 5;
-- المنفذ: سماعة بلوتوث 52 ، ماوس 36 ، شاشة 24 بوصة 29 ، كيبورد 29 ، حقيبة لابتوب 19
-- تعادل صريح: الشاشة والكيبورد الاتنين 29 وحدة (تالتة معًا) ، وكسر التعادل بالمعرف الثابت
-- (product_id) عشان الترتيب يفضل ثابت لو شغلت الاستعلام تاني.
-- ملاحظة: ترتيب الكمية مختلف عن ترتيب الإيراد (الشاشة غالية بس وحداتها أقل) ، وده فرق سؤال الأعلى مبيعًا عن الأعلى إيراد.

-- س3: الإيراد لكل شهر
SELECT substr(o.order_date,1,7) AS month, SUM(i.qty*i.unit_price) AS revenue FROM orders o JOIN order_items i ON i.order_id=o.order_id GROUP BY month ORDER BY month;
-- المنفذ: 2025-10 هو 52350 ، 2025-11 هو 123250 ، 2025-12 هو 94400
-- تحقق استمرارية: إيراد أكتوبر 52350 هو نفس إجمالي الدرس 10 (القاعدة فيها أكتوبر الدرسين حرفيًا).

-- س4: متوسط قيمة الأوردر لكل شهر
SELECT substr(o.order_date,1,7) AS month, ROUND(1.0*SUM(i.qty*i.unit_price)/COUNT(DISTINCT o.order_id),2) AS avg_order FROM orders o JOIN order_items i ON i.order_id=o.order_id GROUP BY month ORDER BY month;
-- المنفذ: 2617.5 ، 3975.81 ، 3776.0
-- ليه COUNT(DISTINCT o.order_id): الدمج مع الأسطر بيكرر الأوردر بعدد أسطره ، فلو قسمت على عدد الصفوف المتكررة يطلع متوسط غلط (نفس مصيدة درس التضاعف).

-- س5: العملاء النشطين لكل شهر
SELECT substr(order_date,1,7) AS month, COUNT(DISTINCT customer_id) AS active_customers FROM orders GROUP BY month ORDER BY month;
-- المنفذ: 8 ، 12 ، 10 (نوفمبر شاف العملاء الجدد 10-13 ، وديسمبر دخله 14-15 وغاب عنه خاملين)
-- نشط مش مسجل: عندنا 15 عميل مسجل ، 14 بس منهم اشتروا فعلًا في الفترة ، وزياد مراد مسجل ولم يشترِ فلا يدخل في العد.

-- س6: أعلى 3 عملاء بالإنفاق
SELECT c.name, SUM(i.qty*i.unit_price) AS total FROM customers c JOIN orders o ON o.customer_id=c.customer_id JOIN order_items i ON i.order_id=o.order_id GROUP BY c.customer_id, c.name ORDER BY total DESC, c.customer_id LIMIT 3;
-- المنفذ: دينا رامي 39350 ، طارق حسن 35300 ، أحمد سمير 28600

-- س7: اشتروا مرة واحدة بس
SELECT c.name FROM customers c JOIN orders o ON o.customer_id=c.customer_id GROUP BY c.customer_id, c.name HAVING COUNT(*)=1 ORDER BY c.customer_id;
-- المنفذ: حسن علي (أوردر واحد يوم 2025-11-15)

-- س8: الخاملون (تعريف محدد: آخر أوردر قبل أكتر من 30 يوم من أحدث تاريخ في البيانات)
WITH last_date AS (SELECT MAX(order_date) AS d FROM orders)
SELECT c.name, MAX(o.order_date) AS last_order FROM customers c JOIN orders o ON o.customer_id=c.customer_id, last_date
GROUP BY c.customer_id, c.name HAVING julianday(last_date.d)-julianday(MAX(o.order_date))>30 ORDER BY last_order, c.customer_id;
-- المنفذ: حسن علي 2025-11-15 ، هشام زكي 2025-11-22 ، عمر فاروق 2025-11-26
-- ملاحظة: تعريف الخمول قرار عمل مش حقيقة مطلقة: 30 يوم اختيار المشروع هنا ، غيّره وشوف النتيجة بتتغير.
-- نور إيهاب آخر أوردر 2025-11-27: بالظبط 30 يوم من النهاية فمش داخلة (الشرط أكبر تمامًا).

-- س9: شهر أول شراء لكل عميل
SELECT c.name, substr(MIN(o.order_date),1,7) AS cohort_month FROM customers c JOIN orders o ON o.customer_id=c.customer_id GROUP BY c.customer_id, c.name ORDER BY cohort_month, c.customer_id;
-- المنفذ: الثمانية الأصليين 2025-10 ، وحسن وعمر وليلى وياسمين 2025-11 ، ورنا ومحمود 2025-12
-- زياد مراد غائب لأنه لم يشتر أبدًا: الـ JOIN بيستبعده ، وده مقصود في تعريف الـ cohort (لازم شراء أول موجود).

-- س10: حجم كل cohort
WITH first_orders AS (SELECT customer_id, substr(MIN(order_date),1,7) AS cohort FROM orders GROUP BY customer_id)
SELECT cohort, COUNT(*) AS customers FROM first_orders GROUP BY cohort ORDER BY cohort;
-- المنفذ: 2025-10 فيه 8 ، 2025-11 فيه 4 ، 2025-12 فيه 2

-- س11: retention مبسّط مع قطع ملاحظة صريح
-- التعريف: عميل "رجع" لو عنده أوردر في شهر لاحق لشهر cohort الخاص به (شهر أكبر تمامًا).
-- شراء تاني جوه نفس الشهر لا يعد رجوعًا بهذا التعريف.
-- قطع الملاحظة: البيانات بتنتهي 2025-12-27 ، فالشهور اللاحقة الظاهرة غير متساوية:
--   cohort أكتوبر عنده شهران لاحقان ظاهران (نوفمبر كامل + ديسمبر حتى 27) ،
--   نوفمبر عنده شهر واحد جزئي (ديسمبر حتى 27) ،
--   ديسمبر عنده صفر شهور لاحقة في البيانات.
-- عشان كده 0 في المية لديسمبر معناها "مفيش شهر لاحق في البيانات يتحسب فيه رجوع" ، مش فشل retention.
WITH first_orders AS (SELECT customer_id, substr(MIN(order_date),1,7) AS cohort FROM orders GROUP BY customer_id),
returned AS (SELECT DISTINCT f.cohort, f.customer_id FROM first_orders f JOIN orders o ON o.customer_id=f.customer_id AND substr(o.order_date,1,7)>f.cohort)
SELECT f.cohort, COUNT(DISTINCT f.customer_id) AS cohort_size, COUNT(DISTINCT r.customer_id) AS returned,
ROUND(100.0*COUNT(DISTINCT r.customer_id)/COUNT(DISTINCT f.customer_id),1) AS pct_returned
FROM first_orders f LEFT JOIN returned r ON r.customer_id=f.customer_id GROUP BY f.cohort ORDER BY f.cohort;
-- المنفذ: أكتوبر 8 رجع منهم 8 بنسبة 100.0 ، نوفمبر 4 رجع 2 بنسبة 50.0 (ليلى وياسمين) ، ديسمبر 2 رجع 0 بنسبة 0.0 (مفيش شهر لاحق في البيانات)

-- س12: الإيراد لكل cohort
WITH first_orders AS (SELECT customer_id, substr(MIN(order_date),1,7) AS cohort FROM orders GROUP BY customer_id)
SELECT f.cohort, SUM(i.qty*i.unit_price) AS revenue FROM first_orders f JOIN orders o ON o.customer_id=f.customer_id JOIN order_items i ON i.order_id=o.order_id GROUP BY f.cohort ORDER BY f.cohort;
-- المنفذ: 216150 ، 41550 ، 12300
-- ملاحظة تفسير: الفرق مزيج من حجم الـ cohort وعمره في البيانات ، مش "جودة" العملاء.

-- س13: أعلى 3 أيام إيراد
SELECT o.order_date, SUM(i.qty*i.unit_price) AS revenue FROM orders o JOIN order_items i ON i.order_id=o.order_id GROUP BY o.order_date ORDER BY revenue DESC, o.order_date LIMIT 3;
-- المنفذ: 2025-12-09 هو 13100 ، 2025-10-23 هو 12000 ، 2025-11-12 هو 11750

-- س14: اتباعت في أكتوبر أو نوفمبر وما اتبعتش في ديسمبر
-- المقارنة على المعرف مع الاسم مش الاسم لوحده ، عشان منتجين بنفس الاسم ما يلغوش بعض غلط في EXCEPT.
SELECT DISTINCT p.product_id, p.name FROM products p JOIN order_items i ON i.product_id=p.product_id JOIN orders o ON o.order_id=i.order_id
WHERE substr(o.order_date,1,7) IN ('2025-10','2025-11')
EXCEPT
SELECT p.product_id, p.name FROM products p JOIN order_items i ON i.product_id=p.product_id JOIN orders o ON o.order_id=i.order_id
WHERE substr(o.order_date,1,7)='2025-12';
-- المنفذ: كابل USB-C
-- الطريقة بـ EXCEPT من درس المجموعات: المباع في الفترة الأولى ناقص المباع في ديسمبر.
-- النتيجة حقيقة مرصودة في عينة البيانات دي: الكابل فعلًا ما اتباعش في ديسمبر داخل القاعدة.
-- أما سبب الغياب ففرضية مش حقيقة: ممكن مخزون خلص أو طلب موسمي ، وديسمبر جزئي أصلًا (البيانات بتقف يوم 27) ،
-- فالقرار محتاج تحقق من المخزون والتوقيت خارج الاستعلام.

-- س15: متوسط عدد الأصناف المختلفة في الأوردر
SELECT ROUND(AVG(n),2) AS avg_items_per_order FROM (SELECT order_id, COUNT(DISTINCT product_id) AS n FROM order_items GROUP BY order_id);
-- المنفذ: 1.72
-- التجميع جوه استعلام داخلي أولًا (عدد الأصناف المميزة لكل أوردر) ، وبعدين المتوسط على مستوى الأوردرات مش على مستوى الأسطر.
-- الاسكيما هنا بيمنع تكرار نفس المنتج مرتين في نفس الأوردر بالمفتاح المركب PRIMARY KEY(order_id,product_id) ،
-- فعد السطور COUNT(*) كان هيطلع نفس الرقم ، لكن COUNT(DISTINCT product_id) أضمن لأنه يفضل صح حتى لو القيد اتغير.
