#!/usr/bin/env python

from scipy import constants as K # <1>

print("pi: {0}".format(K.pi)) # <2>
print("Planck: {0}".format(K.Planck)) # <2>
print("c (speed of light): {0}".format(K.c)) # <2>

print("natural unit of energy: {0}".format(K.value('natural unit of energy')))
print("natural unit of energy (Unit): {0}".format(K.unit('natural unit of energy')))

