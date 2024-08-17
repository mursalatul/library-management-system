from PyQt5 import QtWidgets
from src.core.database import Database

class AddBook:
    """add book to the database"""
    def __init__(self, adminui: QtWidgets) -> None:
        self.adminui = adminui

        self.loadElementsOfAddBookPage()
        self.add_book_object["pushButton_add_book_add"].clicked.connect(self.addButtonAction)

    def addButtonAction(self):
        self.add_book_object["textBrowser_add_book_status"].setPlainText("Add button clicked")

    def loadElementsOfAddBookPage(self):
        self.add_book_object = {}
        self.add_book_object["lineEdit_add_book_id"] = self.adminui.findChild(
            QtWidgets.QLineEdit, "lineEdit_add_book_id"
        )
        self.add_book_object["lineEdit_add_book_name"] = self.adminui.findChild(
            QtWidgets.QLineEdit, "lineEdit_add_book_name"
        )
        self.add_book_object["lineEdit_add_book_author"] = self.adminui.findChild(
            QtWidgets.QLineEdit, "lineEdit_add_book_author"
        )
        self.add_book_object["lineEdit_add_book_number"] = self.adminui.findChild(
            QtWidgets.QLineEdit, "lineEdit_add_book_number"
        )
        self.add_book_object["pushButton_add_book_add"] = self.adminui.findChild(
            QtWidgets.QPushButton, "pushButton_add_book_add"
        )
        self.add_book_object["textBrowser_add_book_status"] = self.adminui.findChild(
            QtWidgets.QTextBrowser, "textBrowser_add_book_status"
        )


class AddBookDataAuthenticate:
    """check id, book_name, author_name and stock type"""
    def setter(self, id: str, book_name: str, author_name: str, stock: str):
        self.id = id
        self.book_name = book_name
        self.author_name = author_name
        self.stock = stock

    def checkDataType(self) -> bool:       
        if len(self.id) == 0 or len(self.book_name) == 0 or len(self.author_name) == 0 or len(self.stock) == 0:
            return False
        else:
            return True
    
    def checkDataAvailability(self):
        """this method will make sure
        1. for old input(id, name, author present) """
        pass