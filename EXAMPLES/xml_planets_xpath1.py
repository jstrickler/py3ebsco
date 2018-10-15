#!/usr/bin/env python

# import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('../DATA/solar.xml') # <1>

inner_nodes = doc.findall('innerplanets/planet') # <2>

outer_nodes = doc.findall('outerplanets/planet') # <3>

print('Inner:')
for planet in inner_nodes:  # <4>
    print('\t',planet.get("planetname")) # <5>

print('Outer:')
for planet in outer_nodes:  # <4>
    print('\t',planet.get("planetname")) # <5>

