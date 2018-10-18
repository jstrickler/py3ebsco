#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import *

street_num = Combine(Word(nums) + Optional(alphas))
street_name = OneOrMore(Word(alphas))
street_type_full = oneOf('''
    Street Avenue Road Boulevard Way Court Alley Lane
''')
street_type_abbr = oneOf('''St Ave Rd Blvd Ct'''.split())
street_type = street_type_full | (street_type_abbr + Optional('.'))
street_addr = street_num + street_name + street_type

test_streets = [
    '123 Elm St',
    '123b Elm Street',
    '123 East Rosemary Ave.'
]

for ts in test_streets:
    print("Parsing:", ts)
    print(street_addr.parseString(ts))

