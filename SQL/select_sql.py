import sqlite3
import csv

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()
    #Don't create the table again just execute
    c.execute("SELECT firstname, lastname FROM employees")
    
    for row in c.fetchall():
        print row[0],row[1]

