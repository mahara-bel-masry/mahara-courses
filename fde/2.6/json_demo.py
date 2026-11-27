import json

order = {"id": "A1", "items": [{"sku": "X", "qty": 2}], "paid": True}
text = json.dumps(order)
print(text)
back = json.loads(text)
print(back["items"][0]["qty"], back["paid"])
with open("order.json", "w") as f:
    json.dump(order, f, indent=2)
with open("order.json") as f:
    print(json.load(f)["id"])
