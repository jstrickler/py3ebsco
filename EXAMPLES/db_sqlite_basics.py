#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/presidents.db") as s3conn: # <1>

    s3cursor = s3conn.cursor()  # <2>

    # select first name, last name from all presidents
    s3cursor.execute('''
        select firstname, lastname
        from presidents
    ''')  # <3>

    print("Sqlite3 does not provide a row count\n")  # <4>
    
    for row in s3cursor.fetchall():  # <5>
        print(' '.join(row))  # <6>
