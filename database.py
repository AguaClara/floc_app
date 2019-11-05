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


def create_table(table_name):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :return:
    """
    return """
        CREATE TABLE IF NOT EXISTS flocs (
            id integer PRIMARY KEY,
            size decimal,
            count integer,
            time TIMESTAMP
        ) 
        """


def create_floc(size, count):
    return """
    INSERT INTO flocs(id, size, count, time)
    """


def execute(command, conn):
    try:
        c = conn.cursor()
        c.execute(command)
    except Error as e:
        print(e)


def main():
    database = 'flocSizes.sqlite'
    conn = create_connection(database)
    # create tables
    if conn is not None:
        # create projects table
        execute(create_table("Flocs"), conn)
        execute(create_floc(5, 3), conn)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
