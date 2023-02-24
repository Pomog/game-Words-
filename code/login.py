import sqlite3


class Login:
    def __init__(self):
        self.conn = sqlite3.connect("user_database.db")
        self.cursor = self.conn.cursor()
        self.check_all_users()

    def __del__(self):
        self.conn.close()

    def input_request(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        return {"name": name, "password": password}

    def input_validator(self, user_data):
        self.cursor.execute("SELECT * FROM users WHERE name=?", (user_data["name"],))
        user = self.cursor.fetchone()
        if user is None:
            print("User not found.")
            return False
        elif user[2] != user_data["password"]:
            print("Incorrect password.")
            return False
        else:
            print("Login successful.")
            return True
    def check_all_users(self):
        print("LIST of ALL REGISTERED USERS:")
        self.cursor.execute("SELECT * from users")
        data=self.cursor.fetchall()

        for i in data:
            print(i)

