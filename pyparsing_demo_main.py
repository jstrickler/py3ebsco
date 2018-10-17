#!/usr/bin/env python
# (c)2015 John Strickler

from pyparsing import Word, alphas, nums, Suppress

hyphenated_word = Word(alphas) + Suppress('-') + Word(nums)

tokens = hyphenated_word.parseString('foo-12')

print(tokens)


