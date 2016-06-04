import sqlite3
import csv

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()
    c.execute('DROP TABLE inventory')
    c.execute("CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)")
    
    cars = [
        ('Ford','Taures',20),
        ('Ford','Truck',30),
        ('Ford','Pickup',40),
        ('Honda','Accord',40),
        ('Honda','Sedan',80)
        ]
    c.executemany("INSERT INTO inventory VALUES(?,?,?)", cars)

    c.execute("UPDATE inventory SET quantity=4000000 WHERE model='Honda'")
    c.execute("DELETE FROM inventory WHERE model='Pickup'")

    c.execute("SELECT * FROM inventory WHERE make='Ford'")
    rows = c.fetchall()
    for r in rows:
        print r[0],r[1],r[2]
