#!/usr/bin/env python
# (c) 2016 John Strickler
#
import csv
from lxml import etree
from lxml.builder import ElementMaker # <1>

NS_RIVER_URL = "http://www.cja-tech.com/ns/river" # <2>

E = ElementMaker( # <3>
    namespace=NS_RIVER_URL,
    nsmap = {'lr' : NS_RIVER_URL}
)

RIVER_LIST = E.riverlist # <4>
RIVER = E.river
RIVER_NAME = E.name
RIVER_LENGTH = E.length

doc = RIVER_LIST() # <5>

with open('../DATA/longest_rivers.csv') as rivers_in:
    rdr = csv.reader(rivers_in)
    for row in rdr: # <6>
        doc.append(
            RIVER(  # <7>
                RIVER_NAME(row[0]),
                RIVER_LENGTH(row[1])
            )
        )

print(etree.tostring(doc, pretty_print=True).decode()) # <8>
etree.ElementTree(doc).write('longest_rivers_ns.xml',
                                   pretty_print=True) # <9>
