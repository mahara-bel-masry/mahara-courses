import requests

response = requests.get("http://127.0.0.1:8765/missing", timeout=5)
print(response.status_code)
try:
    response.raise_for_status()
except requests.HTTPError as error:
    print("HTTPError:", error.response.status_code)
try:
    requests.get("http://127.0.0.1:9", timeout=2)
except requests.ConnectionError:
    print("ConnectionError")
