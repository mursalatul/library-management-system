class FormatVerify:
    def varifyUsernameFormat(self, username: str) -> bool:
        """check username format

        Args:
            username (str): inputed username to check

        Returns:
            bool: True if it is a proper alpha numeric, else False
        """
        # return False if the string is not alpha numeric or underscore
        if len(username) == 0:
            return False 
        for character in list(username.strip()):
            if not character.isalnum() and not character == '_' or character.isupper():
                return False
        return True

    def verifyNameFormat(self, name: str) -> bool:
        """checking if the name only contain string

        Args:
            name (str)

        Returns:
            bool: True if it cantain only string, else False
        """
        if len(name) == 0:
            return False
        for character in list(name.strip()):
            if not character.isalpha():
                return False
        return True
    
    def verifyPasswordFormat(self, password: str) -> bool:
        if len(password) == 0:
            return False
        
        big_letters, small_letters, numbers, spacial_char = 0, 0, 0, 0
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
            elif character.isdigit():
                numbers += 1
            else:
                spacial_char += 1
        
        if big_letters > 0 and small_letters > 0 and numbers > 0 and spacial_char > 0:
            return True
        else:
            return False