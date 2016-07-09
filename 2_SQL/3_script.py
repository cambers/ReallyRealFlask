import sqlite3

with sqlite3.connect('newest.db') as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE population(city TEXT, state TEXT, population INT)")
    
    #create a list of tuples and use the executemany() function
    cities = [
            ('Seattle','WA',20000),
            ('Anacortes','WA',4000),
            ('Bellingham','WA',5000)
            ]

    c.executemany("INSERT INTO population VALUES(?,?,?)", cities)
