#!/usr/bin/env python
import csv

with open('../DATA/computer_people.txt') as computer_people_in:
    rdr = csv.reader(computer_people_in, delimiter=';') # <1>

    for first_name, last_name, known_for in rdr:  # <2>
        print('{}: {}'.format(last_name, known_for))

