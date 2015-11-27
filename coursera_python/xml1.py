import urllib
import xml.etree.ElementTree as ET


url = 'http://python-data.dr-chuck.net/comments_168367.xml'
uh = urllib.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
allnum = []

for i in xrange(0, len(counts)):
    allnum.append(int(counts[i].text))

allsum = sum(allnum)
print allsum

