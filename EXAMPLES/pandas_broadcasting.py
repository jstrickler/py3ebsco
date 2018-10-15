#!/usr/bin/env python
import pandas as pd
from printheader import print_header

cols = ['alpha','beta','gamma','delta','epsilon'] # <1>
index = pd.date_range('2013-01-01 00:00:00',periods=6, freq='D') # <2>

print(index, "\n")

values = [  # <3>
    [100, 110, 120, 930, 140],
    [250, 210, 120, 130, 840],
    [300, 310, 520, 430, 340],
    [275, 410, 420, 330, 777],
    [300, 510, 120, 730, 540],
    [150, 610, 320, 690, 640],
]


df = pd.DataFrame(values, index, cols) # <4>
print_header("Basic DataFrame:")
print(df)
print()

print_header("Triple each value")
print(df * 3)
print()  # <5>

print_header("Multiply column gamma by 1.5")
df['gamma'] *= 1.5 # <6>
print(df)
print()

