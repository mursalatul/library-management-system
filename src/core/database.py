import psycopg2

from data.database_info import database_credentials  # use it(with app)

# from database_info import database_credentials  # delete it


class Database:
    def __init__(self) -> None:
        self.connect(database_credentials=database_credentials)

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
            return False

    def isDataPresent(self, table_name: str, column_name: str, data: str):
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
        try:
            cursor = self.conn.cursor()
            query =  f"DELETE FROM {table_name} WHERE libraryid = %s"
            cursor.execute(query, libraryid)
            self.conn.commit()
            return True
        except Exception as e:
            return str(e)

    # def createTable(self):
    #     try:
    #         curser = self.conn.cursor()
    #         curser.execute('''CREATE TABLE user_info_basic (
    #                             libraryid VARCHAR(20) PRIMARY KEY,
    #                             firstname VARCHAR(20),
    #                             lastname VARCHAR(20),
    #                             username VARCHAR(20)
    #                         );''')
    #         self.conn.commit()
    #         curser.close()
    #     except:
    #         print("Not done")


# d = Database()
# # print(d.connect(database_credentials))
# print(d.isUsernamePasswodPresent("pallob", "Pallob@1"))
# d.createTable()
# d.insertData("user_info_basic", ["libraryid", "firstname", "lastname", "username"], ["1", "a", "b", "c"])
# d.deleteData("user_info_basic", '1')