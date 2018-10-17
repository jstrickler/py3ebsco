#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import *

key = Word(alphanums)('key')
equals = Suppress('=')
value = Word(alphanums)('value')

kvexpression = key + equals + value

with open('sample.cfg') as config_in:
    config_data = config_in.read()

for match in kvexpression.scanString(config_data):
    result = match[0]
    print("{0} is {1}".format(result.key, result.value))
