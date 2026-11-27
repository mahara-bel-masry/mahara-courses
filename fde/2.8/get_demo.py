import requests

response = requests.get("http://127.0.0.1:8765/orders", params={"page": 1}, timeout=5)
print(response.status_code)
data = response.json()
print(data["page"], len(data["items"]))
print(data["items"][0])
