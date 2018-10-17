#!/usr/bin/env python
# (c)2015 John Strickler
from pyparsing import *

'''
grammar:
ssn = nums+ '-' nums+ '-' nums+
nums = '0' | '1' | '2' etc etc
'''

dash = '-'

ssn_parser = Combine(
    Word(nums, exact=3)
    + dash
    + Word(nums, exact=2)
    + dash
    + Word(nums, exact=4)
)

input_string = """
    xxx 225-92-8416 yyy
    103-33-3929 zzz 028-91-0122
"""

for matches, start, stop in ssn_parser.scanString(input_string):
    print(matches, start, stop)


