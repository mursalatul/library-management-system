from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

class Register(QtWidgets.QMainWindow):
    """handle register feature
    """
    def __init__(self, login_window) -> None:
        # instance of login_window(need for show login window again)
        self.login_window = login_window

        # load the register ui
        super(Register, self).__init__()
        loadUi('ui\\register_page.ui', self)
        self.show()

        # load the fields
        self._loadTheWidgets()

        # making label_or_register clickable
        self._makeLoginLabelClickable()

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

        # lastname

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
