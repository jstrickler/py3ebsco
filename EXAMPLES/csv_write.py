#!/usr/bin/env python
import sys
import csv

data = (
    ('February', 28, 'The shortest month, with 28 or 29 days'),
    ('March', 31, 'Goes out like a "lamb"'),
    ('April', 30, 'Its showers bring May flowers'),
)

with open('../TEMP/stuff.csv', 'w') as STUFF:
    if sys.platform == 'win32':
        wtr = csv.writer(STUFF, lineterminator='\n') # <1>
    else:
        wtr = csv.writer(STUFF) # <1>
    for row in data:
        wtr.writerow(row) # <2>
