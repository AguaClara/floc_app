import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :return:
    """
    try:
        c = conn.cursor()
        command = """
        CREATE TABLE IF NOT EXISTS sizes (
            id integer PRIMARY KEY,
            size decimal,
            count integer,
            date_time datetime_interval_code,
        ) 
        """
        c.execute(command)
    except Error as e:
        print(e)


def main():
    database='flocSizes.sqlite'
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create projects table
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

