import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

ORDERS = [{"id": i, "total": i * 10.5} for i in range(1, 8)]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/orders":
            q = parse_qs(url.query)
            page = int(q.get("page", ["1"])[0])
            items = ORDERS[(page - 1) * 3: page * 3]
            self.send(200, {"page": page, "items": items})
        else:
            self.send(404, {"error": "not found"})

    def send(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
