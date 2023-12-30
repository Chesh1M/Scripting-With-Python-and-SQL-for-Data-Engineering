import sqlite3

connection = sqlite3.connect('sample.db')

# create table
table = 'CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)'
# create cursor to allow us to execute the table
cursor = connection.cursor()
cursor.execute(table)
connection.commit()


## Now that the database is created, access it through cmd line using
## sqlite3 sample.db