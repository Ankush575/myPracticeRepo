# python piece of code to create a database.
import sqlite3


class databaseConnection:
    def __init__(self, dbName):
        self.dbName = dbName

    def connect(self):
        """Establish and return a database connection."""
        return sqlite3.connect(self.dbName)

    def close(self, conn):
        """Close the database connection."""
        conn.close()


databaseConnection('users.db').connect()
