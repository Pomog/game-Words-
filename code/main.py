from Input_ import InputProcessor
from UserRegistration import UserRegistration

new_user=UserRegistration()
register=new_user.input_request()
if register:
    new_user.database_update(register)
check=new_user.input_validator(register)


# new_input=InputProcessor()

