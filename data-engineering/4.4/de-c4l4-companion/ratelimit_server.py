"""سيرفر تدريبي محلي (127.0.0.1) بيحدد المعدل:
أكتر من طلبين في نافذة 3 ثواني يرجع 429 مع Retry-After."""
import threading, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

WINDOW = 3.0
LIMIT = 2
hits = []
lock = threading.Lock()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        now = time.monotonic()
        with lock:
            while hits and now - hits[0] > WINDOW:
                hits.pop(0)
            if len(hits) >= LIMIT:
                retry = WINDOW - (now - hits[0])
                self.send_response(429)
                self.send_header("Retry-After", str(int(retry) + 1))
                self.end_headers()
                self.wfile.write(b"too many requests")
            else:
                hits.append(now)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f"quote # {len(hits)}".encode())
    def log_message(self, *a):
        pass

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
