import os
import json
import sqlite3

# From: https://goo.gl/YzypO


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance()


class DB(object):
    """
    DB driver for the To-Do app - deals with writing entities
    to the DB and reading entities from the DB
    """

    def __init__(self):
        # TODO Implement this to connect to the database and create tables
        self.conn = sqlite3.connect('todo.db', check_same_thread=False)
        self.create_user_table()

    def create_floc_table(self):
        try:
            self.conn.execute("""
                CREATE TABLE flocs (
                    ID INTEGER PRIMARY KEY,
                    DATE DATE NOT NULL,
                    TIME TIME NOT NULL,
                    SIZE DECIMAL NOT NULL,
                    COUNT INTEGER NOT NULL
                )
            """)
        except Exception as e:
            print(e)

    def get_all_users(self):
        cursor = self.conn.execute('SELECT * FROM users;')
        users = []
        for row in cursor:
            users.append({'id': row[0], 'name': row[1], 'username': row[2]})
        return users

    def create_user(self, name, username):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO users (NAME, USERNAME, BALANCE) VALUES (?, ?, ?);', (name, username, 0))
        self.conn.commit()
        return cursor.lastrowid

    def get_user_by_id(self, id):
        cursor = self.conn.execute(
            'SELECT * FROM users WHERE ID == ?;', (id, ))
        for row in cursor:
            return {'id': row[0], 'name': row[1], 'username': row[2], 'balance': row[3]}

        return None

    def delete_user_by_id(self, id):
        deleted = self.get_user_by_id(id)
        self.conn.execute('DELETE FROM users WHERE ID == ?;', (id, ))
        return deleted

    def send_money(self, sender_id, receiver_id, amount):
        data = {'sender_id': sender_id,
                'receiver_id': receiver_id, 'amount': amount}
        sender_balance = self.get_user_by_id(sender_id)['balance']
        receiver_balance = self.get_user_by_id(receiver_id)['balance']
        if sender_balance - amount < 0:
            return None
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE users SET BALANCE=BALANCE-? WHERE ID==?;', (sender_balance - amount, sender_id))
        cursor.execute(
            'UPDATE users SET BALANCE= BALANCE+? WHERE ID==?;', (receiver_balance - amount, receiver_id))
        self.conn.commit()
        return data
