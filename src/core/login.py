import src.core.validation as scv

class Login:
    # username and password format status
    usernameOk = False
    passowordOk = False

    # validation object from src->core->validation to perform all type of checking
    validator = None

    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password
        # initialize the validator
        self.validator = scv.FormatVerify()
        # check if the username and password format is ok
        self._checkFormat()
        # if self.username_password_seems_good:
        #     # decrypt the password
        #     # check username and password in database
        #     pass
    
    def _checkFormat(self):
        self.usernameOk = self.validator.varifyUsernameFormat(self._username)
        self.passowordOk = self.validator.verifyPasswordFormat(self._password)
    
    def isGoodFormated(self):
        return self.usernameOk and self.passowordOk