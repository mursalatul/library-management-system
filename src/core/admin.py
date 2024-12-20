from src.core.admin_opetation_handler.add_book import AddBook
from src.core.validation import FormatVerify
from data.Message_data import Message
from src.ui.popupui import MessageBox
from src.core.database import Database
from src.ui.adminui import AdminUI
from data.window_instance import windows
from src.core.admin_opetation_handler.search_book import SearchBook
from src.core.admin_opetation_handler.remove_book import RemoveBook
from src.core.admin_opetation_handler.modify_book import ModifyBook

from data.database_info import database_credentials


class Admin:
    # username and password format status
    admin_login_data_status = {"username": False, "password": False}

    def __init__(self, username, password) -> None:
        self.admin_login_data = {}
        self.admin_login_data["username"] = username
        self.admin_login_data["password"] = password
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
        # now admin_login_data_status will store the status
        # of if the username and password combo is
        # present in the database or not
        status = db.isUsernamePasswodPresent(
            "login_admin", self.admin_login_data["username"].text(), self.admin_login_data["password"].text()
        )
        self.admin_login_data_status["username"] = status
        self.admin_login_data_status["password"] = status

        if status:
            # username and password found
            self._showUsernamePasswordFoundStatusPopupMessage(Message["login"]["in_database"]["found"])

            # loading admin ui
            # self.admin_ui = AdminUI()
            self.admin_ui = AdminPageOperate()
            # hiding the login window
            windows["loginui"].hide()

        else:
            # username and password not found

            self._showUsernamePasswordFoundStatusPopupMessage(Message["login"]["in_database"]["not_found"])

    def _checkFormat(self):
        f = FormatVerify()
        self.admin_login_data_status["username"] = f.varifyUsernameFormat(
            self.admin_login_data["username"].text()
        )
        self.admin_login_data_status["password"] = f.verifyPasswordFormat(
            self.admin_login_data["password"].text()
        )

    def _isGoodFormated(self):
        return self.admin_login_data_status["username"] and self.admin_login_data_status["password"]

    def _markBorder(self):
        for key, status in self.admin_login_data_status.items():
            if status:
                self.admin_login_data[key].setStyleSheet("")
            else:
                self.admin_login_data[key].setStyleSheet("border: 2px solid red;")
                self._showWrongFormatPopupMessage(key)

    def _showWrongFormatPopupMessage(self, element_name):
        msg_box = MessageBox()
        msg_box.showMessage(Message["login"]["format_message"][element_name])

    def _showUsernamePasswordFoundStatusPopupMessage(self, msg):
        msg_box = MessageBox()
        msg_box.showMessage(msg)


class AdminPageOperate(AdminUI):
    """operate all the operations of admin page"""

    def __init__(self) -> None:
        super().__init__()  # executing the constructor of AdminUI

        # by default the search book page will show
        self.activate_search_book()

        # when search button will be clicked 
        self.admin_page_object["pushButton_search_book"].clicked.connect(
            self.activate_search_book
        )

        # when the add button will be clicked
        self.admin_page_object["pushButton_add_book"].clicked.connect(
            self.activate_add_book
        )

        # when the remove button will be clicked
        self.admin_page_object['pushButton_remove_book'].clicked.connect(self.active_remove_book)
        # when the modify button will be clicked
        self.admin_page_object['pushButton_modify_book'].clicked.connect(self.active_modify_book)

    def activate_search_book(self):
        self.admin_page_object["stackedWidget"].setCurrentWidget(self.admin_page_object["page_book_query_search"])
        self.sb = SearchBook(self)

    def activate_add_book(self):
        self.admin_page_object["stackedWidget"].setCurrentWidget(self.admin_page_object["page_book_query_add"])
        self.sb = AddBook(self)

    def active_remove_book(self):
        self.admin_page_object['stackedWidget'].setCurrentWidget(self.admin_page_object['page_book_query_remove'])
        self.sb = RemoveBook(self)

    def active_modify_book(self):
        self.admin_page_object['stackedWidget'].setCurrentWidget(self.admin_page_object['page_book_query_modify'])
        self.sb = ModifyBook(self)
