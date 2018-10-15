#!/usr/bin/env python

import sys
import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
   host="localhost",
   dbname="postgres",
   user="postgres",
   password='scripts',
)

c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

c.execute('''
    select * from presidents where termnum = %s
''', (26,))

row = c.fetchone()
print(row['firstname'], row['lastname'])

print('{0[firstname]} {0[lastname]} is a {0[party]}'.format(row))
