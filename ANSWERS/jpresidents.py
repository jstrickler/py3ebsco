#!/usr/bin/python

import json

with open('../DATA/presidents.json') as PRES:
    p = json.load(PRES)

for pres in p['presidents']:
    name = pres['lname'] + ', ' + pres['fname']
    state = pres['birthstate']
    print('{0:40s} {1:30s}'.format(name, state))
