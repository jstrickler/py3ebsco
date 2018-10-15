#!/usr/bin/env python
import csv

field_names = ['term', 'firstname', 'lastname', 'birthplace', 'state', 'party'] # <1>

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.DictReader(presidents_in, fieldnames=field_names)  # <2>
    for row in rdr:  # <3>
        print('{firstname:25s} {lastname:12s} {party}'.format(**row))  # <4>
