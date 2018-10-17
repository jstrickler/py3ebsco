#!/usr/bin/env python

cave_man = 'Fred Flintstone'
city = 'Bedrock'


x = cave_man + 'lives_in' + city

print(cave_man, 'lives in', city)
print(cave_man, 'lives in', city, sep='')
print(cave_man, 'lives in', city, sep='/')
print(cave_man, 'lives in', city, sep='wombat!')



value1 = 5
value2 = 23.39023
value3 = 'Doris'

print(value1, value2, value3)
print()
print(value1)
print(value2)
print(value3)

print(value1, end='How')
print(value2, end='about')
print(value3, end='that?')
print("Done.")

print(value1, end=' ')
print(value2, end=' ')
print(value3, end=' \n')
print("Done.")


print("{} lives in {}".format(cave_man, city))

print(f"{cave_man} lives in {city}")

count = 99

print("I have {} reasons to love Python".format(count))

print("Value is {}".format(value2))
print("Value is {:.2f}".format(value2))
