# find_rice.py
#
# find the rice's price

from xml.etree.ElementTree import parse

doc = parse('rice_rum.xml')

for rum in doc.findtext('รำ'):
    print rum
