#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import *

def upper_case_it(tokens):
    return [t.upper() for t in tokens]
    # return list(map(lambda t: t.upper(), tokens))

prefix = 'A Fist Full of '

fist_contents = Word(alphas + ' ')

fist_contents.setParseAction(upper_case_it)

title_parser = Combine(prefix + fist_contents)

titles = (
    'A Fist Full of Dollars',
    'A Fist Full of Spaghetti',
    'A Fist Full of Wombats',
    'A Fist Full of Jelly Beans',
)

for title in titles:
    print(title_parser.parseString(title)[0])
