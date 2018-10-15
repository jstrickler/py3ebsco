#!/usr/bin/env python

import fileinput

for line in fileinput.input(): # <1>
    if 'bird' in line:
        print('{}: {}'.format(fileinput.filename(), line), end=' ') # <2>

