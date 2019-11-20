import os
import sqlite3

from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv('DB_NAME')

print(db_name)
con = sqlite3.connect(db_name)


class QueryModel:
    def __init__(self):
        query_str = "CREATE TABLE IF NOT EXISTS query (" \
                    "id integer PRIMARY KEY AUTOINCREMENT," \
                    "name VARCHAR(100))"
        con.execute(query_str)

    def filter_name(self, query):
        cursorObj = con.cursor()
        cursorObj.execute("SELECT name FROM query where name like ?", ("%" + str(query) + "%",))
        rows = cursorObj.fetchall()
        return rows

    def insert_data(self, query_list):
        con.execute('BEGIN TRANSACTION')
        for query in query_list:
            cols = ",".join(query.keys())
            values = ",".join(query.values())
            con.execute('INSERT OR REPLACE INTO query (name) VALUES (?)', (values,))
        con.execute('COMMIT')


QMODELOBJECT = QueryModel()

