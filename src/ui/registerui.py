from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

from src.core.register import Register

class RegisterUI(QtWidgets.QMainWindow):
    """handle register feature
    """
    def __init__(self, login_window) -> None:
        # instance of login_window(need for show login window again)
        self.login_window = login_window

        # load the register ui
        super(RegisterUI, self).__init__()
        loadUi('ui\\register_page.ui', self)
        self.show()

        # load the fields
        self._loadTheWidgets()

        # making label_or_register clickable
        self._makeLoginLabelClickable()

        # trigger login button
        self.pushButton_register.clicked.connect(self._registerButtonClicked)

    def _loadTheWidgets(self):
        """load all the input widgets in the login window
        """
        # getting all the fields
        # firstname
        self.lineEdit_firstname = self.findChild(QtWidgets.QLineEdit, 'lineEdit_firstname')
        # lastname
        self.lineEdit_lastname = self.findChild(QtWidgets.QLineEdit, 'lineEdit_lastname')
        # username
        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'lineEdit_username')
        # library id
        self.lineEdit_libraryid = self.findChild(QtWidgets.QLineEdit, 'lineEdit_libraryid')
        # password
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'lineEdit_password')
        # retyped password
        self.lineEdit_retyped_passwod = self.findChild(QtWidgets.QLineEdit, 'lineEdit_password_retype')
        # register button
        self.pushButton_register = self.findChild(QtWidgets.QPushButton, 'pushButton_register')

    def _makeLoginLabelClickable(self):
        """make the login label in register window clickable
        """
        self.label_or_login.mousePressEvent = self._loginLabelClicked

    def _loginLabelClicked(self, event):
        """Handle click event for the login label"""
        # show login window
        self.login_window.show()
        
        # close register window
        self.close()

    def _registerButtonClicked(self):
        """this method will handle all operation suppose to execute after
        click the register button"""
        handle_register = Register(
            firstname=self.lineEdit_firstname,
            lastname=self.lineEdit_lastname,
            username=self.lineEdit_username,
            libraryid=self.lineEdit_libraryid,
            password=self.lineEdit_password,
            retyped_password=self.lineEdit_retyped_passwod
        )
    
    def _border(self, element, status: bool):
        """Set and remove border from an element"""
        if status:
            element.setStyleSheet("")
        else:
            element.setStyleSheet("border: 2px solid red;")