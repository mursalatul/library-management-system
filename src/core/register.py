from src.core.database import Database
from src.core.validation import FormatVerify
from src.ui.popupui import MessageBox
from data.Message_data import Message


class Register:
    registerDataStatus = {
        "firstname": False,
        "lastname": False,
        "username": False,
        "password": False,
        "retyped_password": False,
        "libraryid": False,
    }

    readyForRegister = False

    # we have seperated this key cause we will perform different opetions on it
    libraryid = False

    def __init__(
        self, firstname, lastname, username, libraryid, password, retyped_password
    ) -> None:
        """
        NOTE
            here all the attributes are pyqt5.qtwidgets.lineedit object
            to access its text use .text() member method with it. we decided
            to work with directly with the object to perform operation on the
            lineEdit object from this class. this way registerui.RegisterUI._registerButtonClicked
            method will be less populated
        """
        self.registerData = {}
        # Populate the dictionary
        self.registerData["firstname"] = firstname
        self.registerData["lastname"] = lastname
        self.registerData["username"] = username
        self.registerData["libraryid"] = libraryid
        self.registerData["password"] = password
        self.registerData["retyped_password"] = retyped_password

        # checking the format
        self._matchPassword()
        self._checkFormat()
        self._checkLibraryId()
        self._markBorder()

        if self._isGoodFormated():
            self._checkDataInDatabase()
            if self.readyForRegister:
                # store the register information
                # show done message
                self._showAMessage(Message["register"]["status"])


    def _existingDataFound(self):
        """"show message for existing data found and mark the box"""
        msg_box = MessageBox()
        if not self.registerDataStatus["libraryid"]:
            msg_box.showMessage(Message["register"]["existing_data"]["libraryid"])
        if not self.registerDataStatus["username"]:
            msg_box.showMessage(Message["register"]["existing_data"]["username"])

        # mark the libraryid box
        self._markABox("libraryid", self.registerDataStatus["libraryid"])
        # mark the username box
        self._markABox("username", self.registerDataStatus["username"])


    def _checkDataInDatabase(self):
        db = Database()
        """
        check username and library id in the login table
        """
        self.registerDataStatus["libraryid"] = not db.isDataPresent(
            table_name="login",
            column_name="libraryid",
            data=self.registerData["libraryid"].text(),
        )
        self.registerDataStatus["username"] = not db.isDataPresent(
            table_name="login",
            column_name="username",
            data=self.registerData["username"].text(),
        )
        if not self.registerDataStatus["libraryid"] or not self.registerDataStatus["username"]:
            # show message and mark box
            self._existingDataFound()
        else:
            # set readyForRegister true, and begin registration process
            self.readyForRegister = True

    def _isGoodFormated(self):
        for key, value in self.registerDataStatus.items():
            if not value:
                return False
        return True

    def _matchPassword(self):
        if (
            self.registerData["password"].text()
            != self.registerData["retyped_password"].text()
        ):
            msg_box = MessageBox()
            msg_box.showMessage(Message["register"]["password_match_error"])

    def _checkFormat(self):
        f = FormatVerify()
        self.registerDataStatus["firstname"] = f.verifyNameFormat(
            self.registerData["firstname"].text()
        )
        self.registerDataStatus["lastname"] = f.verifyNameFormat(
            self.registerData["lastname"].text()
        )
        self.registerDataStatus["username"] = f.varifyUsernameFormat(
            self.registerData["username"].text()
        )
        self.registerDataStatus["password"] = f.verifyPasswordFormat(
            self.registerData["password"].text()
        )
        self.registerDataStatus["retyped_password"] = f.verifyPasswordFormat(
            self.registerData["retyped_password"].text()
        )
        # print(self.registerDataStatus["password"], self.registerData["password"].text())

    def _checkLibraryId(self):
        # for now we are considering the entered library id is ok.
        # this id will be given by the librarian
        self.registerDataStatus["libraryid"] = True

    def _markBorder(self):
        for key, status in self.registerDataStatus.items():
            if status:
                self.registerData[key].setStyleSheet("")
            else:
                self.registerData[key].setStyleSheet("border: 2px solid red;")
                if key == "firstname" or key == "lastname":
                    key = "name"
                elif key == "retyped_password":
                    key = "password"
                self._showWrongFormatPopupMessage(key)

    def _showWrongFormatPopupMessage(self, element_name):
        msg_box = MessageBox()
        msg_box.showMessage(Message["register"]["format_message"][element_name])
    
    def _markABox(self, element, status):
        if status:
            self.registerData[element].setStyleSheet("")
        else:
            self.registerData[element].setStyleSheet("border: 2px solid red;")
    
    def _showAMessage(self, msg):
        msg_box = MessageBox()
        msg_box.showMessage(msg)