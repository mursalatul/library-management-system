import psycopg2

from data.database_info import database_credentials  # use it(with app)

# from database_info import database_credentials  # delete it


class Database:
    def __init__(self) -> None:
        self.connect(database_credentials=database_credentials)
    
    def readyDataBase(self):
        """this method will create all the necessary database and table for this program to run currectly
        database name: elibrary
        tables: login(libraryid, username, password)
                user_info_basic(libraryid, firstname, lastname, username)
        """
        try:
            # store status if they are present in the database or not
            database_found = False
            login_table_found = False
            user_info_basic_table_found = False

            cursor = self.conn.cursor()
            # checking if already the elibrary database present as a database or not
            query = "SELECT 1 FROM pg_database WHERE datname = 'elibrary';"
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                database_found = True

            # if database not found no need to search for the tables cause the are also not present
        #     if database_found == False:
        #         # creating database
        #         query = "CREATE DATABASE elibrary;"
        #         cursor.execute(query)
        #         self.conn.commit()

        #         # creating tables
        #         self._createTable("login", "(libraryid VARCHAR(20) PRIMARY ID)")
        #         cursor.close()
        # except Exception as e:
        #     print("Erros in database.py/readyDatabase.py")
        #     print(str(e))

    def connect(self, database_credentials) -> str:
        """connect to a particular database

        Args:
            database_credentials (dict): information about the database

        Returns:
            str: 'connected' when successfully connected. else the error message
        """
        try:
            self.conn = psycopg2.connect(
                database=database_credentials["database"],
                user=database_credentials["user"],
                password=database_credentials["password"],
                host=database_credentials["host"],
                port=database_credentials["port"],
            )
            return "connected"
        except Exception as e:
            return str(e)

    def isUsernamePasswodPresent(self, username: str, password: str) -> bool:
        """THIS METHOD IS SPECIFICALLY WRITTEN FOR FIND EXISTING USERNAME AND PASSWORD COMBO
        find username & password combo.
        Args:
            username (str)
            password (str)
        Returns:
            bool: True if the username and password is found, else return False
        """
        try:
            cursor = self.conn.cursor()
            quary = """SELECT * FROM login WHERE username = %s AND password = %s"""
            cursor.execute(quary, (username, password))
            result = cursor.fetchone()
            cursor.close()

            if result:
                # username password combo found
                return True
            else:
                # username password combo not found
                return False
        except Exception as e:
            # return False if exception occure
            print(str(e))
            print("ok")
            return False

    def isDataPresent(self, table_name: str, column_name: str, data: str):
        """search for a data in a particular column in a particular table
        Args:
            table_name (str): name of the table where the data will be looked
            column_name (str): targettad table
            data (str): search object
        Return:
            True (bool): if the data found
            False (bool): if the data is not found or exception happend
        """
        try:
            cursor = self.conn.cursor()
            query = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
            cursor.execute(query, (data,))
            result = cursor.fetchone()
            cursor.close()

            if result:
                # username password combo found
                return True
            else:
                # username password combo not found
                return False
        except Exception as e:
            # return False if exception occure
            print(str(e))
            return False
        
    def insertData(self, table_name: str, columns: list, values: list):
        """insert data in a table. must provide the list of colums and values in str
        Args:
            table_name (str): name of the table where data will be inserted
            columns (list): list of the columns names
            values (list): values for the columns
        Return:
            True (bool): if insertion complete
            False (bool): if can not insert for any reason or exception happen
        """
        try:
            # number of columsn must be same as number of values
            if len(columns) != len(values):
                raise ValueError("column number and value number is not same.")
            
            cursor = self.conn.cursor()
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(values))})"

            cursor.execute(query, values)
            self.conn.commit()
            return True
        except Exception as e:
            return str(e)

    def deleteData(self, table_name: str, libraryid: str):
        """ delete data from a table by targetting library id
        Args:
            table_name (str): name of the table from where data will be removed
            libraryid (str): deletion will be happend based of libraryid
        Return:
            True (bool): if deletion complete
            False (bool): if cant found the library id or exception happen
        """
        try:
            cursor = self.conn.cursor()
            query =  f"DELETE FROM {table_name} WHERE libraryid = %s"
            cursor.execute(query, libraryid)
            self.conn.commit()
            return True
        except Exception as e:
            return str(e)

    def _createTable(self, table_name: str, columns: str):
        try:
            curser = self.conn.cursor()
            query = "CREATE TABLE {table_name} "+columns+";"
            curser.execute(query)
            self.conn.commit()
            curser.close()
        except Exception as e:
            print("error in database.py->_createTable()")
            print(str(e))


# d = Database()
# # print(d.connect(database_credentials))
# print(d.isUsernamePasswodPresent("pallob", "Pallob@1"))
# d.createTable()
# d.insertData("user_info_basic", ["libraryid", "firstname", "lastname", "username"], ["1", "a", "b", "c"])
# d.deleteData("user_info_basic", '1')