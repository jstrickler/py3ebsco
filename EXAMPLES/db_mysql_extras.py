#!/usr/bin/env python

import pymysql
import pymysql.cursors

myconn = pymysql.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts",
   cursorclass = pymysql.cursors.DictCursor
)

# c = myconn.cursor(pymysql.cursors.DictCursor) 
c = myconn.cursor()

# select first name, last name from all presidents
num_recs = c.execute('''
    select lname, fname
    from presidents
''')

print(c.description)

for row in c.fetchall():
    print(row['fname'], row['lname'])
print()

c.execute('''
    select * from presidents where num = %s
''', (16,))

row = c.fetchone()
print(row)
print('-' * 50)

# call a stored proc two different ways

cur = myconn.cursor(pymysql.cursors.Cursor)

cur.execute('call pres_full_name(16)')
print(cur.fetchone())
cur.close()

cur = myconn.cursor(pymysql.cursors.Cursor)
cur.callproc('pres_full_name', (16,))
print(cur.fetchone())

cur.close()

x = get_arrays()

try:
    cur.execute('first sql update')
    cur.execute('first sql update')
except pymysql.DatabaseError as err:
    print("OH NO!", err)
    myconn.rollback()
except TypeError as err:
    print(err)
else:
    myconn.commit()
