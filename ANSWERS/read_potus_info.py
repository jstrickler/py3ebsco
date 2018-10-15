#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:52:46 2013

"""
import pickle
from presidentnt import President

with open('potus.pic','rb') as POTUS:
    presidents = pickle.load(POTUS)

for president in presidents:
    print("{0.firstname} {0.lastname} ({0.party})".format(president))
