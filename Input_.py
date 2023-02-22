import sqlite3

class InputProcessor:
    def __init__(self, username):
        self.username = username
        self.conn = None
        self.cursor = None
    
    def create_database(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS english_words (
                starting_letter TEXT,
                ending_letter TEXT
            )
        ''')
        self.conn.commit()
    
    def check_database_exists(self, db_name):
        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM english_words LIMIT 1')
            conn.close()
            return True
        except sqlite3.OperationalError:
            return False
    
    def input_request(self):
        user_input = input(f"Enter a word, {self.username}: ")
        return user_input
    
    def input_validator(self, word):
        starting_letter = word[0]
        ending_letter = word[-1]
        self.cursor.execute('''
            SELECT * FROM english_words
            WHERE starting_letter = ? AND ending_letter = ?
        ''', (starting_letter, ending_letter))
        result = self.cursor.fetchone()
        return result is not None
    
    def input_acceptor(self, word):
        starting_letter = word[0]
        ending_letter = word[-1]
        self.cursor.execute('''
            INSERT INTO english_words (starting_letter, ending_letter)
            VALUES (?, ?)
        ''', (starting_letter, ending_letter))
        self.conn.commit()
