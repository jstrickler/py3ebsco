#!/usr/bin/env python

person = 'Paul', 'Allen', 'Microsoft', 65

print(person[0])
print(len(person))
print(type(person))

first_name, last_name, company, age = person # unpack!

colors = [('red', 5), ('green', 10), ('yellow', 8)]
# c = colors[0]
# print(c)
# color, value = c
# print(color, value)
#
# color, value = colors[0]
# print(color, value)
#
#
# for color_entry in colors:
#     color, value =  color_entry
# print()

for color, value in colors:
    print(color, value)
print()

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux', 'Git'),
]

for first_name, last_name, *product in people:
    print(first_name, last_name, "/".join(product))
print()


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


print(people[0])
print(people[0][0])

