#!/usr/bin/env bash
# تمرين 4: عدد سطور كل ملف في مجلد
# الاستخدام: ./scripts/dir_lines.sh [مسار_المجلد]
set -euo pipefail

DIR="${1:-logs}"

if [[ ! -d "$DIR" ]]; then
  echo "خطأ: المجلد $DIR مش موجود" >&2
  exit 1
fi

if [[ ! -r "$DIR" ]]; then
  echo "خطأ: المجلد $DIR مش قابل للقراية" >&2
  exit 1
fi

for f in "$DIR"/*; do
  if [[ -f "$f" ]]; then
    echo "$f: $(wc -l < "$f") سطر"
  fi
done
