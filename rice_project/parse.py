# Python2.7
# parse.py
#
# learn parse

import bs4
import requests

res = requests.get('http://www.cpffeed.com/price_detail.html?product=8')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('bhtml body table tbody tr td table tbody tr td table tbody tr td table tbody tr td.price_product')

print elems
