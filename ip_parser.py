#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import *

def validate_ip(tokens):
    raw_octet = tokens[0]
    octet = int(raw_octet)
    if octet > 255:
        raise ParseException("Octet cannot be > 255")
    return octet

octet = Word(nums, max=3)('octets').setParseAction(validate_ip)

dot = Suppress('.')
ip = octet + dot + octet + dot + octet + dot + octet

tokens = ip.parseString('123.34.93.23 blah blah')
print(tokens)
