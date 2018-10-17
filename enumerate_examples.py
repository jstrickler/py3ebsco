#!/usr/bin/env python


colors = ['blue', 'purple', 'pink']

for color in colors:
    print(color)
print()


xcolors = [(0, 'blue'), (1, 'purple'), (2, 'pink')]

for i, color in xcolors:
    print(i, color)
print()

for i, color in enumerate(colors):
    print(i, color)
print()
e = enumerate(colors)
print(e)
print(list(e))
print(list(e))

x = [False]
print(x * 10)

x = [1, 2, 3]
print(x * 10)

print('-' * 60)

flags = [False] * 25
print(flags)





