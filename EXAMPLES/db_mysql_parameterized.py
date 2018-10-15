#!/usr/bin/env python

import sys
from contextlib import closing

import pymysql


with closing(pymysql.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts"
)) as myconn:

    mycursor = myconn.cursor()

    for party_name in 'Whig', 'Federalist':
        print(party_name.upper() + ':')

        mycursor.execute('''
        select lname, fname
        from presidents
        where party = :party
        ''', party=party_name)

        print(mycursor.fetchall())
        print()
        print(mycursor.description)

        # for row in mycursor.fetchall():
        #     print(row)
        # print('-' * 60)
