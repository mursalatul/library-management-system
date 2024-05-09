# importing necesarry clases
from book import *
from library import *
from users import *

# accseing the lib through diu_lib obj
diu_lib = Library("DIU", "Diu Unofficial")

# for testing by deafult seted an admin
admin = diu_lib.add_users(1, 'admin', 'admin')


# demo user for testing purpose
nahid = diu_lib.add_users(15, "nahid", "nahid_usha")
pallob = diu_lib.add_users(19, "pallob", "pallob_pal")

# added initially a book 5 copies
pybook = diu_lib.add_books('Cse', 103, 'Intro to C ', 5)

# terminal flag for running the program till user want to
running = True
# this will indicate who are accessing ,as by deafault we set as admin this will show the admin part interface when the program will run
currentUser = admin

while running:
    # checking if there is no user then it will ask for login or registration
    if currentUser == None:
        print(f"\n\tNo logged in user ! ")

        option = input("Login ? Registartion (L/R): ")

        if option == 'R':
            id = int(input("\tEnter id: "))
            name = input("\tEnter Name: ")
            password = input("\tEnter Password: ")
            # using oops magic through diu_libs objects method
            user = diu_lib.add_users(id, name, password)

            # this will enter the login ui directly after registration no need login after regi
            currentUser = user

        elif option == 'L':
            id = int(input("\tEnter id: "))
            password = input("\tEnter Password: ")

            match = False
            # authenicating part
            for user in diu_lib.alluser:
                if user.user_id == id and user.password == password:
                    currentUser = user
                    match = True
                    break

            if match == False:
                print(f"\n\tNo user found ! ")
    # if curent user exists whatever admin or user it will go inside else
    else:

        if currentUser.user_name == 'admin':
            print("\n \t Logged as admin  ")
            print("Options: \n")

            print("1 : Add Book")
            print("2 : Show Users") #will be implemented soon 
            print("3 : Show Books") #will be implemented soon  
            # more functionalities will be here 
            print("4 : Logout")

            # ch = int(input("\nEnter Option: "))
            try:
                ch = int(input("\nEnter Option: "))
            except ValueError:
                print("Invalid option, please enter a number.")
                continue

            if ch == 1:
                cat = input("\tEnter Cat: ")
                id = int(input("\tEnter id: "))
                name = input("\tEnter Name: ")
                q = int(input("\tEnter quantity: "))

                diu_lib.add_books(cat, id, name, q)

            elif ch == 4:
                currentUser = None

        else:
            print("\n Logged as student user ")
            print("Options: \n")

            print("1 : Borrow Book")
            # more functionalities will be here 

            print("2 : Logout")

            ch = int(input("\nEnter Option: "))

            if ch == 1:
                id = int(input("\tEnter id: "))
                diu_lib.borrow_books(currentUser, id)
            elif ch == 2:
                currentUser = None
