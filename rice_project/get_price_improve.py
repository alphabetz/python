# get_rice_price.py
# coding: utf-8
# get rice price from CPF the rice's price

import urllib
from BeautifulSoup import *

class bcolors:
    OKGREEN = '\033[92m'
    BOLD = '\033[1m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

url = 'http://www.cpffeed.com/price_detail.html?product=8'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
price = soup.findAll("td", { "class" : "price_product" } )

"""
# Calculate price changed
last_price = float(price[10].contents[0].encode('utf-8'))
cur_price = float(price[3].contents[0].encode('utf-8'))
change = cur_price - last_price
"""
print "Fetched price from CPF"
print "---------------------"
j = 1

for i in price:
    if j > len(price):
            print "END OF LIST"
            quit()  
    try:
        print "สัปดาห์ที่ : ",price[j].contents[0]
        j += 1 
        print "วันที่ :" ,price[j].contents[0]
        j += 1
        print bcolors.BOLD + "ราคา :" , price[j].contents[0] + bcolors.ENDC
        j += 1
        print "---------------------"
    except IndexError:
        j += 4

"""
# This for week, day and price print
j = 1
for i in price:
...  try:
...   print price[j].contents[0]
...   j += 1
...  except IndexError:
...   j += 4

# for day and price only change j = 2, except j += 5
# for only day set j = 2 step j += 7
# more elegance way to get day
 for i in range(2, len(price), 7):
...  print price[i].contents[0]

append to array day.append(price[i].contents[0].encode('utf-8'))

# elegance way to get price
 for i in range(3, len(price), 7):
 ...  print price[i].contents[0]

append to array prices.append(float(price[i].contents[0].encode('utf-8')))

AND reverse() on both array
"""









