#!/usr/bin/env python
'''Create a print a new XML document'''
import lxml.etree as ET
# import xml.etree.ElementTree as ET

FILE_NAME = 'knights.xml'
FIELDS = ['title', 'color', 'quest', 'comment']


def main():
    '''Program entry point'''
    knight_info = get_knight_info()
    knight_root = build_tree(knight_info)
    knight_doc = ET.ElementTree(knight_root)
    display_doc(knight_root)
    write_doc(knight_doc)


def get_knight_info():
    '''Read knight data from the file'''
    info = []
    with open('../DATA/knights.txt') as kn:
        for line in kn:
            flds = line.rstrip().split(':')
            info.append(flds)
    return info


def build_tree(knight_recs):
    '''Build the new XML document'''
    tree = ET.Element('knights')
    for knight_rec in knight_recs:
        knight_element = ET.SubElement(tree, 'knight', name=knight_rec[0])
        for tag_name, tag_value in zip(FIELDS, knight_rec[1:]):
            ET.SubElement(knight_element, tag_name).text = tag_value
    return tree


def display_doc(root):
    '''Display XML document with pretty-printing'''
    doc = ET.tostring(root, pretty_print=True, xml_declaration=True)
    print(doc.decode())

def write_doc(doc):
    '''Write the XML document out to a file with pretty-printing'''
    doc.write(FILE_NAME, pretty_print=True, xml_declaration=True)

if __name__ == '__main__':
    main()
