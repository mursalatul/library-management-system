from src.core.validation import FormatVerify
from data.Message_data import Message
from src.ui.popupui import MessageBox
class Login:
    # username and password format status
    login_data_status = {
        "username": False,
        "password": False
    }

    def __init__(self, username, password) -> None:
        self.login_data = {}
        self.login_data["username"] = username
        self.login_data["password"] = password
        self._username = username
        self._password = password
        
        # check if the username and password format is ok
        self._checkFormat()
        self._markBorder()
    
    def _checkFormat(self):
        f = FormatVerify()
        self.login_data_status["username"] = f.varifyUsernameFormat(self.login_data["username"].text())
        self.login_data_status["password"] = f.verifyPasswordFormat(self.login_data["password"].text())
    
    def isGoodFormated(self):
        return self.usernameOk and self.passowordOk
    
    def _markBorder(self):
        for key, status in self.login_data_status.items():
            if status:
                self.login_data[key].setStyleSheet("")
            else:
                self.login_data[key].setStyleSheet("border: 2px solid red;")
                self._showWrongFormatPopupMessage(key)

    def _showWrongFormatPopupMessage(self, element_name):
        msg_box = MessageBox()
        if element_name == "username":
            msg_box.showMessage(Message["login"]["wrong_format_username"])
        else:
            msg_box.showMessage(Message["login"]["wrong_format_password"])
