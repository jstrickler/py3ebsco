#!/usr/bin/python

from random import choice
from datetime import date
import sqlite3

candidate_info =  (
    46, 'Nader', 'Ralph', date(2017,1,20), date(2021,1,19),
    'Winstead', 'Connecticut',
    date(1934,2,27), None, 'Independent'
)

with sqlite3.connect("../DATA/presidents.db") as conn:

    c = conn.cursor()

    insert_stmt = '''
       INSERT INTO presidents
    (termnum, lastname, firstname, termstart, termend,
     birthplace, birthstate, birthdate, deathdate, party)
         VALUES
        (?, ?, ?, ?, ?,
         ?, ?, ?, ?, ?);
    '''

    try:
        rows = c.execute(insert_stmt, candidate_info)
    except Exception as e:
        print("Error inserting record:", e)
        conn.rollback()
    else:
        print("Record inserted OK.")
        conn.commit()
