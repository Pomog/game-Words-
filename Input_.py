import string
import sqlite3


class InputProcessor:
	"""
	A class for processing user input and storing English words separated by initial letter into columns of a SQLite database.

	Attributes:
		username (str): The username of the user.
		conn (sqlite3.Connection): The connection to the SQLite database.
		cursor (sqlite3.Cursor): The cursor used to execute SQLite commands.

	Methods:
		create_database(db_name: str) -> None:
			Creates a new SQLite database with columns for each letter of the alphabet, if it doesn't already exist.
			Args:
				db_name (str): The name of the database to create.
			Returns:
				None.

		input_request() -> str:
			Prompts the user to enter a word and returns the user's input.
			Args:
				None.
			Returns:
				str: The user's input.

		input_validator(word: str) -> bool:
			Validates a word against the English words database.
			Args:
				word (str): The word to validate.
			Returns:
				bool: True if the word is valid, False otherwise.

		input_acceptor(word: str) -> None:
			Accepts a word into the English words database.
			Args:
				word (str): The word to accept.
			Returns:
				None.
	"""
	
	def __init__(self, username):
		self.username = username
		self.conn = None
		self.cursor = None
		

	def create_database(self, db_name):
		self.conn = sqlite3.connect(db_name)
		self.cursor = self.conn.cursor()

		# Create a column for each letter of the alphabet
		alphabet = string.ascii_lowercase
		columns = ', '.join([f'{letter} TEXT' for letter in alphabet])
		
		# Create the English words table with columns for each letter
		self.cursor.execute(f'''
			CREATE TABLE IF NOT EXISTS english_words (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				{columns}
			)
		''')
		self.conn.commit()

	def input_request(self):
		user_input = input(f"Enter a word, {self.username}: ")
		return user_input
	
	def input_validator(self, word):
		starting_letter = word[0]
		self.cursor.execute(f'SELECT {starting_letter} FROM english_words')
		words = self.cursor.fetchone()
		return word in words
	
	def input_acceptor(self, word):
		starting_letter = word[0]
		self.cursor.execute(f'''
			INSERT INTO english_words ({starting_letter})
			VALUES (?)
		''', (word,))
		self.conn.commit()

	def get_words_by_letter(self, letter):
		self.cursor.execute(f"SELECT {letter} FROM english_words WHERE {letter} IS NOT NULL")
		words = [row[0] for row in self.cursor.fetchall()]
		return words
