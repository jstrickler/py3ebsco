#!/usr/bin/env python
'''Create, print, and save a new XML document'''
from lxml.builder import ElementMaker # <1>
import lxml.etree as ET

FILE_NAME = 'knights.xml'
NAMESPACE_URL = 'http://www.cja-tech.com/knights' # <2>

E = ElementMaker(  # <3>
    namespace=NAMESPACE_URL,
    nsmap={'kt': NAMESPACE_URL},
)

def main():
    '''Program entry point'''
    knight_info = get_knight_info()
    knight_root = build_tree(knight_info)
    knight_doc = ET.ElementTree(knight_root)
    write_doc(knight_doc)

def get_knight_info():
    '''Read knight data from the file'''
    info = []
    with open('../DATA/knights.txt') as kn:
        for line in kn:
            flds = line[:-1].split(':')
            info.append(flds)
    return info

def build_tree(knight_recs):
    '''Build the new XML document'''
    KNIGHTS = E.knights # <4>
    KNIGHT = E.knight
    TITLE = E.title
    COLOR = E.color
    QUEST = E.quest
    COMMENT = E.comment

    knights_list =     [
        KNIGHT(
            TITLE(kr[1]),
            COLOR(kr[2]),
            QUEST(kr[3]),
            COMMENT(kr[4]),
        ) for kr in knight_recs
    ]  # <5>
    knights = KNIGHTS( # <6>
        *knights_list
    )
    return knights

def write_doc(doc):
    '''Write the pretty-printed XML document out to a file'''
    doc.write(FILE_NAME, pretty_print=True)

if __name__ == '__main__':
    main()
