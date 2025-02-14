from ..models.userModel import userModel
import sqlite3


class userController:
    def __init__(self, dbName):
        self.userModel = userModel(dbName)
        pass

    def insertUser(self, name, email, age):
        """Insert a new user into the database."""
        try:
            conn = self.userModel.dbConnection.connect()
            cursor = conn.cursor()
            cursor.execute("""
            INSERT INTO users (name, email, age)
            VALUES (?, ?, ?);
            """, (name, email, age))
            conn.commit()
            print(f"User {name} inserted successfully!")
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")
        finally:
            self.userModel.dbConnection.close(conn)

    def insertMultipleUsers(self, users):
        """Insert multiple users into the database."""
        try:
            conn = self.userModel.dbConnection.connect()
            cursor = conn.cursor()
            cursor.executemany("""
            INSERT INTO users (name, email, age)
            VALUES (?, ?, ?);
            """, users)
            conn.commit()
            print(f"{len(users)} users inserted successfully!")
        except sqlite3.Error as e:
            print(f"Error inserting users: {e}")
        finally:
            self.userModel.dbConnection.close(conn)

    def fetchAllUsers(self):
        """Fetch all users from the database."""
        try:
            conn = self.userModel.dbConnection.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return users
        except sqlite3.Error as e:
            print(f"Error fetching users: {e}")
            return []
        finally:
            self.userModel.dbConnection.close(conn)

    def updateUser(self, user_id, name, email, age):
        """Update a user's details in the database."""
        try:
            conn = self.userModel.dbConnection.connect()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE users
            SET name = ?, email = ?, age = ? 
            WHERE id = ?;
            """, (name, email, age, user_id))
            conn.commit()

            print(f"User with ID {user_id} updated successfully!")
        except sqlite3.Error as e:
            print(f"Error updating user: {e}")
        finally:
            self.userModel.dbConnection.close(conn)

    def deleteUser(self, user_id):
        """Delete a user from the database."""
        try:
            conn = self.userModel.dbConnection.connect()
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM users
            WHERE id = ?;
            """, (user_id,))
            conn.commit()
            print(f"User with ID {user_id} deleted successfully!")
        except sqlite3.Error as e:
            print(f"Error deleting user: {e}")
        finally:
            self.userModel.dbConnection.close(conn)


'''CRUD operations before crteating the main file'''

# # If this script is being run directly
# if __name__ == "__main__":
#     user_controller = userController("..users.db")

#     # Create the table (if not created yet)
#     user_controller.userModel.createTable()

#     # Insert a single user
#     user_controller.insertUser("John Doe", "doejohn@example.com", 30)

#     # Insert multiple users
#     multipleUsersToInsert = [
#         ("John Doe", "john.doe@example.com", 25),
#         ("Jane Smith", "jane.smith@example.com", 30),
#         ("Robert Brown", "robert.brown@example.com", 28),
#         ("Emily Clark", "emily.clark@example.com", 22),
#         ("Michael Wilson", "michael.wilson@example.com", 35),
#         ("Sophia Johnson", "sophia.johnson@example.com", 29),
#         ("James Lee", "james.lee@example.com", 40),
#         ("Olivia Davis", "olivia.davis@example.com", 31),
#         ("Liam Martinez", "liam.martinez@example.com", 27),
#         ("Ava Taylor", "ava.taylor@example.com", 26),
#         ("William Anderson", "william.anderson@example.com", 32),
#         ("Charlotte Thomas", "charlotte.thomas@example.com", 24),
#         ("Daniel Jackson", "daniel.jackson@example.com", 38),
#         ("Amelia White", "amelia.white@example.com", 33),
#         ("Ethan Harris", "ethan.harris@example.com", 36),
#         ("Mia Martin", "mia.martin@example.com", 21),
#         ("Lucas Lee", "lucas.lee@example.com", 34),
#         ("Harper Robinson", "harper.robinson@example.com", 27),
#         ("Benjamin Wright", "benjamin.wright@example.com", 29),
#         ("Ella King", "ella.king@example.com", 28)
#     ]

#     user_controller.insertMultipleUsers(multipleUsersToInsert)

#     # fetch all users
#     allUsersFromDB = user_controller.fetchAllUsers()
#     print(f"Users fetched from the database: {allUsersFromDB}")

#     # Update a user by ID
#     updatedUser = user_controller.updateUser(
#         1, "John Doe", "newemail@example.com", 30)

#     # Delete a user by ID
#     user_controller.deleteUser(22)
