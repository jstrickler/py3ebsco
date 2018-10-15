#!/usr/bin/env python

import sqlite3

with sqlite3.connect("../DATA/presidents.db") as s3conn:

    s3cursor = s3conn.cursor()

    party_query = '''
    select firstname, lastname
    from presidents
        where party = ?
    '''   # <1>

    for party in 'Federalist', 'Whig':
        print(party)
        s3cursor.execute(party_query, (party,))  # <2>
        print(s3cursor.fetchall())
        print()

