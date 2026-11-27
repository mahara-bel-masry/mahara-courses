import threading, requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup
PAGE = b"""<html><body>
<div class='item'><h2>Pen</h2><span class='price'>25</span></div>
<div class='item'><h2>Book</h2><span class='price'>90</span></div>
</body></html>"""
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(PAGE)
    def log_message(self, *a): pass
srv = HTTPServer(("127.0.0.1", 8766), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
r = requests.get("http://127.0.0.1:8766/")
soup = BeautifulSoup(r.text, "html.parser")
rows = [(i.h2.text, int(i.select_one(".price").text))
        for i in soup.select(".item")]
print(r.status_code)
print(rows)
print(sum(p for _, p in rows))
srv.shutdown()
