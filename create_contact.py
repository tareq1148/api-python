import requests

BASE = "https://masar-class-api.a-f-almatrafi.workers.dev/api"
me = "your-github-username"

r = requests.post(f"{BASE}/students", json={"username": me}, timeout=10)
print("register:", r.status_code)  # 201 the first time — 409 if already registered; both are fine

r = requests.post(
    f"{BASE}/students/{me}/contacts",
    json={"name": "Salem", "phone": "0501234567"},
    timeout=10,
)
print("create:", r.status_code)
if r.status_code == 201:
    print("new contact id:", r.json()["id"])
