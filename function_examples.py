#!/usr/bin/env python

def get_message():
    return "Hello, world"

def print_message():
    msg = get_message()
    print(msg)

print_message()

def double_and_square(n=0):
    return (2 * n) ** 2

print(double_and_square(5))
print(double_and_square(18))
print(double_and_square())

def count_lines_in_file(file_name):
    with open(file_name) as file_in:
        line_count = 0
        for line in file_in:
            line_count += 1
    return line_count

x = count_lines_in_file('DATA/mary.txt')
print(f"mary has {x} lines")

x = count_lines_in_file('DATA/words.txt')
print(f"words has {x} lines")

def count_lines_in_files(*file_names):
    print(file_names)
    line_count = 0
    for file_name in file_names:
        with open(file_name) as file_in:
            for line in file_in:
                line_count += 1
    return line_count

total_count = count_lines_in_files('DATA/mary.txt', 'DATA/alice.txt')
print(f"All files have {total_count} lines")


def spam():
    print("animal is", animal)
    plant = 'giant stinkweed'

animal = 'wombat'

spam()

# print("plant is", plant)


