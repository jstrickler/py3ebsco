#!/usr/bin/env python
import scipy as sp

p1 = sp.poly1d([2, 1, 4]) # <1>
print(p1)
print()

print(p1(.75)) # <2>

print(p1.r) # <3>
print()

p2 = sp.poly1d([2, 1, -4], True) # <4>
print(p2)
print()

print(p2(.75)) # <5>
print(p2.r) # <6>
print()



p3 = sp.poly1d([1, 2, 3], False, 'm') # <7>
print(p3)
print()

print(p3(100)) # <8>

print(p3.r) # <9>
print()


p4 = sp.poly1d([1,2]) # <10>
p5 = sp.poly1d([3,4])
print()

print(p4)
print()

print(p5)
print()

print(p4 + p5)
print()

print(p4 - p5)
print()

print(p4 ** 3)
print()
