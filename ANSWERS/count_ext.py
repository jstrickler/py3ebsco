#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:21:41 2013

"""
import sys
import os
from collections import Counter

start_dir = sys.argv[1]

counter = Counter()

for curr_dir, dir_list, file_list in os.walk(start_dir):
    for file_name in file_list:
        parts = file_name.split('.')
        if len(parts) > 1:
            ext = parts[-1]
            if len(ext) < 5 and not ext.isdigit():
                counter[ext] += 1

for ext, count in counter.items():
    print(ext, count)

