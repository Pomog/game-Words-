import string
import sqlite3
from user import User

class InputProcessor:
	
	def __init__(self, username):
		self.username = username
		self.create_words_db()
		

	def create_words_db(self):
		self.conn = sqlite3.connect("words_game.db")
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

		# Create the played words table
		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS played_words (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				word TEXT NOT NULL
			)
		''')

		self.conn.commit()
		self.get_words_by_letter("a")

	def input_request(self):
		user_input = input(f"Enter a word, {self.username}: ")
		return self.input_validator(user_input)
	
	def input_validator(self, word):
		starting_letter = word[0]
		self.cursor.execute(f'SELECT COUNT(*) FROM english_words WHERE {starting_letter} = ?', (word,))
		count = self.cursor.fetchone()[0]
		if count == 0:
			raise ValueError(f"{word} is not a valid English word.")
		return self.input_acceptor(word)

	def input_acceptor(self, word):
		starting_letter = word[0]
		self.cursor.execute('SELECT COUNT(*) FROM played_words WHERE word = ?', (word,))
		count = self.cursor.fetchone()[0]
		if count > 0:
			raise ValueError(f"{word} has already been played.")
		self.cursor.execute('INSERT INTO played_words (word) VALUES (?)', (word,))
		self.conn.commit()
		return word

	def get_words_by_letter(self, letter):
		self.cursor.execute(f"SELECT {letter} FROM english_words WHERE {letter} IS NOT NULL")
		words = [row[0] for row in self.cursor.fetchall()]
		print(words)
		# return words
