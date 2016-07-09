import csv
import sqlite3

with sqlite3.connect('newsies.db') as conn:
    c = conn.cursor()
    employees = csv.reader(open('employees.csv', 'rU'))
    c.execute("DROP TABLE humans")
    c.execute("CREATE TABLE humans(firstname TEXT, lastname TEXT)")
    c.executemany("INSERT INTO humans VALUES(?,?)", employees)

    try:
        c.execute("INSERT INTO humans VALUES('Slim','Shady')")
        c.execute("INSERT INTO humans VALUES('Sylvester','Stallone')")
    except sqlite3.OperationalError:
        print 'Oops try again bozo'

