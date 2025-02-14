from workingWithdb.controllers.userController import userController


def main():
    # Initialize the userController with the path to your database
    user_controller = userController("..users.db")

    # Create the table (if not created yet)
    user_controller.userModel.createTable()

    # Insert a single user
    user_controller.insertUser("John Doe", "doejohn@example.com", 30)

    # Insert multiple users
    multipleUsersToInsert = [
        ("John Doe", "john.doe@example.com", 25),
        ("Jane Smith", "jane.smith@example.com", 30),
        ("Robert Brown", "robert.brown@example.com", 28),
        ("Emily Clark", "emily.clark@example.com", 22),
        ("Michael Wilson", "michael.wilson@example.com", 35),
        ("Sophia Johnson", "sophia.johnson@example.com", 29),
        ("James Lee", "james.lee@example.com", 40),
        ("Olivia Davis", "olivia.davis@example.com", 31),
        ("Liam Martinez", "liam.martinez@example.com", 27),
        ("Ava Taylor", "ava.taylor@example.com", 26),
        ("William Anderson", "william.anderson@example.com", 32),
        ("Charlotte Thomas", "charlotte.thomas@example.com", 24),
        ("Daniel Jackson", "daniel.jackson@example.com", 38),
        ("Amelia White", "amelia.white@example.com", 33),
        ("Ethan Harris", "ethan.harris@example.com", 36),
        ("Mia Martin", "mia.martin@example.com", 21),
        ("Lucas Lee", "lucas.lee@example.com", 34),
        ("Harper Robinson", "harper.robinson@example.com", 27),
        ("Benjamin Wright", "benjamin.wright@example.com", 29),
        ("Ella King", "ella.king@example.com", 28)
    ]

    # Insert multiple users into the database
    user_controller.insertMultipleUsers(multipleUsersToInsert)

    # Fetch all users and print them
    allUsersFromDB = user_controller.fetchAllUsers()
    print(f"Users fetched from the database: {allUsersFromDB}")

    # Update a user by ID
    user_controller.updateUser(1, "John Doe", "newemail@example.com", 30)

    # Delete a user by ID
    user_controller.deleteUser(22)


if __name__ == "__main__":
    main()
