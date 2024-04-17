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

    def isPresent(self, table_name):
        """check if the needed databases present or not
        """
        pass


d = Database()
print(d.connect(database_credentials))