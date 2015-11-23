import urllib
from BeautifulSoup import *

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_168370.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
numlist = []
total = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   numlist.append(int(tag.contents[0].encode('utf-8')))

for num in numlist:
    total += num
