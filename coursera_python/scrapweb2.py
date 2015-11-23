import urllib
from BeautifulSoup import *

#init url http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
url = raw_input("Enter URL: ")
count = int(raw_input("Enter Count: "))
position = int(raw_input("Enter Position: "))

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    print "Getting page: ", url
    # Retrieve all of the anchor tags
    tags = soup('a')
    cnt = 0
    for tag in tags:
        tag.get('href', None)
        cnt += 1
        if cnt == position:
            url = tag.get('href').encode('utf-8')
print "Finished"
print "Last URL ", url
