#!/usr/bin/env python

from knight import Knight, UnknownKnightError

for name in 'Arthur', 'Robin', 'Alice':
    try:
        k = Knight(name)
    except UnknownKnightError as err:
        print(err)
    else:
        print("Name: {} {}".format(k.title, name))
        print("Favorite Color:", k.favorite_color)
        print()
