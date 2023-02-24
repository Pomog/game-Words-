from inputProcessor import InputProcessor
from userRegistration import UserRegistration
from login import Login

log_in_success=False

while not log_in_success:
    new_game=Login()
    log_in=new_game.input_request()

    log_valid=new_game.input_validator(log_in)

    if not log_valid:
        print("Register new user:")
        new_user=UserRegistration()
        register_new_user=new_user.input_request()   

    else:
        log_in_success=True

print("You are in, let's play a game...")
print("under development.... Stay put! Will be done soon, right Yurii????")


# new_input=InputProcessor()
# test of pulling

