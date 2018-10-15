#!/usr/bin/env python

print("** About Spam **")
with open("../DATA/spam.txt") as spam_in:
    for line in spam_in:
        print(line.rstrip('\r\n')) # <1>

with open("../DATA/eggs.txt") as eggs_in:
    eggs = eggs_in.readlines()  # <2>

print("\n\n** About Eggs **")
print(eggs[0].rstrip())  # <3>
print(eggs[2].rstrip())
