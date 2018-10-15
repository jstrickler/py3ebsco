#!/usr/bin/env python
import numpy as np

r1 = np.arange(45) # <1>
r1.shape = (3,3,5) # <2>
print('r1 datatype:', r1.dtype)
print('r1 =>\n', r1, '\n')

r2 = np.arange(45.) # <3>
r2.shape = (3,3,5)
print('r2 datatype:', r2.dtype)
print('r2 =>\n', r2, '\n')

r3 = np.arange(45, dtype=np.int16) # <3>
r3.shape = (3,3,5)
print('r3 datatype:', r3.dtype)
print('r3 =>\n', r3, '\n')

