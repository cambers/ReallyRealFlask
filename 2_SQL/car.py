import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE inventory(make TEXT, model TEXT, quantity INT)")

