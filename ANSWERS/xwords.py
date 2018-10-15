#!/usr/bin/python 

import xml.etree.ElementTree as ET

words = open('../DATA/words.txt')
xwords = [word.rstrip() for word in words if word.startswith('x')]
words.close()

root = ET.Element('words')

for word in xwords:
    ET.SubElement(root, 'word').text = word

tree = ET.ElementTree(root)
tree.write('xwords.xml')
