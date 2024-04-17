from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

class Login(QtWidgets.QMainWindow):
    """handle login feature
    """
    def __init__(self) -> None:
        # load the login ui
        super(Login, self).__init__()
        loadUi('ui\login_page.ui', self)
        self.show()

        # load the fields
        self._loadTheWidgets()

        # making label_or_register clickable
        self._makeRegisterLabelClickable()
    def _loadTheWidgets(self):
        """load all the input widgets in the login window
        """
        # getting username and password
        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'lineEdit_username')
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'lineEdit_password')

        # getting login button
        self.pushButton_login = self.findChild(QtWidgets.QPushButton, 'pushButton_login')

        # getting register lable
        self.label_or_register = self.findChild(QtWidgets.QLabel, 'label_or_register')

    def _makeRegisterLabelClickable(self):
        self.label_or_register.mousePressEvent = self._registerLabelClicked

    def _registerLabelClicked(self, event):
        """Handle click event for the register label"""
        print("Register label clicked!")

    def user(self, username, password) -> None:
        self._username = username
        self._password = password

class HandleLogin:
    def __init__(self) -> None:
        app = QtWidgets.QApplication(sys.argv)
        l = Login()
        sys.exit(app.exec_())