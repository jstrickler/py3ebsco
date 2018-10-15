#!/usr/bin/env python
#
import shlex

cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'  # <1>

print(cmd.split())  # <2>
print()

print(shlex.split(cmd))  # <3>
