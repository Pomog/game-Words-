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

