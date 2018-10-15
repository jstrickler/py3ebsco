#!/usr/bin/env python

from spam import eggs, toast

eggs("fried")
toast("butter", "strawberry jam")

print()
print("What does eggs() do?")
print(eggs.__doc__)
print()
print("What does toast() do?")
print(toast.__doc__)
