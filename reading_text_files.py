#!/usr/bin/env python

with open('DATA/mary.txt', 'r') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip('\n\r')
        print(line)
print('-' * 60)

my_path = r'C:\Users\pallavi\documents\cats.txt'

my_new_path = my_path.replace('\\', '/')

print(my_new_path)

print('-' * 60)

with open('DATA/mary.txt', 'r') as mary_in:
    contents = mary_in.read()
    print(contents)
print('-' * 60)


with open('DATA/mary.txt', 'r') as mary_in:
    all_lines_with_nl = mary_in.readlines()

print('-' * 60)

with open('DATA/mary.txt', 'r') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]

with open('DATA/mary.txt', 'r') as mary_in:
    all_lines_without_nl = (line.rstrip() for line in mary_in)
