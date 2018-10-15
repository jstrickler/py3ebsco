#!/usr/bin/env python
import pandas as pd
import numpy as np

hourly = pd.date_range('1/1/2013 00:00:00','1/3/2013 23:59:59', freq='H') # <1>
print("Number of periods: ",len(hourly))

seconds = pd.date_range('1/1/2013 12:00:00',freq='S',periods=(60*60*18)) # <2>
print("Number of periods: ", len(seconds))
print("Last second: ",seconds[-1])

monthly = pd.date_range('1/1/2013','12/31/2013', freq='M') # <3>
print("Number of periods: {0} Seventh element: {1}".format(
    len(monthly), 
    monthly[6]
))

NUM_DATA_POINTS = 1441 # <4>

dates = pd.date_range('4/1/2013 00:00:00', periods=NUM_DATA_POINTS, freq='T') # <5>

data = np.random.random(NUM_DATA_POINTS) # <6>

series = pd.Series(data,index=dates) # <7>


time_slice = series['4/1/2013 10:00:00':'4/1/2013 10:30:00'] # <8>
print(time_slice)   # 31 values

