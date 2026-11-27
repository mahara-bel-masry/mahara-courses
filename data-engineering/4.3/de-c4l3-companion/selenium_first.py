import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://quotes.toscrape.com/js/'
opts = Options()
opts.add_argument('--headless=new')

t0 = time.perf_counter()
driver = webdriver.Chrome(options=opts)
try:
    t1 = time.perf_counter()
    driver.get(URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.quote')))
    dt = time.perf_counter() - t1
    quotes = driver.find_elements(By.CSS_SELECTOR, 'div.quote')
    print('selenium-get-and-render-seconds: %.2f' % dt)
    print('quote-divs-after-js:', len(quotes))
    first = quotes[0]
    text = first.find_element(By.CSS_SELECTOR, 'span.text').text
    author = first.find_element(By.CSS_SELECTOR, 'small.author').text
    tags = [a.text for a in first.find_elements(By.CSS_SELECTOR, 'div.tags a.tag')]
    print('first-quote:', text)
    print('first-author:', author)
    print('first-tags:', tags)
    print('quote-div-in-page-source:', '<div class="quote">' in driver.page_source)
    print('page-source-bytes:', len(driver.page_source.encode('utf-8')))
finally:
    driver.quit()
print('total-with-browser-start: %.2f' % (time.perf_counter() - t0))
