import psycopg2

# from data.database_info import database_credentials # use it(with app)
from database_info import database_credentials # delete it
class Database:
    def connect(self, database_credentials) -> str:
        """connect to a particular database

        Args:
            database_credentials (dict): information about the database

        Returns:
            str: 'connected' when successfully connected. else the error message
        """
        try:
            self.conn = psycopg2.connect(database=database_credentials['database'], user=database_credentials['user'], password=database_credentials['password'], host=database_credentials['host'], port=database_credentials['port'])
            return 'connected'
        except Exception as e:
            return str(e)

    def findUsernamePasswod(self, username, password):
        """Load a specific table
        """
        try:
            cursor = self.conn.cursor()
            quary = """SELECT * FROM libraryid_username_password WHERE username = %s AND password = %s"""
            cursor.execute(quary, (username, password))
            result = cursor.fetchone()
            cursor.close()

            if result:
                return "User found!"
            else:
                return "User not found or incorrect credentials."
        except Exception as e:
            return "Error: " + str(e)

    # def createTable(self):
    #     try:
    #         curser = self.conn.cursor()
    #         curser.execute('''CREATE TABLE test (
    #                             name VARCHAR(255),
    #                             number INT
    #                         );''')
    #         self.conn.commit()
    #         curser.close()
    #     except:
    #         print("Not done")

d = Database()
print(d.connect(database_credentials))
print(d.loadTable("pallob", "1234pal"))
