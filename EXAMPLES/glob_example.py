#!/usr/bin/env python

from glob import glob

files = glob('../DATA/*.txt') # <1>
print(files)
