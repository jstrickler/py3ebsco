#!/usr/bin/env python
import numpy as np

a = np.array(
        [[ 2,  4,  6],
        [10, 20, 30]]
) # <1>

m1 = np.matrix(a) # <2>

m2 = np.matrix([[ 1, 15],
        [ 3, 25],
        [ 5, 35]]) # <3>

print('m1 =>\n', m1)
print()

print('m2 =>\n', m2)
print()

print('m1 * 3 =>\n', m1 * 3) # <4>
print()

print('m1 * m2 =>\n', m1 * m2) # <5>
print()

print('m1.A.transpose() =>\n', m1.A.transpose()) # <6>
print()

print('m1.A.transpose() * m2.A =>\n', m1.A.transpose() * m2.A) # <7>
