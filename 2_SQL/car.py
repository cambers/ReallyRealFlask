import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()
    c.execute("DROP TABLE invent")
    c.execute("CREATE TABLE invent(make TEXT,model TEXT, inventory INT)")
    c.execute("INSERT INTO invent VALUES('ford','caravan',5)")
    autos = [
            ('ford','pickup',200),
            ('ford','ranger',300),
            ('honda','civic',200),
            ('honda','cobalt',400)
            ]
    c.executemany("INSERT INTO invent VALUES(?,?,?)", autos)

    c.execute("UPDATE invent SET make = 'ford' WHERE inventory = 200")
    c.execute("DELETE FROM invent WHERE model = 'civic'")

    c.execute("SELECT make,model,inventory from invent WHERE make = 'ford'")
    rows = c.fetchall()
    print "\nNEW DATA\n"

    for r in rows:
        print r[0],r[1],r[2]

