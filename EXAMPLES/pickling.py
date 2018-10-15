#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Mar 16 00:47:05 2013

"""
import pickle
import pprint

# <1>
airports = {
    'RDU': 'Raleigh-Durham', 'IAD': 'Dulles', 'MGW': 'Morgantown',
    'EWR': 'Newark', 'LAX': 'Los Angeles', 'ORD': 'Chicago'
}

colors = [
    'red', 'blue', 'green', 'yellow', 'black',
    'white', 'orange', 'brown', 'purple'
]

data = [  # <2>
    colors,
    airports,
]

with open ('../TEMP/pickled_data.pic', 'wb') as pic_out: # <3>
    pickle.dump(data, pic_out) # <4>

with open ('../TEMP/pickled_data.pic', 'rb') as pic_in: # <5>
    pickled_data = pickle.load(pic_in) # <6>

pprint.pprint(pickled_data) # <7>
