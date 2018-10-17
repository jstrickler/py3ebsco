#!/usr/bin/env python

while True:
    show_name = input("Enter name of show: ")
    if show_name == 'q':
        break
    if show_name == '':
        continue

    raw_num_tickets = input("Number of tickets: ")
    if raw_num_tickets == '':
        continue
    num_tickets = int(raw_num_tickets)

    print("OK: {} tickets for {}".format(num_tickets, show_name))


