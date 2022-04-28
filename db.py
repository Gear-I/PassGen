"""
The below code does the following:
	db_create_database() -> creates a database named app_pwd.db and returns the connection object
	db_create_table(connection) -> Creates a table application_password.
	insert(connection, column parameters) -> inserts the keyword parameters into application_password
	select() -> selects data from table application_password and returns the cursor object.
"""

import sqlite3

def db_create_database():
	db_connection = sqlite3.connection('app_pwd.db')
	#db_connection.execute("drop table application_password")
	return db_connection

def db_create_table(connection):
		connection.execute("""
			create table if not exists application_password 
			(ID integer primary key autoincrement, APPLICATION_NAME varchar2 (255) not null,
			EMAIL_ID varchr2(255) not null,
			PASSWORD varchr2(255) unique not null)
			""")
		connection.commit()
		return True

def insert(connection, **kwargs):
	insert_query = """insert into application_password
							(APPLICATION_NAME, EMAIL_ID, PASSWORD)
							values
						(""" + "'{}', '{}', '{}'" .format(kwargs['APPLICATION_NAME'],kwargs['EMAIL_ID'], kwargs['PASSWORD'])
	connection.execute(insert_query)
	connection.commit()
	print("Insert Successful")
	return True

def select(connection):
	return connection.execute("""
						select * from application_password
						""")

