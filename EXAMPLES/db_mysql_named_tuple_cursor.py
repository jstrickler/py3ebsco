#!/usr/bin/env python

from contextlib import closing
from collections import namedtuple
import pymysql

def named_tuple_cursor(cursor):
    '''Generate rows as named tuple'''
    column_names = [desc[0] for desc in cursor.description]
    RowTuple = namedtuple('RowTuple', column_names)
    # "RowTuple" is internal name of RowTuple class
    for row in cursor.fetchall():
        yield RowTuple(*row)


with closing(pymysql.connect(
   host="localhost",
   db="python2",
   user="scripts",
   passwd="scripts",
)) as myconn:

    c = myconn.cursor()

    # select first name, last name from all presidents
    num_recs = c.execute('''
        select lastname, firstname
        from presidents
    ''')

    for row in named_tuple_cursor(c):
        print(row.furstname, row.lastname)
