#!/usr/bin/env python

users_by_shell = {}
with open("../DATA/passwd") as passwd_in:
    for line in passwd_in:
        (_, _, _, _, _, _, shell) = line.rstrip('\n\r').split(":")
        if shell == "":
            shell = "NONE"

        if shell in users_by_shell:
            users_by_shell[shell] = users_by_shell[shell] + 1
        else:
            users_by_shell[shell] = 1

for shell, count in users_by_shell.items():
    print("{:5d} {}".format(count, shell))
