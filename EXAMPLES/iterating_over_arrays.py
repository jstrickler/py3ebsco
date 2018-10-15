#!/usr/bin/env python

mylist = [ "Idle", "Cleese", "Chapman", "Gilliam", "Palin", "Jones"]
mytup = ("Roger", "Old Woman", "Prince Herbert", "Brother Maynard")
mystr = "She turned me into a newt"

for p in mylist:  # <1>
    print(p)
print()

for r in mytup:  # <2>
    print(r)
print()

for ch in mystr:  # <3>
    print(ch, end=' ')
print()
