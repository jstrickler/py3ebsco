#!/usr/bin/env python
import re

num = re.compile(r"\b\d{3}-\d{4}\b")

with open("../DATA/custinfo.dat") as f:
    for line in f:
        if num.search(line):
            print(line, end='')

