import submitting_words_into_db
import random

list_words = submitting_words_into_db.w
print(list_words)

played_words = []

end_game = False


def player_move():
    print("To stop playing, do not enter the word.")
    entered_word = input("Enter your word:  ")
    if entered_word == '':
        exit()
    entered_word = entered_word.lower()

    if entered_word not in played_words:
        if entered_word in list_words:
            if len(played_words):
                last_word = played_words[-1]
                last_letter = last_word[-1]
                if entered_word[0] == last_letter:
                    played_words.append(entered_word)
                    letters = [entered_word[0], entered_word[-1]]
                    print(entered_word, '|')
                    return entered_word, letters
                else:
                    print(f"The word should start with letter: {last_letter}")
                    player_move()
            else:
                played_words.append(entered_word)
                letters = [entered_word[0], entered_word[-1]]
                print(entered_word, '|')
        else:
            print("Such word does not exist in our db, try another one...")
            player_move()
    else:
        print("already played, type another word")
        player_move()


def pc_move():
    last_word = played_words[-1]
    last_letter = last_word[-1]
    for w in list_words:
        if w[0] == last_letter[-1]:
            if w not in played_words:
                played_words.append(w)
                print(w, '|')
                return w


while not end_game:
    player_move()
    pc_move()
