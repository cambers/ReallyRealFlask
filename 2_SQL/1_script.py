#Create a sqlite3 db and table

import sqlite3

#create a db
conn = sqlite3.connect('new.db')

#create a cursor object to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population(city TEXT, state TEXT, population INT)""")

#close the connection
conn.close()


