import requests

all_items = []
page = 1
while True:
    response = requests.get("http://127.0.0.1:8765/orders", params={"page": page}, timeout=5)
    items = response.json()["items"]
    if not items:
        break
    all_items.extend(items)
    page += 1
print("pages:", page - 1)
print("orders:", len(all_items))
