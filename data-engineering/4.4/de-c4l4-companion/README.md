# الدرس 4: القوانين والأخلاق — الملف المرفق

- robots-en-wikipedia.txt و robots-wikipedia.txt و robots-github.txt: نسخ محفوظة من الجلب الحقيقي وقت التسجيل (طلبات مفردة متباعدة بـ User-Agent معرّف). نسختا ويكيبيديا من مضيفين مختلفين ومتطابقتان بايت ببايت.
- robots_check.py: فحص robots.txt بـ urllib.robotparser على النسخ المحفوظة.
- ratelimit_server.py: سيرفر تدريبي محلي (127.0.0.1:8765) بحد طلبين كل 3 ثواني ويرجع 429 مع Retry-After.
- polite_client.py: عميل مستعجل وعميل مهذب يحترم Retry-After (python3 polite_client.py impolite أو polite [gap]).
- solutions.py: حلول التمارين الخمسة منفذة. شغل السيرفر التدريبي الأول في طرفية لوحده، وبعدين python3 solutions.py.
- exercises.md: نص التمارين.

كل الأرقام في الدرس نتائج تنفيذ فعلي وقت التسجيل. اللي في الدرس مش استشارة قانونية.
