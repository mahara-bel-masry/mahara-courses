# تمارين الدرس 2 - بحلولها المنفذة فعلًا

كل الحلول دي اتنفذت على نفس حاوية التسجيل، والنتايج منسوخة من التنفيذ الحقيقي (نصه الكامل في exercises-session.txt). أرقام العمليات PID هتختلف عندك طبيعي. ملحوظة: في الطرفية التفاعلية بتشوف كود خروج آخر أمر بـ `echo $?`، وفي نص التسجيل هتلاقيه متسجل بمتغير RC لأن سكربت التسجيل بيحتفظ بكود الخروج فيه، القيمة واحدة.

## تمرين 1: سكربت عد الصفحات المفقودة
اكتب سكربت `scripts/count404.sh` ياخد مسار لوج كوسيط (أو الافتراضي logs/server.log)، يتحقق إن الملف موجود، ويطبع عدد ردود 404 فيه.

الحل: السكربت مرفق في `demo/scripts/count404.sh`. التنفيذ:
```
$ bash scripts/count404.sh
عدد صفحات 404 في logs/server.log:
61

$ chmod +x scripts/count404.sh

$ ./scripts/count404.sh
عدد صفحات 404 في logs/server.log:
61
```
لاحظ: اشتغل بباش من غير صلاحية تنفيذ، وبعد chmod +x اشتغل مباشرة. والسكربت بيتعامل صراحة مع حالة مفيش ولا صفحة 404 (grep بيرجع كود واحد): بيطبع صفر ويكمل بنجاح، وجربناها على لوج من غير 404 وطلع صفر وكود خروج صفر، مسجل في exercises-session.txt.

## تمرين 2: عملية خلفية وإيقاف مهذب
شغل `sleep 120` في الخلفية، تأكد إنه موجود، أوقفه بالطريقة المهذبة، وتأكد إنه اختفى.

التنفيذ الحقيقي:
```
$ sleep 120 & SP=$!; echo "background pid: $SP"
background pid: 1648

$ pgrep -a sleep
1648 sleep 120

$ kill 1648

$ pgrep -a sleep

$ echo "pgrep exit code: $RC"
pgrep exit code: 1
```
kill لوحده بعت TERM، والعملية استجابت وقفلت، وpgrep بعدها رجع بكود واحد يعني مفيش عملية بالاسم ده.

## تمرين 3: صلاحيات ملف الأسرار
خلي notes.txt للمالك بس (600)، تأكد بطريقتين، ورجعه 644.

التنفيذ الحقيقي:
```
$ chmod 600 notes.txt

$ stat -c %a,%n notes.txt
600,notes.txt

$ ls -l notes.txt
-rw------- 1 sandbox sandbox 169 Nov 25 22:45 notes.txt

$ chmod 644 notes.txt

$ stat -c %a,%n notes.txt
644,notes.txt
```

## تمرين 4: سكربت عد سطور مجلد
اكتب سكربت `scripts/dir_lines.sh` ياخد مجلد كوسيط (أو logs افتراضيًا)، يتحقق إنه موجود، ويطبع عدد سطور كل ملف فيه.

الحل: مرفق في `demo/scripts/dir_lines.sh`. التنفيذ:
```
$ ./scripts/dir_lines.sh
logs/server.log: 500 سطر

$ ./scripts/dir_lines.sh data
data/sales.csv: 121 سطر

$ ./scripts/dir_lines.sh notadir
خطأ: المجلد notadir مش موجود

$ echo "exit code: $RC"
exit code: 1
```

## تمرين 5: شوف عملية الشيل بتاعتك
اطبع رقم عملية الشيل الحالية، واعرضها بـ ps بأعمدة رقم العملية والأمر بس.

التنفيذ الحقيقي:
```
$ echo "my shell pid: $$"
my shell pid: 1637

$ ps -o pid,cmd -p 1637
   PID CMD
  1637 bash run/exercises.sh
```
`$$` متغير خاص فيه رقم عملية الشيل الحالية.
