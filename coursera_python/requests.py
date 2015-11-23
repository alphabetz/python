import requests

r = requests.get("http://192.168.1.14/")

print r.status_code
print r.headers
print r.content
