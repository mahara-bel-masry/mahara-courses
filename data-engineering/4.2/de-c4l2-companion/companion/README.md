# مرفق الدرس التاني: أول سكرابر بـrequests وBeautifulSoup

كورس 4 - الويب سكرابينج والأتمتة - قناة مهارة بالمصري

## المحتوى

- `walkthrough.py` - حل تمارين الدرس الأول مشروح ومنفذ: كل صفحة بتتفحص
  بفحص مزدوج (كود 200 وعلامة محتوى متوقعة) قبل التحليل ، وأي رفض أو نقص
  بيوقف السكربت برسالة واضحة.
- `scraper.py` - السكرابر الكامل بتاع الدرس: يلف على أول 3 صفحات من
  books.toscrape.com ، يجمع العنوان والسعر كرقم والرابط الكامل لكل كتاب
  (60 كتاب) ، ويحفظهم في `books.csv` ، مع استنانة ثانية بين كل طلب والتاني.
- `books.csv` - ملف النتائج الفعلي من تنفيذ السكرابر وقت التسجيل:
  60 كتاب مع سطر العناوين.
- `exercises.md` - أربع تمارين على نفس الموقع مبنية على كود الدرس.
- `solutions.py` - حلول التمارين الأربعة ، منفذة فعليًا على الموقع.

## التشغيل

```
pip install requests beautifulsoup4
python scraper.py
python solutions.py
```

السكربتات بتبعت طلبات حقيقية للموقع ، فالنتائج ممكن تختلف بسيطًا لو الموقع اتغير ،
والاستنانة المهذبة جزء من الكود ، متشيلهاش.

## مصادر الدرس

- https://requests.readthedocs.io/en/latest/user/quickstart/
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors
- https://docs.python.org/3/library/csv.html
- https://docs.python.org/3/library/urllib.parse.html

موقع التدريب: https://books.toscrape.com/ (موقع معمول أصلًا للتدريب على السكرابينج)

كل الأرقام في الدرس والملفات نتائج تنفيذ حقيقي على الموقع وقت التسجيل.
