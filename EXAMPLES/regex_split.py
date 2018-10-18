#!/usr/bin/env python

import re

rx_wordsep = re.compile(r"[^\w']+")  # <1>

s1 = '''There are 10 kinds of people in a Binary world, I hear" -- Geek talk'''

words = rx_wordsep.split(s1) # <2>
print(words)

with open('../DATA/alice.txt') as alice_in:
    contents = alice_in.read()
    all_words = sorted(set(rx_wordsep.split(contents.lower())))
    print(all_words[:100])
    print()
    print(all_words[-100:])
