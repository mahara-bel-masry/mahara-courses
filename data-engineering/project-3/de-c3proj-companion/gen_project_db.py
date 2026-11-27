# مشروع كورس 3: قاعدة متجر موسعة على 3 شهور (أكتوبر لديسمبر 2025)
# أكتوبر = نفس بيانات الدرس 9/10 المقبولة حرفيًا (20 أوردر ، 25 سطر ، ماوس 1750)
# + نوفمبر وديسمبر مولدين ببذرة ثابتة 42 لتحليلات المشروع (شهري ، خاملين ، cohort)
import sqlite3, os, random
DB = os.path.join(os.path.dirname(__file__), "store.db")
if os.path.exists(DB): os.remove(DB)
con = sqlite3.connect(DB); cur = con.cursor()
cur.execute("PRAGMA foreign_keys=ON")
cur.execute("CREATE TABLE products(product_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, category TEXT NOT NULL, price INTEGER NOT NULL)")
cur.executemany("INSERT INTO products VALUES(?,?,?,?)", [
 (1,'حقيبة لابتوب','شنط',900),
 (2,'سماعة بلوتوث','صوتيات',1200),
 (3,'شاشة 24 بوصة','شاشات',4500),
 (4,'كابل USB-C','اكسسوارات',150),
 (5,'كيبورد','اكسسوارات',700),
 (6,'ماوس','اكسسوارات',350),
 (7,'طابعة','اكسسوارات',3200),
])
cur.execute("CREATE TABLE customers(customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, city TEXT NOT NULL, phone TEXT NOT NULL)")
cur.executemany("INSERT INTO customers VALUES(?,?,?,?)", [
 (1,'أحمد سمير','القاهرة','01000000001'),
 (2,'دينا رامي','الإسكندرية','01000000006'),
 (3,'سارة علي','القاهرة','01000000004'),
 (4,'طارق حسن','القاهرة','01000000007'),
 (5,'كريم فؤاد','الفيوم','01000000003'),
 (6,'منى عادل','الجيزة','01000000002'),
 (7,'نور إيهاب','الفيوم','01000000008'),
 (8,'هشام زكي','المنصورة','01000000005'),
 (9,'زياد مراد','الفيوم','01000000009'),
 (10,'ليلى سامي','القاهرة','01000000010'),
 (11,'عمر فاروق','الجيزة','01000000011'),
 (12,'ياسمين عادل','المنصورة','01000000012'),
 (13,'حسن علي','الفيوم','01000000013'),
 (14,'رنا محمد','القاهرة','01000000014'),
 (15,'محمود سعيد','الإسكندرية','01000000015'),
])
cur.execute("CREATE TABLE orders(order_id INTEGER PRIMARY KEY, order_date TEXT NOT NULL, customer_id INTEGER NOT NULL REFERENCES customers(customer_id))")
cur.execute("""CREATE TABLE order_items(order_id INTEGER NOT NULL REFERENCES orders(order_id),
 product_id INTEGER NOT NULL REFERENCES products(product_id),
 qty INTEGER NOT NULL, unit_price INTEGER NOT NULL, PRIMARY KEY(order_id,product_id))""")

# أكتوبر 2025: نسخة حرفية من الدرس 9/10 المقبول
cur.executemany("INSERT INTO orders VALUES(?,?,?)", [
 (1,'2025-10-08',6),(2,'2025-10-19',5),(3,'2025-10-07',4),(4,'2025-10-23',3),
 (5,'2025-10-09',4),(6,'2025-10-09',1),(7,'2025-10-03',5),(8,'2025-10-20',4),
 (9,'2025-10-04',8),(10,'2025-10-27',4),(11,'2025-10-03',2),(12,'2025-10-15',3),
 (13,'2025-10-07',2),(14,'2025-10-06',8),(15,'2025-10-09',3),(16,'2025-10-13',3),
 (17,'2025-10-23',8),(18,'2025-10-21',2),(19,'2025-10-08',7),(20,'2025-10-19',8),
])
cur.executemany("INSERT INTO order_items VALUES(?,?,?,?)", [
 (1,3,1,4500),(2,1,1,900),(3,6,1,350),(4,1,1,900),(4,3,2,4500),(4,6,2,350),
 (5,2,2,1200),(6,2,1,1200),(7,3,1,4500),(8,3,1,4500),(9,2,2,1200),(10,1,1,900),
 (11,2,1,1200),(11,5,2,700),(11,6,1,350),(12,2,1,1200),(13,3,1,4500),(14,1,2,900),
 (15,2,1,1200),(16,5,1,700),(16,6,1,350),(17,5,2,700),(18,2,1,1200),(19,3,1,4500),
 (20,4,2,150),
])
# تحقق داخلي: ثوابت أكتوبر المقبولة
assert cur.execute("SELECT COUNT(*) FROM orders").fetchone()[0]==20
assert cur.execute("SELECT COUNT(*) FROM order_items").fetchone()[0]==25
assert cur.execute("SELECT SUM(qty*unit_price) FROM order_items WHERE product_id=6").fetchone()[0]==1750

random.seed(42)
oid = 21
def add_order(date,cid,items):
    global oid
    cur.execute("INSERT INTO orders VALUES(?,?,?)",(oid,date,cid))
    seen=set()
    for pid,qty in items:
        if pid in seen: continue
        seen.add(pid)
        price = cur.execute("SELECT price FROM products WHERE product_id=?",(pid,)).fetchone()[0]
        cur.execute("INSERT INTO order_items VALUES(?,?,?,?)",(oid,pid,qty,price))
    oid += 1

# نوفمبر 2025: 30 أوردر (زياد 9 لا يشتري أبدًا ، عملاء جدد 10-12 أول ظهور)
nov = []
for k in range(30):
    day = 1 + (k*37)%28
    cid = [1,2,3,4,5,6,7,8,10,11,12,1,6,3][k%14]
    items=[]
    for j in range(1 + (k*13)%3):
        pid = [6,3,1,2,4,5,6,2][(k*7+j*5)%8]
        items.append((pid, 1 + (k+j)%2))
    nov.append((f"2025-11-{day:02d}",cid,items))
for d,c,it in sorted(nov): add_order(d,c,it)
# حسن علي (13): أوردر واحد فقط في نوفمبر (مثال س7: اشترى مرة واحدة)
add_order('2025-11-15',13,[(2,1),(6,1)])

# ديسمبر 2025: 25 أوردر (نور 7 وهشام 8 وعمر 11 خاملين ، رنا 14 ومحمود 15 أول ظهور ، بلا كابل USB-C)
dec = []
for k in range(25):
    day = 1 + (k*29)%27
    cid = [1,4,6,3,2,5,1,6,10,12,14,15][k%12]
    items=[]
    for j in range(1 + (k*11)%3):
        pid = [2,6,7,3,1,6,5,2][(k*3+j*7)%8]
        items.append((pid, 1 + (k*2+j)%2))
    dec.append((f"2025-12-{day:02d}",cid,items))
for d,c,it in sorted(dec): add_order(d,c,it)

con.commit()
print("orders:", cur.execute("SELECT COUNT(*) FROM orders").fetchone()[0])
print("items:", cur.execute("SELECT COUNT(*) FROM order_items").fetchone()[0])
print("months:", cur.execute("SELECT substr(order_date,1,7), COUNT(*) FROM orders GROUP BY 1 ORDER BY 1").fetchall())
con.close()
print("db written:", DB)
