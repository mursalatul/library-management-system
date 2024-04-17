class FormatVerify:
    def varifyUsernameFormat(self, username: str) -> bool:
        """check username format

        Args:
            username (str): inputed username to check

        Returns:
            bool: True if it is a proper alpha numeric, else False
        """
        # return False if the string is not alpha numeric or underscore
        for character in list(username.strip()):
            if not character.isalnum() and character == '_':
                return False
        return True
    
    def verifyNameFormat(self, name: str) -> bool:
        """checking if the name only contain string

        Args:
            name (str)

        Returns:
            bool: True if it cantain only string, else False
        """
        for character in list(name.strip()):
            if not character.isalpha():
                return False
        return True
    
    def verifyPasswordFormat(self, password: str) -> bool:
        big_letters, small_letters, numbers = 0
        password = password.strip()

        # return false if password contain inner space
        if ' ' in password:
            return False

        # getting the indivituals 
        for character in list(password):
            if character.isalpha():
                if character.isupper():
                    big_letters += 1
                else:
                    small_letters += 1
            else:
                numbers += 1
        
        if big_letters > 1 and small_letters > 1 and numbers > 1:
            return True
        else:
            return False