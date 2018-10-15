#!/usr/bin/python

from xml.etree import ElementTree as ET

presroot = ET.parse('../DATA/presidents.xml')

for pres in presroot.findall("president"):
    name = pres.findtext('name/last') + ', ' + pres.findtext('name/first')
    state = pres.findtext('birthstate')
    print('{0:40s} {1:30s}'.format(name, state))
