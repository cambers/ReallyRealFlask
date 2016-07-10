import sqlite3
import csv

with sqlite3.connect('newsies.db') as conn:
    c = conn.cursor()
    employees = csv.reader(open('employees.csv','rU')) 
    c.execute("DROP TABLE empleados")    
    c.execute("CREATE TABLE empleados(firstname TEXT, lastname TEXT)")
    c.executemany("INSERT INTO empleados VALUES(?,?)", employees)
    
    #add some more employees
    c.execute("INSERT INTO empleados VALUES('Sal','Williams')")

    peeps = [
            ('bart','simpson'),
            ('maggie','simpson')
            ]
    c.executemany("INSERT INTO empleados VALUES(?,?)", peeps)

    #loop through the db
    c.execute("SELECT firstname, lastname from empleados")
    rows = c.fetchall()
    for r in rows:
        print r[0],r[1]


