# import psycopg2
# def get_connection():
# 	try:
# 		return psycopg2.connect(
# 			database="test1",
# 			user="postgres",
# 			password="1234",
# 			host="localhost",
# 			port=5432,
# 		)
# 	except:
# 		return False
# conn = get_connection()
# print(conn)
# cr = conn.cursor()
# cr.execute("""INSERT INTO person (id, name, age)
# VALUES
#     (7, 'John', 30),
#     (8, 'Emma', 25),
#     (9, 'Michael', 40);

# """)
# conn.commit()
# if conn:
# 	print("Connection to the PostgreSQL established successfully.")
# else:
# 	print("Connection to the PostgreSQL encountered and error.")

# conn.close()

# # class Database:
    