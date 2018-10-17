#!/usr/bin/env python

names = ['Manny', 'Moe', 'Jack']

n2 = names

n2.append('Fred')

print(names)

n3 = list(names)
n3.append('Jason')
print(names)
print(n3)

n4 = names[:]

s1 = 'spam'
s1 += 'ham'
# s1 = s1 + 'ham'



