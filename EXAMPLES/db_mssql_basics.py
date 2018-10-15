#!/usr/bin/env python

import pymssql

conn = pymssql.connect(
        host="host",
        db="database",
        user="username",
        passwd="l0lz"
)

cursor = conn.cursor()

# select first name, last name from all presidents
row_count = cursor.execute('''
    select lname, fname
    from presidents
''')

print("{} rows in result set\n".format(row_count))

for row in cursor.fetchall():
    print(' '.join(row))
print()

# cursor.fetchone() and cursor.fetchmany() are also available

