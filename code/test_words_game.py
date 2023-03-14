from unittest.mock import patch
import io
import submitting_words_into_db
import simpleTest

list_words = submitting_words_into_db.w

def test_player_move():
    # Test entering a valid word
    with patch('builtins.input', return_value='apple'):
        with patch('sys.stdout', new=io.StringIO()) as output:
            entered_word, letters = simpleTest.player_move()
            assert entered_word == 'apple'
            assert letters == ['a', 'e']
            assert 'apple |' in output.getvalue()

    # Test entering a word that has already been played
    with patch('builtins.input', return_value='apple'):
        with patch('sys.stdout', new=io.StringIO()) as output:
            simpleTest.played_words = ['apple']
            simpleTest.player_move()
            assert 'already played, type another word' in output.getvalue()

    # Test entering a word that does not exist in the database
    with patch('builtins.input', return_value='xyz'):
        with patch('sys.stdout', new=io.StringIO()) as output:
            simpleTest.player_move()
            assert 'Such word does not exist in our db, try another one' in output.getvalue()

    # Test entering an empty word
    with patch('builtins.input', return_value=''):
        with patch('sys.stdout', new=io.StringIO()) as output:
            simpleTest.player_move()
            assert 'To stop playing, do not enter the word.' in output.getvalue()
