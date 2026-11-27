# تمارين الدرس 1 — سطر أوامر لينكس (بحلولها)
شغل كل التمارين جوه مجلد demo المرفق. الحلول منفذة فعلًا ونتايجها مكتوبة.

## تمرين 1: عد ردود "صفحة مش موجودة" في اللوج
الحل: `grep -c " 404 " logs/server.log`
الناتج المنفذ: 61

## تمرين 2: أكتر تلات مسارات طلبًا في اللوج كله
الحل: `cut -d'"' -f2 logs/server.log | cut -d' ' -f2 | sort | uniq -c | sort -nr | head -3`
الناتج المنفذ:
     54 /favicon.ico
     52 /api/books
     47 /static/style.css

## تمرين 3: عدد سجلات كل منتج من غير صف العناوين
الحل: `cut -d, -f3 data/sales.csv | grep -v product | sort | uniq -c | sort -nr`
الناتج المنفذ:
     43 course
     39 subscription
     38 book

## تمرين 4: كل الطلبات اللي من عنوان بيبدأ بـ 198 واحفظها في ملف
الحل: `grep "^198" logs/server.log > backup/requests-198.txt && wc -l backup/requests-198.txt`
الناتج المنفذ: 7 backup/requests-198.txt

## تمرين 5: أعلى خمس مبيعات قيمة
الحل: `tail -n +2 data/sales.csv | sort -t, -k4 -nr | head -5`
الناتج المنفذ:
2026-11-01,cairo,book,1992
2026-11-11,alex,course,1990
2026-11-07,alex,subscription,1975
2026-11-08,alex,course,1962
2026-11-08,fayoum,course,1955
ملحوظة: tail -n +2 بيتخطى صف العناوين، وسورت بشرطة تي بتحدد الفاصلة فاصل وبشرطة كيه العمود الرابع.
