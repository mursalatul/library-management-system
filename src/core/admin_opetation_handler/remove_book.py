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
    def validId(self):
        """
        Work:
            1. see if the id is a valid id, if no, go to step 4, else step 2
            2. if id is valid id, check the id presence in the database books.
                if found go to step 3,
                else go to step 4
            3. return true
            4. return false
        Returns:
            object: False if not found, else the data

        """
        id = self.remove_book_object["lineEdit_remove_book_id"].text()
        if  (len(id) == 0 or not id.isnumeric()):
            return False
        db = Database()
        status = db.getData('books','book_id', id)
        if status == None:
            return False
        else:
            # removing the book form the table
            db.deleteData('books','book_id',id)
            return status

    def removeButtonAction(self):
        status = self.validId()
        if not status:
          self.remove_book_object["textBrowser_remove_book_status"].setPlainText("Invalid id")
        else:
          self.remove_book_object["textBrowser_remove_book_status"].setPlainText(
              f'Book Removed:\n{status[0]}\t{status[1]}\t{status[2]}')

