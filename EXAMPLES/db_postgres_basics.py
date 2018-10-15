#!/usr/bin/env python

import sys
import psycopg2

pgconn = psycopg2.connect(
   host="localhost",
   dbname="postgres",
   user="postgres",
   password='scripts',
)
pgcursor = pgconn.cursor()

# select first name, last name from all presidents
pgcursor.execute('''
    select firstname, lastname from presidents
''')

print("{} rows in result set\n".format(pgcursor.rowcount))

for row in pgcursor.fetchall():
    print(' '.join(row))
print()

