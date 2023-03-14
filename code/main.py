from inputProcessor import InputProcessor
from userRegistration import UserRegistration
from login import Login

player1_score=0
player1_name=""
player2_score=0

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


game_over=False



while not game_over:
    player1=InputProcessor(player1_name["name"])


    



# stop_playing=False

# while not stop_playing:
#     new_word=new_input.input_request()    
#     stop_playing=True