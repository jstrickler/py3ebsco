#!/usr/bin/env python
import sys
import numpy as np
if sys.platform == 'darwin': # <1>
    import matplotlib
    matplotlib.use('QT5Agg')
import matplotlib.pyplot as plt


dt = np.dtype([('Month', 'int8'), ('Day', 'int8'), ('Year', 'int16'), ('Temp', 'float64')]) # <2>
data = np.loadtxt('../DATA/weather/NYNEWYOR.txt',dtype=dt) # <3>

print(data['Temp'])

temps = data['Temp'] # <4>

plt.plot(temps) # <5>
plt.show() # <6>
plt.cla() # <7>


normalized_data = data[ data['Temp'] > -50 ]  # <8>
temps = normalized_data['Temp'] # <9>
plt.plot(temps) # <10>
plt.show()
