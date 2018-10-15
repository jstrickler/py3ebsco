#!/usr/bin/python
import pymysql

candidate = (
    'Nader', 'Ralph', 'Winstead', 'Connecticut', '1934-02-27', 'Independent'
)

myconn = pymysql.connect(
    host="localhost",
    db="python2",
    user="scripts",
    passwd="scripts"
)

c = myconn.cursor()

insert_stmt = '''
   INSERT INTO presidents
    (termnum, lastname, firstname, termstart, termend,
     birthplace, birthstate, birthdate, deathdate, party)
     VALUES
    (45, %s, %s, '2012-01-20', '2016-01-20',
     %s, %s, %s, NULL, %s);
'''

rows = c.execute(insert_stmt, candidate)

if rows == 1:
    print("Record inserted OK.")
    myconn.commit()
else:
    print("Error inserting record:")
