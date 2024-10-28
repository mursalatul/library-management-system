from PyQt5 import QtWidgets
from src.core.database import Database
from data.Message_data import Message

class ModifyBook:
    def __init__(self, adminui: QtWidgets) -> None:
        self.adminui = adminui

        self.loadElementsOfModifyBookPage()
        self.modify_book_object["pushButton_modify_book_change"].clicked.connect(self.modifyButtonAction)

    def loadElementsOfModifyBookPage(self):
        self.modify_book_object = {}

        # id
        self.modify_book_object["lineEdit_modify_book_id"] = self.adminui.findChild(
            QtWidgets.QLineEdit,  "lineEdit_modify_book_id"
        )

        # name
        self.modify_book_object["lineEdit_modify_book_name"] = self.adminui.findChild(
            QtWidgets.QLineEdit,  "lineEdit_modify_book_name"
        )

        # author
        self.modify_book_object["lineEdit_modify_book_author"] = self.adminui.findChild(
            QtWidgets.QLineEdit,  "lineEdit_modify_book_author"
        )

        # edition
        self.modify_book_object["lineEdit_modify_book_edition"] = self.adminui.findChild(
            QtWidgets.QLineEdit,  "lineEdit_modify_book_edition"
        )

        # number
        self.modify_book_object["lineEdit_modify_book_number"] = self.adminui.findChild(
            QtWidgets.QLineEdit,  "lineEdit_modify_book_number"
        )


        self.modify_book_object["textBrowser_modify_book_status"] = self.adminui.findChild(
            QtWidgets.QTextBrowser, "textBrowser_modify_book_status"
        )
        self.modify_book_object["pushButton_modify_book_change"] = self.adminui.findChild(
            QtWidgets.QPushButton, "pushButton_modify_book_change"
        )




    def modifyButtonAction(self):
        book_auth = ModifyBookDataAuthenticate()
        book_auth.setter(
            self.modify_book_object["lineEdit_modify_book_id"],
            self.modify_book_object["lineEdit_modify_book_name"],
            self.modify_book_object["lineEdit_modify_book_author"],
            self.modify_book_object["lineEdit_modify_book_edition"],
            self.modify_book_object["lineEdit_modify_book_number"]
        )

        if not book_auth.checkDataType():
            self.modify_book_object["textBrowser_modify_book_status"].setPlainText(
                "All information is not given."
            )

        # check if any data is present or invalid
        elif book_auth.isValidData() == False:
            self.modify_book_object["textBrowser_modify_book_status"].setPlainText(
                "Book Failed to add!\n" + book_auth.error_message
            )
        else:
            db = Database()
            db.deleteData('books', 'book_id', self.modify_book_object["lineEdit_modify_book_id"].text())
            # adding the new data
            db.insertData(
                table_name="books",
                columns=["book_id", "book_name", "author", "edition", "stock"],
                values=[
                    self.modify_book_object["lineEdit_modify_book_id"].text(),
                    self.modify_book_object["lineEdit_modify_book_name"].text(),
                    self.modify_book_object["lineEdit_modify_book_author"].text(),
                    self.modify_book_object["lineEdit_modify_book_edition"].text(),
                    self.modify_book_object["lineEdit_modify_book_number"].text()
                ]
            )
            self.modify_book_object["textBrowser_modify_book_status"].setPlainText(
                "Book Updated.\n" + self.toCustomString((
                    self.modify_book_object["lineEdit_modify_book_id"].text(),
                    self.modify_book_object["lineEdit_modify_book_name"].text(),
                    self.modify_book_object["lineEdit_modify_book_author"].text(),
                    self.modify_book_object["lineEdit_modify_book_edition"].text(),
                    self.modify_book_object["lineEdit_modify_book_number"].text()
                ))
            )

    def toCustomString(self, info: tuple):
        """create a standard printing format with the data
        from tuple. this printing format will be used to show
        the book information in the textBrower

        """
        spacing = 5
        id_space = max(len(str(info[0])), len('ID')) + spacing
        book_name = max(len(str(info[1])), len("Book Name")) + spacing
        author = max(len(str(info[2])), len("Author")) + spacing
        version = max(len(str(info[3])), len("Version")) + spacing
        stock = max(len(str(info[4])), len("Stock")) + spacing

        header = "ID".ljust(id_space) + "Book Name".ljust(book_name) + "Author".ljust(author) + "Version".ljust(
            version) + "Stock".ljust(stock) + "\n"
        header += "".center(len(header), "-") + "\n"

        return header + str(info[0]).ljust(id_space) + str(info[1]).ljust(book_name) + str(info[2]).ljust(author) + str(
            info[3]).ljust(version) + str(info[4]).ljust(stock)

class ModifyBookDataAuthenticate:
    """check id, book_name, author_name and stock type"""

    def setter(self, id, book_name, author_name, edition, stock):
        self.id = id
        self.book_name = book_name
        self.author_name = author_name
        self.edition = edition
        self.stock = stock

    def checkDataType(self) -> bool:
        if len(self.id.text()) == 0 or len(self.book_name.text()) == 0 or len(self.author_name.text()) == 0 or len(
                self.edition.text()) == 0 or len(self.stock.text()) == 0:
            return False
        else:
            return True

    def isValidData(self):
        """check
        1. if id already exist in the database
        2. if book name already exist in the database
        3. edition and stock are int numbers"""
        db = Database()

        # checking id
        if db.getData("books", "book_id", self.id.text()) == None:
            self.error_message = "Id Dont exist. Choose a valid id."
            self._markBorder(self.id, "red")
            return False
        else:
            self._markBorder(self.id, "white")


        # checking if the edition is a pure number or not
        if not self.edition.text().isnumeric():
            self.error_message = "Book's Edition should be a number."
            self._markBorder(self.edition, "red")
            return False
        else:
            self._markBorder(self.edition, "white")

        # checking if the stock is a pure number or not
        if not self.stock.text().isnumeric():
            self.error_message = "Book's quantity should be a number."
            self._markBorder(self.stock, "red")
            return False
        else:
            self._markBorder(self.stock, "white")

        # if all ok, return true
        return True

    def _markBorder(self, element, color):
        """mark/unmark the borders of the fields if error found"""
        if color == "white":
            element.setStyleSheet("")
        else:
            element.setStyleSheet("border: 2px solid red;")