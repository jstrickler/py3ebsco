#!/usr/bin/env python

import sys
import re
import fileinput
import argparse
from glob import glob  # <1>
from itertools import chain  # <2>

arg_parser = argparse.ArgumentParser(description="Emulate grep with python") # <3>

arg_parser.add_argument(
    '-i',
    dest='ignore_case', action='store_true',
    help='ignore case'
) # <4>

arg_parser.add_argument(
    'pattern', help='Pattern to find (required)'
) # <5>

arg_parser.add_argument(
    'filenames',nargs='*',
    help='filename(s) (if no files specified, read STDIN)'
) # <6>

args = arg_parser.parse_args() # <7>

print('-' * 40)
print(args)
print('-' * 40)

regex = re.compile(args.pattern, re.I if args.ignore_case else 0) # <8>

filename_gen = (glob(f) for f in args.filenames) # <9>
filenames = chain.from_iterable(filename_gen) # <10>

for line in fileinput.input(filenames): # <11>
    if regex.search(line):
        print(line.rstrip())

