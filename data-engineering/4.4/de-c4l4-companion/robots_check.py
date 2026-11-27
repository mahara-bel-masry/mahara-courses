"""قراءة robots.txt وفحص المسارات بـ robotparser من المكتبة القياسية.
الملفات المقروءة هنا نسخ محفوظة من الجلب الحقيقي (fetch-robots.log)."""
import urllib.robotparser as rp

def check(name, path, urls):
    parser = rp.RobotFileParser()
    with open(path, encoding="utf-8") as f:
        parser.parse(f.read().splitlines())
    print(f"=== {name} ===")
    print(f"crawl_delay(*) = {parser.crawl_delay('*')}")
    print(f"sitemaps = {parser.sitemaps}")
    for u in urls:
        print(f"can_fetch('*', {u}) -> {parser.can_fetch('*', u)}")
    print()

check("en.wikipedia.org", "robots-en-wikipedia.txt", [
    "https://en.wikipedia.org/wiki/Python",
    "https://en.wikipedia.org/w/api.php?action=query",
])
check("github.com", "robots-github.txt", [
    "https://github.com/python/cpython",
    "https://github.com/search/advanced",
    "https://github.com/copilot/",
])
print("=== حدود المطابقة الحرفية: قواعد فيها * و$ (RFC 9309 قسم 2.2.3) ===")
gh = rp.RobotFileParser()
gh.parse(open("robots-github.txt", encoding="utf-8").read().splitlines())
for u in ["https://github.com/python/cpython/issues/search",
          "https://github.com/python/cpython/issues/search/open"]:
    print(f"can_fetch('*', {u}) -> {gh.can_fetch('*', u)}  (حسب RFC 9309: False)")
