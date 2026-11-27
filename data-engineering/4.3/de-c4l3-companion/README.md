# الدرس 3 من كورس 4: Selenium للصفحات اللي بتحمّل بالجافاسكريبت — الملف المرفق

## المحتوى
- diagnose.py: التشخيص المنفذ في الدرس — requests على quotes.toscrape.com/js/ بيرجع 200 بس 0 عناصر div.quote في الشجرة الخام، والبيانات جوه وسم script كمتغير var data.
- selenium_first.py: أول تشغيل Selenium — متصفح Chrome حقيقي (headless) بيشغل الجافاسكريبت فتظهر 10 بطاقات، مع قياس التوقيت.
- scraper_js.py: السكرابر الكامل المنفذ — بينقر زرار next عبر 3 صفحات (تشغيل تدريبي محدود) ويحفظ 30 اقتباس في quotes.csv ويتحقق بإعادة القراءة والإحصائيات.
- quotes.csv: الملف الناتج من التشغيل (31 سطر: عناوين + 30 اقتباس).
- exercises.md: تمارين الدرس الخمسة.
- solutions.py: حلولها المنفذة (تمرين 5 بيكتب quotes_ex5.csv).

## المتطلبات
pip install requests beautifulsoup4 selenium
ومتصفح Chrome أو Chromium متسطب على الجهاز (Selenium بيدير الـ driver تلقائي).

## التشغيل
python3 diagnose.py
python3 selenium_first.py
python3 scraper_js.py
python3 solutions.py

ملحوظة: السكربتات بتفتح متصفح حقيقي في الخلفية (headless) وبتقفله بـ driver.quit(). الاستنانة بين الصفحات في السكرابر اختيار تدريبي للموقع ده؛ قبل أي موقع تاني راجع robots.txt وشروط الاستخدام (وده موضوع الدرس الرابع).
