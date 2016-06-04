import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    #WHERE is a filter clause

    #UPDATE data
    c.execute("UPDATE population SET city='Seattle' WHERE population=4000")
    #DELETE data
    c.execute("DELETE FROM population WHERE state='Texas'")
    print "\nNEW DATA:\n"

    c.execute('SELECT * FROM population')
    rows = c.fetchall()
    for r in rows:
        print r[0],r[1],r[2]


