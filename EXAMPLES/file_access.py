#!/usr/bin/env python

import sys
import os

if len(sys.argv) < 2:
    sys.stderr.write('Please specify a starting directory\n')
    sys.exit(1)

start_dir = sys.argv[1]

for base_name in os.listdir(start_dir): # <1>
    file_name = os.path.join(start_dir,base_name)
    if os.access(file_name,os.W_OK):  # <2>
        print(file_name,"is writable")
