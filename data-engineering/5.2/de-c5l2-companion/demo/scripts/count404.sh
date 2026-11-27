#!/usr/bin/env bash
# تمرين 1: عد صفحات 404 في لوج
# الاستخدام: ./scripts/count404.sh [مسار_اللوج]
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

echo "عدد صفحات 404 في $LOG:"
# كود 1 من grep معناه مفيش مطابقات، يعني صفر مش فشل
rc=0
count=$(grep -c ' 404 ' "$LOG") || rc=$?
if [[ $rc -gt 1 ]]; then
  echo "خطأ: مش قادر أقرا $LOG" >&2
  exit "$rc"
fi
echo "$count"
