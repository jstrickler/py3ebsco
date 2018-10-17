#!/usr/bin/env python

# set max/min
max_value = 26
min_value = 0

# while "forever"
while True:
#     calculate guess as avg of max/min
    guess = (max_value + min_value) // 2
#     ask user if guess is their #
    response = input(f"Is {guess} your number? (h, l, or y) ")

#     if input is "h"
    if response == 'h':
        max_value = guess
    elif response == 'l':
        min_value = guess
    elif response == 'y':
        print("Found it!")
        break
    else:
        print("h, l, or y only, please")
        continue
#        set max to guess
#     if input is "l"
#        set min to guess
#     if input is "y"
#        quit

