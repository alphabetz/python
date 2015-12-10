import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Name of University: ')
	url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
	data = urllib.urlopen(url).read()
    
	try:
		js = json.loads(str(data))
	except:
		js = None
	if 'status' not in js or js['status'] != 'OK':
		print 'Something wrong with DATA'
		print data
		continue
	
	print json.dumps(js, indent=4)
	location = js['results'][0]['place_id']
	print location
