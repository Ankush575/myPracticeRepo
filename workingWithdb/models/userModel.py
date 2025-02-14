

from ..databases.userDB import databaseConnection
import sqlite3


class userModel:
    def __init__(self, dbName):
        self.dbName = dbName
        self.dbConnection = databaseConnection(dbName)

    def createTable(self):
        """Create the users table if it doesn't exist."""
        try:
            conn = self.dbConnection.connect()
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                age INTEGER
            );
            """)
            conn.commit()
            print("Table created successfully (if it didn't exist already).")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            self.dbConnection.close(conn)


userModel('users.db').createTable()
