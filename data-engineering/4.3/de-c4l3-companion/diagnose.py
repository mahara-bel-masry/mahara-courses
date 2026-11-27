import requests, time
from bs4 import BeautifulSoup

URL = 'https://quotes.toscrape.com/js/'
t0 = time.perf_counter()
r = requests.get(URL, timeout=20)
dt = time.perf_counter() - t0
print('status:', r.status_code)
if r.status_code != 200:
    print('stop: response error, this is not a JavaScript question at all')
    raise SystemExit(1)
print('raw-bytes:', len(r.content))
print('requests-seconds: %.2f' % dt)
soup = BeautifulSoup(r.text, 'html.parser')
quotes = soup.select('div.quote')
print('quote-divs-in-raw-tree:', len(quotes))
if quotes:
    print('elements already in raw HTML: requests is enough here')
else:
    print('zero matching elements is a diagnostic clue, not proof a browser is required')
    print('data-as-js-variable-in-script:', 'var data' in r.text)
    print('script-tags:', len(soup.find_all('script')))
    print('here the data arrived embedded as JS code; a rendering browser is the general route taught in this lesson')
