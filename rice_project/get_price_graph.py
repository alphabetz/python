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
day = []
prices = []

# Get day and prices to array
for i in range(2, len(price), 7):
    day.append(price[i].contents[0].encode('utf-8'))

for i in range(3, len(price), 7):
    prices.append(float(price[i].contents[0].encode('utf-8')))

day.reverse()
prices.reverse()

# 2015 graph started at index 54 
day = day[54:]
prices = prices[54:]

print day
print len(day)
print prices
print len(prices)
