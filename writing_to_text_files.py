#!/usr/bin/env python

with open('fruits.txt') as fruits_in:
    with open('shortfruits.txt', 'w') as short_fruits_out:
        with open('longfruits.txt', 'w') as long_fruits_out:
            for fruit in fruits_in:
                if len(fruit) > 7:
                    long_fruits_out.write(fruit)
                else:
                    short_fruits_out.write(fruit)

# with open('fruits.txt') as fruits_in, open('shortfruits.txt', 'w') as short_fruits_out, open('longfruits.txt', 'w') as long_fruits_out:
