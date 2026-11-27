import hashlib
rows = [{"name": "Ali", "email": "ali@x.com", "total": 100}]
roles = {"analyst": ["total"], "admin": ["total", "email"]}
def mask(v):
    return hashlib.sha256(v.encode()).hexdigest()[:8]
def view(row, role):
    return {k: row[k] for k in roles[role]}
print(view(rows[0], "analyst"))
print(mask(rows[0]["email"]))
print(mask("ali@x.com") == mask(rows[0]["email"]))
