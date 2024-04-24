from src.core.validation import FormatVerify
from data.Message_data import Message
from src.ui.popupui import MessageBox
from src.core.database import Database

from data.database_info import database_credentials

class Login:
    # username and password format status
    login_data_status = {"username": False, "password": False}

    def __init__(self, username, password) -> None:
        self.login_data = {}
        self.login_data["username"] = username
        self.login_data["password"] = password
        self._username = username
        self._password = password

        # check if the username and password format is ok
        self._checkFormat()
        self._markBorder()  # border will be marked only if there is a wrong formatted username or/and password

        # check in the database if username and password well formatted
        if self._isGoodFormated():
            self._checkDataInDatabase()

    def _checkDataInDatabase(self):
        db = Database()
        # now login_data_status will store the status
        # of if the username and password combo is
        # present in the database or not
        status = db.isUsernamePasswodPresent(
            self.login_data["username"].text(), self.login_data["password"].text()
        )
        self.login_data_status["username"] = status
        self.login_data_status["password"] = status

        if status:
            # username and password found
            self._showUsernamePasswordFoundStatusPopupMessage(Message["login"]["in_database"]["found"])
        else:
            # username and password not found

            self._showUsernamePasswordFoundStatusPopupMessage(Message["login"]["in_database"]["not_found"])

    def _checkFormat(self):
        f = FormatVerify()
        self.login_data_status["username"] = f.varifyUsernameFormat(
            self.login_data["username"].text()
        )
        self.login_data_status["password"] = f.verifyPasswordFormat(
            self.login_data["password"].text()
        )

    def _isGoodFormated(self):
        return self.login_data_status["username"] and self.login_data_status["password"]

    def _markBorder(self):
        for key, status in self.login_data_status.items():
            if status:
                self.login_data[key].setStyleSheet("")
            else:
                self.login_data[key].setStyleSheet("border: 2px solid red;")
                self._showWrongFormatPopupMessage(key)

    def _showWrongFormatPopupMessage(self, element_name):
        msg_box = MessageBox()
        msg_box.showMessage(Message["login"]["format_message"][element_name])

    def _showUsernamePasswordFoundStatusPopupMessage(self, msg):
        msg_box = MessageBox()
        msg_box.showMessage(msg)