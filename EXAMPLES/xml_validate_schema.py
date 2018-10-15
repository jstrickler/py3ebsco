#!/usr/bin/env python
# (c) 2016 John Strickler
#
import os
from lxml import etree

XML_BASE = '../DATA' # <1>
PRES_SCHEMA_PATH = os.path.join(XML_BASE, 'presidents.xsd')
PRES_XML_PATH = os.path.join(XML_BASE, 'presidents.xml')
BAD_PRES_XML_PATH = os.path.join(XML_BASE, 'presidents_bad.xml')

pres_schema = etree.XMLSchema(file=PRES_SCHEMA_PATH) # <2>
pres_parser = etree.XMLParser(schema=pres_schema) # <3>

def validate(xml_path):
    try:
        pres_doc = etree.parse(xml_path, parser=pres_parser) # <4>
    except etree.ParseError as err: # <5>
        print(("Error Parsing {}:".format(xml_path)))
        print(err)
    else:
        print(("Parsed {} OK:".format(xml_path)))
        print(pres_doc) # <6>
    print(('-' * 60))

for xml_doc in PRES_XML_PATH, BAD_PRES_XML_PATH: # <7>
    validate(xml_doc)
