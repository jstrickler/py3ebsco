#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'''spam\n'''


print("It's a gift!")
print('The "gift" is excellent')

query = """
select author, title, isbn
from periodicals
where pid = '1234'
"""

