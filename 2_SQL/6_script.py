import sqlite3

with sqlite3.connect('newbie.db') as conn:
    c = conn.cursor()

    

    cities = [
            ('Atlanta','GA',200),
            ('Macon','GA',200),
            ('Dawson','GA',400)
            ]

    c.executemany("INSERT INTO population VALUES(?,?,?)", cities)
    
    c.execute("DELETE FROM population WHERE city = 'Annaheim'")
    c.execute("UPDATE population SET city = 'Greenville' WHERE state = 'CA'")
    try:
        c.execute("SELECT * from population")

        rows = c.fetchall()
        for r in rows:
            print r[0],r[1],r[2]
    except sqlite3.OperationalError:
        print 'Try again silly beans'

