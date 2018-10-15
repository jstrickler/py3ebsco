#!/usr/bin/env python

import sys

try:
    celsius = float(input("Enter Celsius temp: "))
except ValueError as e:
    print("Error!", e)
    sys.exit(1)

fahrenheit = ((9 * celsius) / 5) + 32

print("{:.1f} C is {:.1f} F".format(celsius, fahrenheit))

