import sqlite3
import csv

#objects have to have single quotes in SQL
with sqlite3.connect('new.db') as conn:
    c = conn.cursor()
    c.execute('DROP TABLE population')
    c.execute('CREATE TABLE population(city TEXT, state TEXT, population INT)')
    c.execute("INSERT INTO population VALUES('Housten','Texas', 2000)")
    c.execute("INSERT INTO population VALUES('Dallas','Texas', 40000)")

    cities = [
        ('Boston','Mass',2000),
        ('Phoenix','Arizona', 783),
        ('San Francisco','California',4000)
        ]

    #Use these ? parameterized statements instead of string subsitution %s cuz of sql injections
    c.executemany("INSERT INTO population VALUES(?,?,?)", cities)

     
    #insert values from a CSV file into the DB via the executemany function
    employees = csv.reader(open('employees.csv', 'rU'))
    try:
        c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
        c.executemany("INSERT INTO employees VALUES(?,?)", employees)
    except sqlite3.OperationalError:
        print 'The table has already been created and I want to print out the iterators below'



    #Use SELECT to print out all the rows of the employees table
    c.execute("SELECT firstname, lastname FROM employees")
    rows = c.fetchall()   #fetchall retrieves all records from the query and stores them in a tuple
    for r in rows:
        print r[0], r[1]

    posts = []
    for r in rows:
        posts.append(dict(firstname=r[0],lastname=r[1]))
    print posts


    #close the connection w/ the connection object = conn
   # conn.close()





