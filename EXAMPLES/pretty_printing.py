#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 21:13:22 2013

"""
from pprint import pprint

struct = { # <1>
    'part1':[
        ['a','b','c'], ['d','e','f']
    ],
    'part2':{
        'red':55,
        'blue':[8, 98, -3],
        'purple':['Chicago','New York','L.A.'],
    },
    'part3': ['g','h','i'],
}

print('Without pprint:')
print(struct) # <2>
print()

print('With pprint:')
pprint(struct) # <3>
print()

print('With pprint (depth=2):')
pprint(struct, depth=2) # <4>
print()
