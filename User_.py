class User:
    """
    A class representing a user.

    Attributes:
        name (str): The name of the user.
        password (str): The password of the user.
        score (int): The score of the user.

    Methods:
        set_name(name: str) -> None:
            Sets the name of the user.
            Args:
                name (str): The name of the user.
            Returns:
                None.

        set_password(password: str) -> None:
            Sets the password of the user.
            Args:
                password (str): The password of the user.
            Returns:
                None.

        set_score(score: int) -> None:
            Sets the score of the user.
            Args:
                score (int): The score of the user.
            Returns:
                None.

        get_name() -> str:
            Returns the name of the user.
            Args:
                None.
            Returns:
                str: The name of the user.

        get_password() -> str:
            Returns the password of the user.
            Args:
                None.
            Returns:
                str: The password of the user.

        get_score() -> int:
            Returns the score of the user.
            Args:
                None.
            Returns:
                int: The score of the user.
    """
    
    def __init__(self, name, password, score):
        self.name = name
        self.password = password
        self.score = score

    def set_name(self, name):
        self.name = name
    
    def set_password(self, password):
        self.password = password
    
    def set_score(self, score):
        self.score = score
    
    def get_name(self):
        return self.name
    
    def get_password(self):
        return self.password
    
    def get_score(self):
        return self.score
