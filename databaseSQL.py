import json
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

    # conn = sqlite3.connect(sqlite_file)
# c = conn.cursor()



# From: https://goo.gl/YzypO

# def connect(sqlite_file):
#     """ Make connection to an SQLite database file """
#     conn = sqlite3.connect(sqlite_file)
#     c = conn.cursor()
#     return conn, c

# def close(conn):
#     """ Commit changes and close connection to the database """
#     conn.commit()
#     conn.close()

# def singleton(cls):
#     instances = {}

#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls()
#         return instances[cls]
#     return getinstance()

# class DB(object):
#     """
#     DB driver for the To-Do app - deals with writing entities
#     to the DB and reading entities from the DB
#     """

#     def __init__(self):
#         # TODO Implement this to connect to the database and create tables
#         self.conn = sqlite3.connect('todo.db', check_same_thread=False)
#         self.create_user_table()

    def create_floc_table(self):
        try:
            sqlite_file = 'size_of_flocs'    
            table_name1 = 'sizes'
            size_field = 'size' # name of the column
            date_time_field = 'date_time' #time stamp of the size of the flocs
            field_type = 'INTEGER'  # column data type

            # Creating a new SQLite table with 1 column
            c.execute('CREATE TABLE {tn} ({nf} {ft})'\
                    .format(tn=table_name1, nf=size_field, ft=field_type))

            #following block of code sets the time and date stamp to each new entry of the size of the flocs 
            c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
                     .format(tn=table_name1, cn=date_time_col))
            c.execute("UPDATE {tn} SET {cn}=(CURRENT_TIMESTAMP) WHERE {idf}='some_id1'"\
                     .format(tn=table_name1, idf=id_field, cn=date_time_col))
            
#             self.conn.execute("""
#                 CREATE TABLE flocs (
#                     ID INTEGER PRIMARY KEY,
#                     FLOC COUNT NOT NULL,
#                     FLOC SIZE TIME NOT NULL
#                 )
#             """)
        except Exception as e:
            print(e)
    """ Returns a dictionary with columns as keys
    and the number of not-null entries as associated values.
    """
    def values_in_col(cursor, table_name, print_out=True):
        cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))
        info = cursor.fetchall()
        col_dict = dict()
        for col in info:
            col_dict[col[1]] = 0
        for col in col_dict:
            c.execute('SELECT ({0}) FROM {1} '
                      'WHERE {0} IS NOT NULL'.format(col, table_name))
            # In my case this approach resulted in a
            # better performance than using COUNT
            number_rows = len(c.fetchall())
            col_dict[col] = number_rows
        if print_out:
            print("\nNumber of entries per column:")
            for i in col_dict.items():
                print('{}: {}'.format(i[0], i[1]))
        return col_dict
    
    def add_size(outputOfScript):
        c.execute('INSERT INTO 'sizes' ('size')'
        'VALUES (outputOfScript)
    
#     def get_all_users(self):
#         cursor = self.conn.execute('SELECT * FROM users;')
#         users = []
#         for row in cursor:
#             users.append({'id': row[0], 'name': row[1], 'username': row[2]})
#         return users

#     def create_user(self, name, username):
#         cursor = self.conn.cursor()
#         cursor.execute(
#             'INSERT INTO users (NAME, USERNAME, BALANCE) VALUES (?, ?, ?);', (name, username, 0))
#         self.conn.commit()
#         return cursor.lastrowid

#     def get_user_by_id(self, id):
#         cursor = self.conn.execute(
#             'SELECT * FROM users WHERE ID == ?;', (id, ))
#         for row in cursor:
#             return {'id': row[0], 'name': row[1], 'username': row[2], 'balance': row[3]}

#         return None

#     def delete_user_by_id(self, id):
#         deleted = self.get_user_by_id(id)
#         self.conn.execute('DELETE FROM users WHERE ID == ?;', (id, ))
#         return deleted
    
if __name__ == '__main__':
    sqlite_file = 'flocSizes.sqlite' # this creates the name of the file that will be saved as the first time the function is run
    conn = create_connection(sqlite_file)
    table_name = 'sizes_of_flocs'
    #conn, c = connect(sqlite_file)
    values_in_col(c, table_name, print_out=True)
    #close(conn)
