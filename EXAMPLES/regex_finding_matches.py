#!/usr/bin/env python

import re


s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

pattern = r'[A-Z]\d{2,3}\b'  # <1>

if re.search(pattern, s):  # <2>
    print("Found pattern.")
print()

m = re.search(pattern, s)  # <3>
print(m)
if m:
    print("Found:", m.group(0)) # <4>
print()

# def group(group_num=0):
#     pass

for m in re.finditer(pattern, s): # <5>
    print(m.group(), m.span(), m.start(), m.end())
print()

matches = re.findall(pattern, s)  # <6>
print("matches:",  matches)

# re.match(pattern, str)
# re.fullmatch(pattern, str)

#   ^    $    \b

# all_matches = []
# for file_name in list_of_file_names:
#     with open(file_name) as file_in:
#         contents = file_in.read()
#         all_matches.extend(re.findall(my_regex, contents))
