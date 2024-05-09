class User:
    def __init__(self,user_id,user_name,password):
        self.user_id=user_id
        self.user_name=user_name
        self.password=password
        self.borrowed_books=[] #to store all borrowed books here 

