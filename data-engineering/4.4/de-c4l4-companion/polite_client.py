"""عميل مهذب وعميل مستعجل ضد السيرفر التدريبي المحلي."""
import sys, time, urllib.request, urllib.error

BASE = "http://127.0.0.1:8765/quote"

def fetch():
    try:
        with urllib.request.urlopen(BASE, timeout=5) as r:
            return r.status, r.read().decode(), None
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(), e.headers.get("Retry-After")

def impolite(n=5):
    print("--- العميل المستعجل: 5 طلبات فورية ---")
    for i in range(1, n + 1):
        st, body, _ = fetch()
        print(f"طلب {i}: {st} ({body})")

def polite(n=5, gap=1.6, max_attempts=12):
    # ملاحظة مقصودة: بنقرا Retry-After كرقم ثواني بس زي ما السيرفر التدريبي بيبعته.
    # الصيغة التانية المسموحة في المواصفة (تاريخ HTTP كامل) مش مدعومة هنا.
    # وفي الشغل الحقيقي: لو الصد اتكرر لحد الحد الأقصى نقف، منفضلش نحاول بلا نهاية.
    print("--- العميل المهذب: ثابت بين الطلبات + احترام Retry-After ---")
    ok = 0
    i = 1
    while ok < n and i <= max_attempts:
        st, body, retry = fetch()
        if st == 200:
            ok += 1
            print(f"طلب {i}: 200 ({body})")
        else:
            wait = int(retry) if retry else 1
            print(f"طلب {i}: 429 - Retry-After قال استنى {wait} ثانية، بنستنى فعلًا")
            time.sleep(wait)
        i += 1
        time.sleep(gap)
    if ok == n:
        print(f"النتيجة: {ok}/{n} طلب ناجح في {i-1} محاولة، مع {i-1-ok} رفض مؤقت بـ 429 اتعامل معاه صح")
    else:
        print(f"وقفنا بعد {i-1} محاولة (الحد الأقصى {max_attempts}): نجح {ok}/{n} بس، والصد المتكرر معناه قف وراجع الموقع")

if __name__ == "__main__":
    if sys.argv[1] == "impolite":
        impolite()
    else:
        gap = float(sys.argv[2]) if len(sys.argv) > 2 else 1.6
        polite(gap=gap)
