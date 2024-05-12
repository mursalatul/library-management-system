from PyQt5 import QtWidgets
from src.core.database import Database

class SearchBook:
    def __init__(self, adminui: QtWidgets) -> None:
        # creating database object for query
        db = Database()
        # targetted table
        table = "books"
        # getting textBrowser
        self.textBrower = adminui.admin_page_object["textBrowser_book_information"]
        self.book_search_target = adminui.admin_page_object["comboBox_book_search_by"].currentText()
        self.book_search_value = adminui.admin_page_object["lineEdit_comboBox_targetted"].text()



        if self.book_search_target == "Name":
            self.book_information = db.getData(table, "book_name", self.book_search_value)
        elif self.book_search_target == "ID":
            self.book_information = db.getData(table, "book_id", self.book_search_value)
        elif self.book_search_target == "Author":
            self.book_information = db.getData(table, "author", self.book_search_value)
        
        # triger search by line edit button
        adminui.admin_page_object["pushButton_for_lineEdit_comboBox_targetted"].clicked.connect(self.lineEdit_pushButton_clicked)
    
    def lineEdit_pushButton_clicked(self):
        if self.book_information == None:
            self.textBrower.setPlainText(f"{self.book_search_target} = {self.book_search_value} not found!")
        else:
            self.textBrower.setPlainText(self.book_information)
            
