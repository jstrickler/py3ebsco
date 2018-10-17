#!/usr/bin/env python

john_countries = """
Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel
""".split()

clare_countries = """
BVI
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada
""".split()


john = set(john_countries)
clare = set(clare_countries)

print("Both:", john & clare)
print("Just one:", john ^ clare)
print("Either:", john | clare)
print("Just Clare:", clare - john)
print("Just John:", john - clare)

print(set('Mississippi'))
