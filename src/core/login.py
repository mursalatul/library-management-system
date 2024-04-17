import src.core.validation as scv

class Login:
    # username and password format status
    username_password_seems_good = False
    # validation object from src->core->validation to perform all type of checking
    validator = None

    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password
        # initialize the validator
        self.validator = scv.FormatVerify()
        # check if the username and password format is ok
        self.checkFormat()
        if self.username_password_seems_good:
            # decrypt the password
            # check username and password in database
            pass
    
    def checkFormat(self):
        self.username_password_seems_good = self.validator.varifyUsernameFormat(self._username) and self.validator.verifyPasswordFormat(self._password)