#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import *


phrase = Suppress('big') + Word(alphas)

s = 'this is big news: the big boss has landed a big deal'

for match in phrase.scanString(s):
    print(match)
