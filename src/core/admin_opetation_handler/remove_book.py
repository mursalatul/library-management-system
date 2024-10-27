from PyQt5 import QtWidgets
from src.core.database import Database

class RemoveBook:
    def __init__(self, adminui: QtWidgets) -> None:
        self.adminui = adminui

        self.loadElementsOfRemoveBookPage()
        self.remove_book_object["pushButton_remove_book_remove_button"].clicked.connect(self.removeButtonAction)

    def loadElementsOfRemoveBookPage(self):
        self.remove_book_object = {}
        self.remove_book_object["lineEdit_remove_book_id"] = self.adminui.findChild(
            QtWidgets.QLineEdit,  "lineEdit_remove_book_id"
        )
        self.remove_book_object["textBrowser_remove_book_status"] = self.adminui.findChild(
            QtWidgets.QTextBrowser, "textBrowser_remove_book_status"
        )
        self.remove_book_object["pushButton_remove_book_remove_button"] = self.adminui.findChild(
            QtWidgets.QPushButton, "pushButton_remove_book_remove_button"
        )
    def validId(self) -> bool:
        id = self.remove_book_object["lineEdit_remove_book_id"].text()
        return not (len(id) == 0 or not id.isnumeric())

    def removeButtonAction(self):
        if self.validId():
            self.remove_book_object["textBrowser_remove_book_status"].setPlainText("valid id")
        else:
          self.remove_book_object["textBrowser_remove_book_status"].setPlainText("Invalid id")