#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.lower().startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

# [EXPRESSION for VAR in ITERABLE if CONDITION]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [float(n) for n in nums if n > 100]
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print("last names:", last_names)

last_names = [p[1] for p in people if p[1][0] > 'G']
print("last names:", last_names, '\n')

x = [(i, i**2, i**3) for i in range(10)]
print("x:", x, '\n')

last_names = (p[1] for p in people)
print(last_names)

for last_name in last_names:
    print(last_name)

