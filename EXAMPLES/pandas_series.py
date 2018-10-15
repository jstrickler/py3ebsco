#!/usr/bin/env python
import numpy as np
import pandas as pd

NUM_VALUES = 10
index = [chr(i) for i in range(97,97 + NUM_VALUES)] # <1>
print("index:", index, '\n')

s1 = pd.Series(np.linspace(1,5,NUM_VALUES), index=index) # <2>
s2 = pd.Series(np.linspace(1,5,NUM_VALUES)) # <3>

print("s1:", s1, "\n")
print("s2:", s2, "\n")

print("selecting elements")
print(s1[['h','b']], "\n")  # <4>

print(s1[['a','b','c']], "\n") # <4>

print("slice of elements")
print(s1['b':'d'], "\n") # <5>

print("sum(), mean(), min(), max():")
print(s1.sum(), s1.mean(), s1.min(), s1.max(), "\n")  # <6>

print("cumsum(), cumprod():")
print(s1.cumsum(), s1.cumprod(), "\n") # <6>

print('a' in s1) # <7>
print('m' in s1) # <7>
print()

s3 = s1 * 10 # <8>
print("s3 (which is s1 * 10)")
print(s3, "\n")

s1['e'] *= 5

print("boolean mask where s3 > 25:")
print(s3 > 25, "\n") # <9>

print("assign -1 where mask is true")
s3[s3 < 25] = -1 # <10>
print(s3, "\n")


s4 = pd.Series([-0.204708, 0.478943, -0.519439]) # <11>
print("s4.max(), .min(), etc.")
print(s4.max(), s4.min(), s4.max() - s4.min(), '\n') # <12>

s = pd.Series([5,10,15], ['a','b','c'])  # <13>
print("creating series with index")
print(s)
