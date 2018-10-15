#!/usr/bin/env python

import psycopg2

DB_HOST = 'localhost'
DB_USER = 'postgres'
DB_PASSWORD = 'scripts'

TABLE_QUERY = '''
    select table_name
    from information_schema.tables
    where table_schema = 'public'
'''

COLUMN_QUERY = '''
    select column_name, data_type, is_nullable, column_default
    from information_schema.columns
    where
        table_name = %s
        and
        table_schema = 'public'
'''


def main(database_name):
    try:
        pgcursor = connect_to_dbserver(database_name)
    except Exception as err:
        print("Unable to connection to {}: {}".format(database_name, err))

    tables = get_all_tables_from_database(pgcursor, database_name)

    for table in tables:
        print(table)
        columns = get_columns_for_table(pgcursor, table, database_name)
        if columns:
            column_data_format = '\t{:15} {:20} {:3} {:10}'
            for col_name, col_type, is_nullable, default_value in columns:
                print(column_data_format.format(col_name, col_type, is_nullable, default_value))


def connect_to_dbserver(database_name):
    try:
        with psycopg2.connect(
           host=DB_HOST,
           dbname=database_name,
           user=DB_USER,
           password=DB_PASSWORD,
        ) as pgconn:
            return pgconn.cursor()
    except Exception as err:
        print(err)
        raise err

def get_all_tables_from_database(pgcursor, database):

    pgcursor.execute(TABLE_QUERY, (database,))

    return [row[0] for row in pgcursor.fetchall()]


def get_columns_for_table(pgcursor, table_name, database_name):

    try:
        pgcursor.execute(COLUMN_QUERY, (table_name,))
    except psycopg2.ProgrammingError as err:
        print("Unable to get columns:", err)
    else:
        return pgcursor.fetchall()


if __name__ == '__main__':
    main('postgres')
