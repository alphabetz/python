import  urllib
import json

url = 'http://python-data.dr-chuck.net/comments_42.json'
data = urllib.urlopen(url).read()

info = json.loads(data)

count = 0

for item in info['comments']:
    count += int(item['count'])

print count
