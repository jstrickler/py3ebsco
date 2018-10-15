#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:34:17 2013

"""
import csv
import pickle

presidents = {}

with open('../DATA/presidents.csv') as president_in:
    rdr = csv.reader(president_in)
    for row in rdr:
        term_num = int(row[0])
        presidents[term_num] = {
            "firstname": row[1],
            "lastname": row[2],
            "birthplace": row[3],
            "birthstate": row[4],
            "party": row[5],
        }

with open('presidents.pic','wb') as president_out:
    pickle.dump(presidents, president_out)

# note: prior to Python 3.6, presidents will come out in arbitrary order. Use
# collections.ordereddict to get this behavior in earlier versions:
#
# from collections import ordereddict
# presidents = ordereddict()
