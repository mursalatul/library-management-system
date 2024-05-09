# importing necesarry clases 
from book import Book  
from users import *

class Library:
    def __init__(self,owner,library_name):
        self.owner=owner
        self.library_name=library_name
        self.allbooks=[]
        self.alluser=[]
    def add_books(self,category,book_id,book_name,quantity):
        # creating instance  of Book class to access the books info
        book=Book(category,book_id,book_name,quantity)
        self.allbooks.append(book)

    def add_users(self,user_id,user_name,password):
        user=User(user_id,user_name,password)
        self.alluser.append(user)
        return user
    def borrow_books(self,user,book_id):
        for book in self.allbooks:
            if book.book_id==book_id:
                if book in user.borrowed_books:
                    print(f"\n {book} Already been borrowed")
                    return
                elif book.quantity<1:
                    print(f"\n {book} currently 0 in stock")
                else:
                    user.borrowed_books.append(book)
                    book.quantity-=1
                    print(f"\n\t{book.book_name} borrowed successfully ! ")
                    return
        
        print(f"\n\tBook not found ! ")

 