from PyQt5 import QtWidgets
from src.core.database import Database

class SearchBook:
    def __init__(self, adminui: QtWidgets) -> None:
        # creating database object for query
        self.db = Database()
        # targetted table
        self.table = "books"
        self.adminui = adminui

        
        # triger search by line edit button
        adminui.admin_page_object["pushButton_for_lineEdit_comboBox_targetted"].clicked.connect(self.lineEdit_pushButton_clicked)
    
    def reloadFields(self):
        # getting the textbrowser, comboBox, lineEdit field for new input
        self.textBrower = self.adminui.admin_page_object["textBrowser_book_information"]
        self.book_search_target = self.adminui.admin_page_object["comboBox_book_search_by"].currentText()
        self.book_search_value = self.adminui.admin_page_object["lineEdit_comboBox_targetted"].text()

        # getting the data from database
        if self.book_search_target == "Name":
            self.book_information = self.db.getData(self.table, "book_name", self.book_search_value)
        elif self.book_search_target == "ID":
            self.book_information = self.db.getData(self.table, "book_id", self.book_search_value)
        elif self.book_search_target == "Author":
            self.book_information = self.db.getData(self.table, "author", self.book_search_value)

    def lineEdit_pushButton_clicked(self):
        self.reloadFields()
        if self.book_information == None:
            if len(self.book_search_value):
                self.textBrower.setPlainText(f"{self.book_search_target} = {self.book_search_value} not found!")
            else:
                # no value entered in the line edit field in the book search page
                self.textBrower.setPlainText(f"Please give the value of {self.book_search_target}")

        else:
            self.textBrower.setPlainText(self.toCustomString(self.book_information))
            # print(self.book_information)
            
    def toCustomString(self, info: tuple):
        spacing = 5
        id_space = max(len(str(info[0])), len('ID')) + spacing
        book_name = max(len(str(info[1])), len("Book Name")) + spacing
        author = max(len(str(info[2])), len("Author")) + spacing
        version = max(len(str(info[3])), len("Version")) + spacing
        stock = max(len(str(info[4])), len("Stock")) + spacing

        header = "ID".ljust(id_space) + "Book Name".ljust(book_name) + "Author".ljust(author) + "Version".ljust(version) + "Stock".ljust(stock) + "\n"
        header += "".center(len(header), "-") + "\n"

        return header + str(info[0]).ljust(id_space) + str(info[1]).ljust(book_name) + str(info[2]).ljust(author) + str(info[3]).ljust(version) + str(info[4]).ljust(stock)