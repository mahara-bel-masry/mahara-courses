"""حلول منفذة لتمارين الدرس 4: القوانين والأخلاق.
تعتمد على النسخ المحفوظة robots-wikipedia.txt وrobots-github.txt
والسيرفر التدريبي ratelimit_server.py (شغال على 127.0.0.1:8765)."""
import time, urllib.request, urllib.error, urllib.robotparser as rp

print("== تمرين 1: عدد سطور Disallow ==")
for name in ["robots-en-wikipedia.txt", "robots-github.txt"]:
    with open(name, encoding="utf-8") as f:
        n = sum(1 for ln in f if ln.strip().lower().startswith("disallow:"))
    print(f"{name}: {n} سطر Disallow")

print()
print("== تمرين 2: can_fetch على ويكيبيديا ==")
p = rp.RobotFileParser()
p.parse(open("robots-en-wikipedia.txt", encoding="utf-8").read().splitlines())
for u in ["https://en.wikipedia.org/wiki/Arabic",
          "https://en.wikipedia.org/w/api.php?action=parse",
          "https://en.wikipedia.org/w/index.php"]:
    print(f"can_fetch('*', {u}) -> {p.can_fetch('*', u)}")

print()
print("== تمرين 3: البوتات المحظورة تمامًا في ويكيبيديا ==")
agents, blocked = [], []
for ln in open("robots-wikipedia.txt", encoding="utf-8"):
    ln = ln.strip()
    if ln.lower().startswith("user-agent:"):
        agents.append(ln.split(":", 1)[1].strip())
    elif ln.lower() == "disallow: /":
        for a in agents:
            if a != "*" and not a.startswith("#"):
                blocked.append(a)
        agents = []
    elif ln and not ln.startswith("#") and ":" in ln:
        agents = []
print("المحظورون تمامًا:", blocked)
print("عددهم:", len(blocked))

print()
print("== تمرين 4: backoff تصاعدي مع احترام Retry-After ==")
BASE = "http://127.0.0.1:8765/quote"

def fetch():
    req = urllib.request.Request(BASE, headers={"User-Agent": "ex4-backoff/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, None
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Retry-After")

backoff, ok, tries = 1, 0, 0
MAX_TRIES = 12  # حد أقصى: الصد المتكرر معناه قف، مش محاولات بلا نهاية
while ok < 5 and tries < MAX_TRIES:
    tries += 1
    st, retry = fetch()
    if st == 200:
        ok += 1
        backoff = 1
        print(f"محاولة {tries}: 200 (ناجح {ok}/5)")
        time.sleep(0.3)
    else:
        wait = int(retry) if retry else backoff
        print(f"محاولة {tries}: 429 - استنانة {wait} ثانية (Retry-After={retry})")
        time.sleep(wait)
        backoff = min(backoff * 2, 8)
if ok == 5:
    print(f"النتيجة: 5/5 في {tries} محاولة")
else:
    print(f"وقفنا عند الحد الأقصى {MAX_TRIES} محاولة: نجح {ok}/5")

print()
print("== تمرين 5: fetch_polite متكاملة ==")
def fetch_polite(url, parser, ua="mahara-course-demo/1.0 (training)", gap=1.0):
    if not parser.can_fetch("*", url):
        print(f"مرفوض قبل الإرسال: robots.txt بيمنع {url}")
        return None
    # Retry-After هنا بيتقرا كرقم ثواني بس؛ صيغة تاريخ HTTP مش مدعومة في التمرين ده.
    # ووسيلة التواصل في الـ UA مثال رمزي: حط بريدك أو رابط مشروعك الحقيقي.
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=5) as r:
                body = r.read().decode()
                print(f"200 بعد فحص robots: {body}")
                time.sleep(gap)
                return body
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = int(e.headers.get("Retry-After") or 1)
                print(f"429: بنستنى {wait} ثانية زي ما Retry-After قال")
                time.sleep(wait)
            else:
                raise
    print("فشل بعد 3 محاولات")
    return None

time.sleep(3.5)  # ندي نافذة السيرفر التدريبي وقتها تفضى بعد تمرين 4
local_parser = rp.RobotFileParser()
local_parser.parse(["User-agent: *", "Disallow: /admin"])
fetch_polite("http://127.0.0.1:8765/quote", local_parser)
fetch_polite("http://127.0.0.1:8765/admin", local_parser)
