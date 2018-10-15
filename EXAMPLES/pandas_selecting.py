#!/usr/bin/env python
import pandas as pd
from printheader import print_header

cols = ['alpha','beta','gamma','delta','epsilon'] # <1>
index = ['a','b','c','d','e','f'] # <2>

values = [ # <3>
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]

df = pd.DataFrame(values, index=index, columns=cols)  # <4>
print_header('DataFrame df')
print(df, '\n')

print_header("df['alpha']")
print(df['alpha'], '\n')   # <5>

print_header("df.beta")
print(df.beta, '\n') # <6>

print_header("df['b':'e']")
print(df['b':'e'], '\n')  # <7>

print_header("df[['alpha','epsilon','beta']]")
print(df[['alpha','epsilon','beta']]) # <8>
print()


print_header("df[['alpha','epsilon','beta']]['b':'e']")
print(df[['alpha','epsilon','beta']]['b':'e']) # <9>
print()


