# مرفق الدرس الأول - كورس 4: الويب سكرابينج والأتمتة

الدرس 1: إزاي الويب بيشتغل: HTTP وHTML وCSS selectors

## الملفات

- demo.py - كود الديمو اللي اتنفذ في الفيديو على الهواء، مرتب ومعلق
- exercises.md - خمس تمارين الدرس
- solutions.py - حلول التمارين منفذة

## التشغيل

```
pip install requests beautifulsoup4
python demo.py
python solutions.py
```

الاتنين بيشتغلوا على موقع books.toscrape.com ، موقع مخصص للتدريب على
السكرابينج، فمحتاج نت شغال. لو الموقع وقع مؤقتًا جرب تاني بعد شوية.

## ملاحظات

- كل النتائج اللي في الفيديو من تنفيذ حقيقي على الموقع وقت التسجيل.
  أرقام زي عدد الكتب في الصفحة أو أول سعر ممكن تتغير لو الموقع اتعدل.
- مصيدة الترميز: السيرفر بيبعت content-type: text/html من غير charset ،
  فمكتبة requests بتفترض ISO-8859-1 وعلامة الجنيه تطلع مشوهة (Â£51.77).
  الحل: r.encoding = "utf-8" قبل التحليل، والسعر يرجع سليم (£51.77).
  الصفحة بتعلن UTF-8 في وسم meta.
- عدّ وسوم script: العدّ المباشر للنص الخام بيطلع 9 ، بس العناصر الحقيقية 7.
  الزيادة: وسم جوه تعليق مشروط لمتصفحات IE القديمة، وواحد جوه نص جافاسكريبت
  (سطر document.write الاحتياطي لجيكويري). demo.py بيعد العناصر الحقيقية.

## المصادر الرسمية للمفاهيم العامة في الدرس

- أكواد حالة HTTP والعائلات (2xx و3xx و4xx و5xx):
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
- المرجع الرسمي لمواصفة HTTP (دلالات الأكواد):
  https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes
- طرق الطلب (GET وPOST وHEAD):
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods
- هيدر Retry-After (حد أدنى للانتظار قبل إعادة المحاولة مع 429 و503):
  https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After
- مرجع CSS selectors (الوسم والكلاس والـ id والتداخل والخصائص):
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors
- توثيق requests (الترميز الافتراضي ومتابعة التحويلات تلقائيًا):
  https://requests.readthedocs.io/en/latest/user/quickstart/
- توثيق BeautifulSoup الرسمي:
  https://www.crummy.com/software/BeautifulSoup/bs4/doc/

## ملاحظة عن قرار الاستمرار

القاعدة اللي اتعلمناها: كود 200 لوحده مش كفاية، لازم علامة محتوى متوقعة كمان
(زي وجود وسوم الكتب في صفحتنا)، لأن في مواقع بترجع 200 مع صفحة خطأ شكلها شيك.
ولو الرد 429 أو 500: إعادة محاولة مرات محدودة بفواصل بتطول، ومع وجود هيدر
Retry-After نستنى على الأقل المدة اللي فيه قبل ما نعيد.
