#!/usr/bin/env python

name = input("Enter a full name: ")

print("name: ", name)
print("upper: ", name.upper())
print("lower: ", name.lower())
print("title: ", name.title())

# other string methods
print("starts with 'B'", name.lower().startswith('b'))
print("capital: ", name.capitalize())
print("space replaced with X", name.replace(' ', 'X'))
