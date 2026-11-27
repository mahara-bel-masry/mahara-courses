# تمارين الدرس 4: القوانين والأخلاق

الملفات اللي هتحتاجها موجودة في المرفق: robots-en-wikipedia.txt وrobots-wikipedia.txt (نسختان محفوظتان من مضيفي en.wikipedia.org وwww.wikipedia.org، طبق الأصل من بعض وقت التسجيل) وrobots-github.txt وratelimit_server.py وrobots_check.py وpolite_client.py.

## تمرين 1
اطبع من النسختين robots-en-wikipedia.txt وrobots-github.txt عدد سطور Disallow في كل موقع.

## تمرين 2
بـ robotparser على نسخة en.wikipedia.org (نفس مضيف الروابط)، افحص المسارات التلاتة دول واطبع مسموح ولا ممنوع:
/wiki/Arabic و /w/api.php?action=parse و /w/index.php

## تمرين 3
استخرج من نسخة ويكيبيديا أسماء البوتات المحظورة تمامًا (اللي تحت User-agent مسمى مع Disallow: /) واطبع عددها.

## تمرين 4
شغل السيرفر التدريبي (python3 ratelimit_server.py) واكتب عميل بفاصل 0.3 ثانية بين الطلبات يستخدم backoff تصاعدي (1، 2، 4 ثواني بحد أقصى 8) لما يقابل 429، بس لو الرد فيه Retry-After يحترمه بدل الـ backoff. الهدف 5 طلبات ناجحة.

## تمرين 5
اكتب دالة fetch_polite(url, parser, ua, gap) بتجمع كل اللي اتعلمناه: ترفض قبل الإرسال لو can_fetch رجع False، تبعت User-Agent مخصص، وتستنى gap بعد كل طلب. جربها على السيرفر المحلي مع parser فيه Disallow: /admin.

الحلول المنفذة في solutions.py (شغل السيرفر التدريبي الأول عشان تمرين 4 و5).
