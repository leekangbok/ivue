import os
import sqlite3
import sys
from itertools import dropwhile

from .. import DBBase


class DBSQLite3(DBBase):
    def __init__(self):
        self.db = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'storage', 'data.db')

    def get_all_column_name(self, tablename):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('select * from {} limit 0'.format(tablename))
        for e in cursor.description:
            yield e[0]
        conn.close()

    def get_column_name(self, tablename):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('select * from {} limit 0'.format(tablename))
        for _, e in dropwhile(lambda i: i[0] < 3, enumerate(cursor.description)):
            yield e[0]
        conn.close()

    def create_table(self, statement):
        print(statement)
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        conn.close()

    def run_operation(self, statement, *args):
        print(statement, *args)
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(statement, *args)
        conn.commit()
        conn.close()

    def run_fetch(self, statement, callback):
        print(statement)
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(statement)
        rows = cursor.fetchall()
        callback(rows)
        conn.close()
        return rows
