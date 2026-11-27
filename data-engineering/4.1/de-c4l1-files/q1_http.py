import threading, urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"<html><body><h1>Hello</h1><p class='price'>25</p></body></html>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass
srv = HTTPServer(("127.0.0.1", 8765), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
r = urllib.request.urlopen("http://127.0.0.1:8765/")
print(r.status, r.headers["Content-Type"])
print(r.read().decode())
srv.shutdown()
