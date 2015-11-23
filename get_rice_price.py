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

# Calculate price changed
last_price = float(price[10].contents[0].encode('utf-8'))
cur_price = float(price[3].contents[0].encode('utf-8'))
change = cur_price - last_price

print "Fetched price from CPF"

print "---------------------"
print "ราคารำขาว"
# since original page arranged date after price we must re-arrange
print "สัปดาห์ที่ : " ,price[1].contents[0] 
print "วันที่ :" ,price[2].contents[0]
print bcolors.BOLD + "ราคา : %.2f" %cur_price

if change < 0:
    print "เปลี่ยนแปลง : " + bcolors.FAIL + "%.2f" %change + bcolors.ENDC
else:
    print "เปลี่ยนแปลง : " + bcolors.OKGREEN + "%.2f" %change + bcolors.ENDC
 
print "---------------------"











