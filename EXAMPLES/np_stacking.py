#!/usr/bin/env python
import numpy as np

a = np.array(
[[70, 31, 21, 76, 19, 5, 54, 66],
 [23, 29, 71, 12, 27, 74, 65, 73]]
) # <1>

b = np.array(
[[11, 84, 7, 10, 31, 50, 11, 98],
 [25, 13, 43, 1, 31, 52, 41, 90]]
) # <2>

print('a =>\n', a)
print()
print('b =>\n', b)
print()
print('vstack((a,b)) =>\n', np.vstack((a,b))) # <3>
print()

print('vstack((a,a[0] + a[1])) =>\n', np.vstack((a,a[0] + a[1]))) # <4>
print()

print('hstack((a,b)) =>\n', np.hstack((a,b))) # <5>
