#!/usr/bin/env python
import numpy as np

a = np.array(
[[70, 31, 21, 76],
 [23, 29, 71, 12]]
) # <1>

print('a =>\n', a)
print()

print("for row in a: =>")
for row in a: # <2>
    print("row:", row)
print()

print("for column in a.T:")
for column in a.T: # <3>
    print("column:", column)
print()

print("for elem in a.flat: =>")
for elem in a.flat: # <4>
    print("element:", elem)
