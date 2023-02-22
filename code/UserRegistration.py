import sqlite3

class UserRegistration:
    """
    A class representing user registration.

    Attributes:
        None.

    Methods:
        input_request() -> dict:
            Requests input from the user for name and password.
            Args:
                None.
            Returns:
                dict: A dictionary containing the name and password entered by the user.

        input_validator(data: dict, db_name: str) -> bool:
            Validates the user input against the database.
            Args:
                data (dict): A dictionary containing the name and password entered by the user.
                db_name (str): The name of the database to use for validation.
            Returns:
                bool: True if the input is valid, False otherwise.

        database_update(data: dict, db_name: str) -> None:
            Updates the database with the user's name and password.
            Args:
                data (dict): A dictionary containing the name and password entered by the user.
                db_name (str): The name of the database to update.
            Returns:
                None.
    """

    def __init__(self):
        # Create a database connection
        self.conn = sqlite3.connect('user_database.db')
        self.cursor = self.conn.cursor()

        # Create a table to store user information if it doesn't exist already
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT,
                                 password TEXT)''')

        # Commit the changes to the database
        self.conn.commit()

    def input_request(self):
        """
        Prompts the user to enter a name and password, validates the input, and returns a dictionary containing the name and password.

        Args:
        - None

        Returns:
        - A dictionary containing the name and password entered by the user.
        """
        while True:
            name = input("Enter your name: ")
            if len(name) < 5 or not name.isalnum() or not name[-1].isdigit():
                print("Invalid name! Name must be at least 5 characters long, consist of letters and digits only, and end with a digit.")
                continue

            password = input("Enter your password: ")
            if len(password) < 6 or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
                print("Invalid password! Password must be at least 6 characters long, contain at least one uppercase letter and one digit.")
                continue

            return {"name": name, "password": password}


    def input_validator(self, data):
        # Check if the username is already in the database
        self.cursor.execute(f"SELECT name FROM users WHERE name='{data['name']}'")
        result = self.cursor.fetchone()
        if result:
            print("Username already exists.")
            return False
        return True

    def database_update(self, data):
        # Insert the user's information into the database
        self.cursor.execute(f"INSERT INTO users (name, password) VALUES ('{data['name']}', '{data['password']}')")
        self.conn.commit()
