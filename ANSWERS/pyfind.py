#!/usr/bin/env python

import sys
import re

if len(sys.argv) < 3:
    print("Usage: pfind PATTERN file ...")
    sys.exit(1)

try:
    pattern = re.compile(sys.argv[1])
except re.error as e:
    print("Error compiling RE: {}".format(e))
    sys.exit()

for file_name in sys.argv[2:]:
    try:
        file_in = open(file_name)
    except IOError as e:
        print("Unable to open {}: {}".format(file_name, e))
        continue
    else:
        for line in file_in:
            if pattern.search(line):
                print("{}: {}".format(file_name, line), end=' ')
        file_in.close()
