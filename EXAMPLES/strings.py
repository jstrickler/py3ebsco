#!/usr/bin/env python

a = "My hovercraft is full of EELS"

print("original:", a)
print("upper:", a.upper())
print("lower:", a.lower())
print("swapcase:", a.swapcase()) # <1>
print("title:", a.title())  # <2>
print("e count (normal):", a.count('e'))
print("e count (lower-case):", a.lower().count('e')) # <3>
print("found EELS at:", a.find('EELS'))
print("found WOLVERINES at:", a.find('WOLVERINES')) # <4>

b = "graham cracker"
print("Capitalized:", b.capitalize()) # <5>

#  print(x, y, z)


record = 'Twain:Mark:Huckleberry Finn'
fields = record.split(':')
print(fields)

data = 'sis boom bah'
print(data.split())


s = '     All my exes live in Texas     '
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print(s.strip().replace(' ', '_'))
print()


s = 'xyxxyyxxxyyyAll my exes live in Texasxyyxxyyyxyxyxyx'
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')




