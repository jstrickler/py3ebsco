#!/usr/bin/env python
import csv

with open('../DATA/knights.csv') as knights_in:
    rdr = csv.reader(knights_in)  # <1>
    for name, title, color, quest, comment, number, ladies in rdr:  # <2>
        print('{:4s} {:9s} {}'.format(
            title, name, quest
        ))
