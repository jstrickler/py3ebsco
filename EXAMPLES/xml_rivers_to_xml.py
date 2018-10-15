#!/usr/bin/env python
# (c) 2016 John Strickler
#
import csv
from dicttoxml import dicttoxml # <1>
import lxml.etree as ET
from pprint import pprint

rivers = {'rivers': [] } # <2>

with open('../DATA/longest_rivers.csv') as rivers_in:
    rdr = csv.reader(rivers_in)
    for row in rdr:
        rivers['rivers'].append({'name': row[0], 'length': row[1]})  # <3>

pprint(rivers)
print('-' * 60)


snippet = dicttoxml(rivers, attr_type=False, root=False,
    item_func=lambda x: x.rstrip('s'))

river_root = ET.fromstring(snippet)
river_doc = ET.ElementTree(river_root)

print(ET.tostring(river_doc, pretty_print=True, xml_declaration=True).decode())

river_doc.write('longest_rivers.xml', pretty_print=True,
    xml_declaration=True)
