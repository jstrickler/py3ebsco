#!/usr/bin/env python

import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo Z883  consequat. Duis aute irure dolor in reprehenderit in  
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

pattern = r'(?P<letter>[A-Z])(?P<number>\d{2,3})'  # <1>

for m in re.finditer(pattern, s):
    print(m.group('letter'), m.group('number')) # <2>


p2 = r'\d+\s+\w+\s+(?:St.?|Street)'

my_text = 'blah blah 123 Elm Street blah blah 456 Walnut St. blah blah'

m = re.search(p2, my_text)
print(m.group())
print(re.findall(p2, my_text))




