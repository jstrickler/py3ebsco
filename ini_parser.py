#!/usr/bin/env python
# (c)2015 John Strickler
from pprint import pprint
from pyparsing import *

'''
    inifile ::= section+
    section ::= section_tag + section_data
    section_tag ::= '[' alphanums+ ']'
    section_data ::= key_value_pair+
    key_value_pair ::= key '=' value
    key ::= alphanums+
    value ::= chars+
'''
value = Word(' \t' + printables, excludeChars='=')('value')
key = Word(alphanums, excludeChars='=')('key')
key_value_pair = Group(key + Suppress('=') + value)
section_data = Group(OneOrMore(key_value_pair))('keylist')
start_tag = Suppress('[')
end_tag = Suppress(']')
section_tag = start_tag + Word(alphanums)('section') + end_tag
section = Group(section_tag + section_data + Suppress(Optional(White())))
ini_file = OneOrMore(section)

with open('DATA/application.ini') as ini_in:
    contents = ini_in.read()

for section in ini_file.parseString(contents):
    print(section.section)
    for key, value in section.keylist:
        print('\t{0:10s} {1}'.format(key, value))
