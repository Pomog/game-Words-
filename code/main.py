from inputProcessor import InputProcessor
from userRegistration import UserRegistration
from login import Login
import submitting_words_into_db
import random



log_in_check=False
while not log_in_check:
    new_game=Login()
    log_in=new_game.input_request()
    log_in_valid=new_game.input_validator(log_in)
    player1_name=log_in
    if not log_in_valid:
        ask1=input("Would you like to register a new user - Y/N: ")
        if ask1.lower()=="y":
            new_user_reg=UserRegistration()
            login_new_user=new_user_reg.input_request()
            login_new_user_valid=new_user_reg.input_validator(login_new_user)
            if login_new_user_valid:
                new_user_reg.database_update(login_new_user)
                player1_name=log_in
                log_in_check=True
        else:
            ask2=input("Try to log in again or quit - Y/N: ")
            if ask2.lower()=="n":
                print("ok, bye bye!")
                log_in_check=True
    else:
        log_in_check=True


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
