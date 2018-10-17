#!/usr/bin/env python

list1 = list()  # create new empty list
list2 = []
towns = ['Ipswich', 'Essex', 'Marblehead', 'Boston']
towns.append('Salem')
print(towns)
more_towns = ['Woeburn', 'Peabody', 'Worcester']
towns.extend(more_towns)
print(towns)
towns.insert(0, 'Marlborough')
towns.insert(4, 'Boxboro')
print(towns)

del towns[2]
print(towns)

towns.remove('Boston')
print(towns)

t = towns.pop()
print(t)
t = towns.pop()
print(t)
print(towns)
t = towns.pop(2)
print(t)
print(towns)

print(towns[0])
print(towns[2])
print(towns[-1])
print(towns[len(towns)-1])
print(towns[-5])
# print(towns[-10]) ERROR!

print(towns[0:2])  # START:STOP  :STOP START:
print(towns[:2])

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(fruits[:5])
print(fruits[-5:])
print(fruits[13:16])
print()

for town in towns:
    print(town)
print()

# while True:
#     town = next(towns)


for wombat in towns:
    print(wombat)
print()

for NOT_THIS_THING_AGAIN in towns:
    print(NOT_THIS_THING_AGAIN)
print()

print(len(fruits))
for fruit in fruits[:8]:
    print(fruit)
print()

for fruit in fruits[-5:]:
    print(fruit)




