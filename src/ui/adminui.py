from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
from data.window_instance import windows
class AdminUI(QtWidgets.QMainWindow):
    """load admin ui
    it will be called from login page, when
    a admin will login
    """
    # this variable will hold the adminui on
    admin_page = None
    admin_page_object = {}
    def __init__(self) -> None:
        super(AdminUI, self).__init__()
        # load the admin page ui
        loadUi("ui\\admin.ui", self)
        # storing the window instance
        windows["adminui"] = self
        self.show()
        
        # load the field
        self._loadTheWidgets()
    
    def _loadTheWidgets(self):
        #  widget of the admin page
        self.admin_page_object["widget_main_options"] = self.findChild(
            QtWidgets.QWidget, "widget_main_options"
        )

        # widget of sub option book query
        self.admin_page_object["widget_sub_options_book_query"] = self.findChild(
            QtWidgets.QWidget, "widget_sub_options_book_query"
        )

        # push button of search book
        self.admin_page_object["pushButton_search_book"] = self.findChild(
            QtWidgets.QWidget, "pushButton_search_book"
        )

        # combo box 
        self.admin_page_object["comboBox_book_search_by"] = self.findChild(
            QtWidgets.QComboBox, "comboBox_book_search_by"
        )

        # combo box targetted line edit
        self.admin_page_object["lineEdit"] = self.findChild(
            QtWidgets.QLineEdit, "lineEdit_comboBox_targetted"
        )

        # search by the line edit button
        self.admin_page_object["pushButton_for_lineEdit_comboBox_targetted"] = self.findChild(
            QtWidgets.QPushButton, "pushButton_for_lineEdit_comboBox_targetted"
        )

        # show book information text browser
        self.admin_page_object["textBrowser_book_information"] = self.findChild(
            QtWidgets.QTextBrowser, "textBrowser_book_information"
        )

        # widget operations main screen
        self.admin_page_object["widget_operations"] = self.findChild(
            QtWidgets.QWidget, "widget_operations"
        )





