#!/usr/bin/env python
#
import numpy as np

a = np.arange(1, 31) # <1>
a.shape = 3, 10 # <2>
print(a)

def spam(n): # <3>
    return n ** 2

b = spam(a) # <4>
print(b)
