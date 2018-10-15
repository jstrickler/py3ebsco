#!/usr/bin/env python
import numpy as np
import scipy as sp

def set_default(value, limit, default): # <1>
    if value > limit:
        value = default

    return value


raw_samples = np.array([5, 18, 36, 1000, 98, 2323]) # <2>

try:
    print("Without sp.vectorize:")
    norm_samples = set_default(raw_samples, 100, 0) # <3>
except ValueError as err:
    print("Function failed:", err) # <4>
else:
    print(norm_samples)
finally:
    print()

set_default_vect = sp.vectorize(set_default) # <5>
try:
    print("With sp.vectorize:")
    norm_samples = set_default_vect(raw_samples, 100, 0) # <6>
except ValueError as err:
    print("Function failed:", err)
else:
    print(norm_samples) # <7>
finally:
    print()
