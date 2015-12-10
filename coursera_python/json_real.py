import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_168371.json'
data = urllib.urlopen(url).read()

info = json.loads(data)
total = 0
for item in info['comments']:
    total += int(item['count'])

print total
