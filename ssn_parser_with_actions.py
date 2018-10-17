#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import *
from pprint import pprint

'''
grammar:
ssn = nums+ '-' nums+ '-' nums+
nums = '0' | '1' | '2' etc etc
'''

def show_token(token):
    print("Found:", token)

dash = '-'

area = Word(nums, exact=3).setParseAction(show_token)
group = Word(nums, exact=2).setParseAction(show_token)
serial = Word(nums, exact=4).setParseAction(show_token)

ssn_parser = Combine(
    area
    + dash
    + group
    + dash
    + serial
)


input_string = """
    xxx 225-92-8416 yyy
    103-33-3929 zzz 028-91-0122
"""

for match_tokens, start, stop in ssn_parser.scanString(input_string):
    print(match_tokens, start, stop)
    print()

