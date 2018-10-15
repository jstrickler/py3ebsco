#!/usr/bin/env python

import sys

max_value = 26
if len(sys.argv) > 1:
    max_value = int(sys.argv[1]) + 1

min_value = 0
tries = 0

while True:
    guess = (max_value + min_value) // 2
    answer = input("Is {} your number? ".format(guess))

    if answer == "q":
        break

    tries = tries + 1

    if answer == "h":
        max_value = guess
    elif answer == "l":
        min_value = guess
    elif answer == "y":
        print("I got it in {} try(ies)!".format(tries))
        break
    else:
        print("Please enter h, l, or y")


