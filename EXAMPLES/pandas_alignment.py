#!/usr/bin/env python
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from printheader import print_header # <1>

dataset1 = np.arange(9.).reshape((3,3))  # <2>

df1 = DataFrame(  # <3>
    dataset1,
    columns = ['apple', 'banana', 'mango'],
    index = ['orange', 'purple', 'blue']
)

dataset2 = np.arange(12.).reshape((4,3)) # <2>

df2 = DataFrame(   # <3>
    dataset2,
    columns = ['apple', 'banana', 'kiwi'],
    index = ['orange', 'purple', 'blue', 'brown']
)

print_header('df1')
print(df1)  # <4>
print()

print_header('df2')
print(df2) # <4>
print()

print_header('df1 + df2')
print(df1 + df2) # <5>

print_header('df1.add(df2, fill_value=0)')
print(df1.add(df2, fill_value=0))  # <6>
