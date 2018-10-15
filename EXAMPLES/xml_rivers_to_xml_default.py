#!/usr/bin/env python
# (c) 2016 John Strickler
#
import csv
from dicttoxml import dicttoxml # <1>
import lxml.etree as ET

rivers = {'rivers': []} # <2>
with open('../DATA/longest_rivers.csv') as rivers_in:
    rdr = csv.reader(rivers_in)
    for row in rdr: # <3>
        rivers['rivers'].append({'name': row[0], 'length': row[1]})

snippet = dicttoxml(rivers)  # <4>

river_root = ET.fromstring(snippet) # <5>
river_doc = ET.ElementTree(river_root) # <6>

print(ET.tostring(river_doc, pretty_print=True, xml_declaration=True).decode())  # <7>

river_doc.write('longest_rivers_default.xml', pretty_print=True, xml_declaration=True) # <8>
