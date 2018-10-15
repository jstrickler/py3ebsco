#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

rx_code = re.compile(r'(?P<letter>[A-Z])(?P<number>\d{2,3})', re.I)

s2 = rx_code.sub("[REDACTED]", s) # <1>
print(s2)
print()

s3, count = rx_code.subn("___", s) # <2>
print("Made {} replacements".format(count))
print(s3)
