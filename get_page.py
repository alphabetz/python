# get_page.py
#
# get page with python3

import urllib.request
import os.path

u = urllib.request.urlopen('http://www.cpffeed.com/price.html')
data = u.read()

f = open('rice_rum.xml', 'wb')
f.write(data)
f.close()

if os.path.exists('rice_rum.xml') == True:
    print('Wrote file')
else:
    print('No file write!')


