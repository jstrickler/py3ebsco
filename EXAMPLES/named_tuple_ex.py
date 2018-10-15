#!/usr/bin/env python
"""

@author: jstrick
Created on Thu Mar 14 09:07:57 2013

"""
from collections import namedtuple

Knight = namedtuple('Knight', 'name title color quest comment') # <1>

k = Knight('Bob', 'Sir', 'green', 'whirled peas', 'Who am i?') # <2>

print(k.title, k.name) # <3>
print(k[1], k[0]) # <4>
print()

knights = {} # <5>
with open('../DATA/knights.txt') as knights_in:
    for line in knights_in:
        flds = line.rstrip().split(':')
        knights[flds[0]] = Knight(*flds) # <6>

for knight, info in knights.items(): # <7>
    print('{0} {1}: {2}'.format(info.title, knight, info.color))
