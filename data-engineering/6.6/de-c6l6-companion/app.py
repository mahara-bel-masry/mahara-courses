import socket, csv, time, sys

def connect(host, port, tries=5):
    for i in range(1, tries + 1):
        try:
            return socket.create_connection((host, port), timeout=3)
        except OSError:
            print(f"db مش جاهزة لسه (محاولة {i})")
            time.sleep(2)
    sys.exit("مقدرناش نوصل للـ db")

class Redis:
    def __init__(self, host, port):
        self.sock = connect(host, port)
        self.f = self.sock.makefile("rb")
    def call(self, *args):
        out = f"*{len(args)}\r\n"
        for a in args:
            b = str(a).encode()
            out += f"${len(b)}\r\n" + b.decode() + "\r\n"
        self.sock.sendall(out.encode())
        return self.read()
    def read(self):
        line = self.f.readline().decode().strip()
        t, rest = line[0], line[1:]
        if t == "+": return rest
        if t == ":": return int(rest)
        if t == "$":
            n = int(rest)
            if n == -1: return None
            data = self.f.read(n).decode()
            self.f.read(2)
            return data
        raise RuntimeError("رد غير متوقع: " + line)

r = Redis("db", 6379)
print("الاتصال بالـ db:", r.call("PING"))

seen = set()
orders = []
with open("/app/sales.csv") as fh:
    for row in csv.DictReader(fh):
        if row["order_id"] in seen:
            continue
        seen.add(row["order_id"])
        if row["status"] == "confirmed":
            orders.append(row)

totals = {}
for o in orders:
    totals[o["customer"]] = totals.get(o["customer"], 0) + float(o["amount"])
top = max(totals, key=totals.get)

run = r.call("INCR", "report:runs")
r.call("SET", "report:top", f"{top}={totals[top]:.0f}")
print(f"أوردرات مؤكدة بعد إزالة التكرار: {len(orders)}")
print(f"أعلى عميل: {top} ({totals[top]:.0f})")
print(f"رقم التشغيلة دي: {run}")
print("المخزن في الـ db:", r.call("GET", "report:top"))
