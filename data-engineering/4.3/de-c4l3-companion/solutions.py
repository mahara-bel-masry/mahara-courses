# حلول تمارين الدرس 3 من كورس 4 — كلها منفذة على quotes.toscrape.com
import time
from collections import Counter

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_driver():
    opts = Options()
    opts.add_argument('--headless=new')
    return webdriver.Chrome(options=opts)


def wait_quotes(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.quote')))


def ex1():
    print('--- ex1 ---')
    for url in ['https://quotes.toscrape.com/', 'https://quotes.toscrape.com/js/']:
        r = requests.get(url, timeout=20)
        if r.status_code != 200:
            print('%s -> status %s: response error, not a JavaScript question' % (url, r.status_code))
            continue
        soup = BeautifulSoup(r.text, 'html.parser')
        n = len(soup.select('div.quote'))
        if n:
            print('%s -> 200 and %d div.quote in raw: requests kafaya' % (url, n))
        else:
            print('%s -> 200 but 0 div.quote in raw: clue not proof; rendering route taught here' % url)


def ex2():
    print('--- ex2 ---')
    d = make_driver()
    try:
        d.get('https://quotes.toscrape.com/js/')
        wait_quotes(d)
        authors = [q.find_element(By.CSS_SELECTOR, 'small.author').text
                   for q in d.find_elements(By.CSS_SELECTOR, 'div.quote')]
        for a in authors:
            print(a)
    finally:
        d.quit()


def ex3():
    print('--- ex3 ---')
    r = requests.get('https://quotes.toscrape.com/', timeout=20)
    if r.status_code != 200:
        print('status %s: response error, selectors skipped' % r.status_code)
        return
    soup = BeautifulSoup(r.text, 'html.parser')
    tags = [a.text.strip() for a in soup.select('.tags-box a.tag')]
    print('top-tags-count:', len(tags))
    print(tags)
    print('requests kfaya hena 2l2aht: el elements mawgoda fel raw tree; Selenium at2al men gher da3i')


def ex4():
    print('--- ex4 ---')
    d = make_driver()
    try:
        d.get('https://quotes.toscrape.com/js/page/2/')
        wait_quotes(d)
        tags = [a.text for q in d.find_elements(By.CSS_SELECTOR, 'div.quote')
                for a in q.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')]
        print('total-tags-on-page2:', len(tags))
        top = Counter(tags).most_common(3)
        print('most-common:', top)
    finally:
        d.quit()


def ex5():
    print('--- ex5 ---')
    import csv
    d = make_driver()
    rows = []
    try:
        d.get('https://quotes.toscrape.com/js/')
        for page in range(1, 5):
            wait_quotes(d)
            quotes = d.find_elements(By.CSS_SELECTOR, 'div.quote')
            for q in quotes:
                rows.append((q.find_element(By.CSS_SELECTOR, 'span.text').text,
                             q.find_element(By.CSS_SELECTOR, 'small.author').text,
                             '|'.join(a.text for a in q.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')),
                             d.current_url))
            if page < 4:
                old_first = quotes[0]
                next_links = d.find_elements(By.CSS_SELECTOR, 'li.next a')
                if not next_links:
                    print('no next link: end of site reached, stopping')
                    break
                next_links[0].click()
                WebDriverWait(d, 10).until(EC.staleness_of(old_first))
                time.sleep(1)
    finally:
        d.quit()
    with open('quotes_ex5.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['text', 'author', 'tags', 'page_url'])
        w.writerows(rows)
    with open('quotes_ex5.csv', newline='', encoding='utf-8') as f:
        physical = sum(1 for _ in f)
    with open('quotes_ex5.csv', newline='', encoding='utf-8') as f:
        recs = list(csv.DictReader(f))
    print('physical-lines:', physical)
    print('logical-records:', len(recs))
    print('unique-authors:', len({r['author'] for r in recs}))


if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
