#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:52:46 2013

"""
import pickle

with open('presidents.pic','rb') as presidents_in:
    presidents = pickle.load(presidents_in)

for term_number, president_info in presidents.items():
    print("{:20.20s} {:20.20s} {}".format(
        president_info['firstname'],
        president_info['lastname'],
        president_info['party'],
    ))
