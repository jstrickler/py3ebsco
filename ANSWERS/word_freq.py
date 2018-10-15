#!/usr/bin/env python

import sys
import re

word_sep_rx = re.compile(r"[^\w']+")

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        found = {}
        for line in file_in:
            words = word_sep_rx.split(line)
            for word in words:
                if word == '' or word == "'":
                    continue
                word = word.lower()
                found[word] = found.get(word, 0) + 1

    for word, count in sorted(found.items()):
        print("{:<16s} {:4d}".format(word, count))
