#!/usr/bin/env python3
"""حلول منفذة لتمارين الدرس 5. شغل: python3 solutions.py"""
import csv, logging, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# تمرين 1: 30 2 * * * /opt/backup.sh
#   30 دقيقة ، 2 الساعة ، الباقي نجوم: كل يوم 2:30 صباحًا
# تمرين 4: */10 9-16 * * 1-5 /usr/bin/python3 /path/scraper_scheduled.py
#   كل 10 دقايق ، الساعات 9 لحد 16 (يعني آخر إطلاقة 4:50) ، الاتنين للجمعة

def ex2_manual_run():
    """تشغيل يدوي والتحقق من سطور اللوج الأربعة"""
    before = (HERE / "logs" / "scraper.log").read_text().count("\n")
    r = subprocess.run([sys.executable, str(HERE / "scraper_scheduled.py")])
    lines = (HERE / "logs" / "scraper.log").read_text().splitlines()[before:]
    assert r.returncode == 0, r.returncode
    assert len(lines) == 4 and all("INFO" in l for l in lines), lines
    return f"ex2 ok: exit=0 و {len(lines)} سطور INFO"

def ex3_warning_variant():
    """نسخة معدلة: WARNING لو الاقتباسات أقل من 5 (منفذة على الصفحة الحية)"""
    import requests
    from bs4 import BeautifulSoup
    log = logging.getLogger("ex3")
    resp = requests.get("https://quotes.toscrape.com/",
                        headers={"User-Agent": "mahara-course-demo/1.0 (+training)"}, timeout=10)
    quotes = BeautifulSoup(resp.text, "html.parser").select("div.quote")
    if len(quotes) < 5:
        log.warning("quotes dropped to %s", len(quotes))
    return f"ex3 ok: status={resp.status_code} quotes={len(quotes)} (مش أقل من 5 فمفيش WARNING، وده متوقع)"

def ex5_forced_failure():
    """تشغيل النسخة المكسورة والتحقق من الفشل المرئي"""
    r = subprocess.run([sys.executable, str(HERE / "scraper_broken.py")],
                       capture_output=True, text=True)
    log_text = (HERE / "logs" / "scraper.log").read_text()
    assert r.returncode == 1, r.returncode
    assert "ERROR run failed" in log_text
    assert "NameResolutionError" in log_text
    return "ex5 ok: exit=1 و ERROR و NameResolutionError في اللوج"

if __name__ == "__main__":
    print(ex2_manual_run())
    print(ex3_warning_variant())
    print(ex5_forced_failure())
