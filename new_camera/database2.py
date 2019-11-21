import json
import sqlite3
from sqlite3 import Error
import cv2
import count_and_size


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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def expToCSV(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM flocs")
    table = c.fetchall()
    print(table)

    # to export as csv file
    with open("wub.csv", "w") as write_file:
        cursor = conn.cursor()
        for row in cursor.execute("SELECT * FROM flocs"):
            writeRow = " ".join(str(x) for x in row)
            write_file.write(writeRow)


def add_flocs(img, cur):
    sql = ''' INSERT INTO flocs (size)
              VALUES(?) '''
    for size in count_and_size.count_and_size_flocs(img):
        print(size)
        cur.execute(sql, (size, ))


def get_all_flocs(cur):
    sql = """ SELECT * from flocs """
    data = cur.execute(sql)
    for cell in data:
        print(cell)


def get_floc_from_id(cur, id):
    sql = """SELECT * FROM flocs WHERE id=?"""
    cur.execute(sql, (id,))
    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    sql_create_floc_table = """ CREATE TABLE IF NOT EXISTS flocs (
                                        id integer PRIMARY KEY,
                                        size integer NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)
    conn.commit()

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_floc_table)

    else:
        print("Error! cannot create the database connection.")

    img = cv2.imread("openCV/flocs/Image 32339.jpg")
    cur = conn.cursor()
    add_flocs(img, cur)
    print("get floc with id of 40: \n" + str(get_floc_from_id(cur, 40)))
    print("get all flocs: " + str(get_all_flocs(cur)))
    conn.close()


if __name__ == '__main__':
    main()
