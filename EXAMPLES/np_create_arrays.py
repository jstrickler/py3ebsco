#!/usr/bin/env python
import numpy as np

a = np.array([[1, 2.1, 3], [4, 5, 6], [7, 8, 9], [20, 30, 40]]) # <1>
print(a)
print("# dims", a.ndim) # <2>
print("shape", a.shape) # <3>
print()

a_zeros = np.zeros((3,5), dtype=np.uint32) # <4>
print(a_zeros)
print()

a_ones = np.ones([2,3,4,5]) # <5>
print(a_ones)
print()

# with uninitialized values
a_empty = np.empty([3,8]) # <6>
print(a_empty)

print(a.dtype) # <7>


nan_array = np.zeros([5,10]) # <8>
nan_array[:] = np.nan
print(nan_array)









