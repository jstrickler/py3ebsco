#!/usr/bin/env python

from contextlib import closing
import pymysql

with closing(
        pymysql.connect(
        host="localhost",
        db="presidents",
        user="scripts",
        passwd="scripts",
    )
) as myconn:
    mycursor = myconn.cursor()

    # select first name, last name from all presidents
    row_count = mycursor.execute('''
        select firstname, lastname
        from presidents
    ''')

    print("{} rows in result set\n".format(row_count))

    for firstname, lastname in mycursor.fetchall():
        print(firstname, lastname)
    print()
