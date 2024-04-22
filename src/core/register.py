from src.core.validation import FormatVerify

class Register:
    registerDateStatus = {
        "firstname": False,
        "lastname": False,
        "username": False,
        "password": False,
        "libraryid": False
    }
    
    # we have seperated this key cause we will perform different opetions on it
    libraryid = False

    def __init__(self, firstname, lastname, username, libraryid, password) -> None:
        """
        NOTE
            here all the attributes are pyqt5.qtwidgets.lineedit object
            to access its text use .text() member method with it. we decided
            to work with directly with the object to perform operation on the
            lineEdit object from this class. this way registerui.RegisterUI._registerButtonClicked
            method will be less populated
        """
        self.registerDate = {}
        # Populate the dictionary
        self.registerDate["firstname"] = firstname
        self.registerDate["lastname"] = lastname
        self.registerDate["username"] = username
        self.registerDate["libraryid"] = libraryid
        self.registerDate["password"] = password

        # checking the format
        self._checkFormat()
        self._checkLibraryId()
        self._markBorder()

    def _checkFormat(self):
        f = FormatVerify()
        self.registerDateStatus["firstname"] = f.verifyNameFormat(self.registerDate["firstname"].text())
        self.registerDateStatus["lastname"] = f.verifyNameFormat(self.registerDate["lastname"].text())
        self.registerDateStatus["username"] = f.varifyUsernameFormat(self.registerDate["username"].text())
        self.registerDateStatus["password"] = f.verifyPasswordFormat(self.registerDate["password"].text())
        # print(self.registerDateStatus["password"], self.registerDate["password"].text())

    def _checkLibraryId(self):
        # for now we are considering the entered library id is ok.
        self.registerDateStatus["libraryid"] = True
    
    def _markBorder(self):
        for key, status in self.registerDateStatus.items():
            if status:
                self.registerDate[key].setStyleSheet("")
            else:
                self.registerDate[key].setStyleSheet("border: 2px solid red;")
