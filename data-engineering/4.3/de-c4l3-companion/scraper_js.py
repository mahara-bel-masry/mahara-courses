import csv, time
from collections import Counter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

START = 'https://quotes.toscrape.com/js/'
MAX_PAGES = 3  # تشغيل تدريبي محدود باختيارنا

opts = Options()
opts.add_argument('--headless=new')

driver = webdriver.Chrome(options=opts)
rows = []
try:
    driver.get(START)
    for page in range(1, MAX_PAGES + 1):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.quote')))
        quotes = driver.find_elements(By.CSS_SELECTOR, 'div.quote')
        print('page %d: %d quotes (%s)' % (page, len(quotes), driver.current_url))
        for q in quotes:
            rows.append((q.find_element(By.CSS_SELECTOR, 'span.text').text,
                         q.find_element(By.CSS_SELECTOR, 'small.author').text,
                         '|'.join(a.text for a in q.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')),
                         driver.current_url))
        if page < MAX_PAGES:
            old_first = quotes[0]
            next_links = driver.find_elements(By.CSS_SELECTOR, 'li.next a')
            if not next_links:
                print('no next link: end of site reached, stopping')
                break
            next_links[0].click()
            WebDriverWait(driver, 10).until(EC.staleness_of(old_first))
            time.sleep(1)  # وقفة تدريبية بين الصفحات، مش استنانة للتحميل
finally:
    driver.quit()

with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['text', 'author', 'tags', 'page_url'])
    w.writerows(rows)
print('rows-written:', len(rows))

# التحقق بإعادة القراءة: قارئ CSV بيفهم الأعمدة والسجلات متعددة الأسطر
with open('quotes.csv', newline='', encoding='utf-8') as f:
    physical_lines = sum(1 for _ in f)
with open('quotes.csv', newline='', encoding='utf-8') as f:
    recs = list(csv.DictReader(f))
print('physical-lines:', physical_lines)
print('logical-records:', len(recs))
print('first-record-author:', recs[0]['author'])
authors = Counter(r['author'] for r in recs)
tags = Counter(t for r in recs for t in r['tags'].split('|'))
print('unique-authors:', len(authors))
print('authors-with-2-quotes:', sorted(a for a, c in authors.items() if c == 2))
print('top-3-tags:', tags.most_common(3))
print('longest-quote-chars:', max(len(r['text']) for r in recs))
print('shortest-quote-chars:', min(len(r['text']) for r in recs))
