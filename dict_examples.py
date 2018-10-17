#!/usr/bin/env python

d1 = dict()
d2 = {'red': 5, 'pink': 6, 'scarlet': 2}
d3 = {}
d4 = dict(red=5, pink=6, scarlet=2)

pairs = [('red', 5), ('pink', 6), ('scarlet', 2)]
d5 = dict(pairs)

keys = ['red', 'pink', 'scarlet']
values = [5, 6, 2]
colors = dict(zip(keys, values))
print(colors)

colors['coral'] = 8
colors['peach'] = 1
print(colors)
print(colors['pink'])

print(colors.get('purple'))
print(colors.get('purple', -1))

print(len(colors))
print(colors.keys())
print(colors.values())

more_colors = {'blue': 5, 'pink': 9, 'green': 6}

colors.update(more_colors)
print(colors)
print()

for color_name, color_value in colors.items():
    print(color_name, color_value)


x = {
    ('a', 'b'): 5,
    ('a', 'c'): 8,
    ('b', 'c'): 4,
}

print(x.keys())
print(x.values())

print(x[('a', 'c')])



