#!/usr/bin/env python

import pymysql

DB = 'information_schema'
DB_HOST = 'localhost'
DB_USER = 'scripts'
DB_PASSWORD = 'scripts'

TABLE_QUERY = '''
    select table_name
    from tables
    where table_schema = %s
'''

COLUMN_QUERY = '''
    select column_name, data_type, is_nullable, column_default
    from columns
    where
        table_name = %s
        and
        table_schema = %s
'''


def main(database_name):
    mycursor = connect_to_dbserver()
    tables = get_all_tables_from_database(mycursor, database_name)
    print('-' * 60)
    for table in tables:
        print(table)
        columns = get_columns_for_table(mycursor, table, database_name)
        column_data_format = '\t{:15} {:12} {:3} {:10}'
        for col_name, col_type, is_nullable, default_value in columns:
            print(column_data_format.format(col_name, col_type, is_nullable, default_value))


def connect_to_dbserver():
    with pymysql.connect(
       host=DB_HOST,
       db=DB,
       user=DB_USER,
       passwd=DB_PASSWORD
    ) as cursor:
        return cursor


def get_all_tables_from_database(mycursor, database):

    mycursor.execute(TABLE_QUERY, (database,))

    return [row[0] for row in mycursor.fetchall()]


def get_columns_for_table(mycursor, table_name, database_name):

    mycursor.execute(COLUMN_QUERY, (table_name, database_name))

    return mycursor.fetchall()


if __name__ == '__main__':
    main('python2')
