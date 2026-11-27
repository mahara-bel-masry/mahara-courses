#!/usr/bin/env bash
# تقرير سريع عن لوج سيرفر: توزيع الردود وأعلى العناوين وعدد الأخطاء
# الاستخدام: ./scripts/log_report.sh [مسار_اللوج]
set -euo pipefail

LOG="${1:-logs/server.log}"

if [[ ! -f "$LOG" ]]; then
  echo "خطأ: الملف $LOG مش موجود" >&2
  exit 1
fi

if [[ ! -r "$LOG" ]]; then
  echo "خطأ: الملف $LOG مش قابل للقراية" >&2
  exit 1
fi

echo "=== تقرير اللوج: $LOG ==="
echo "عدد الأسطر: $(wc -l < "$LOG")"
echo
echo "-- توزيع ردود السيرفر --"
cut -d'"' -f3 "$LOG" | cut -d' ' -f2 | sort | uniq -c | sort -nr
echo
echo "-- أعلى خمسة عناوين طلبات --"
cut -d' ' -f1 "$LOG" | sort | uniq -c | sort -nr | head -5
echo
echo "-- عدد أخطاء الخادم 500 --"
# grep بيرجع كود 1 لما ميلاقيش مطابقات، وده عندنا نجاح بعدد صفر مش فشل
# الكود 2 أو أكتر معناه غلطة قراية حقيقية، وساعتها نفشل بصوت عالي
rc=0
count=$(grep -c ' 500 ' "$LOG") || rc=$?
if [[ $rc -gt 1 ]]; then
  echo "خطأ: مش قادر أقرا $LOG" >&2
  exit "$rc"
fi
echo "$count"
