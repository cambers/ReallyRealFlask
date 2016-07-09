#use the insert statement
import sqlite3

with sqlite3.connect('newbie.db') as conn:
    c = conn.cursor()
    c.execute("DROP TABLE population")
    c.execute("CREATE TABLE population(city TEXT, state TEXT, population INT)")
    c.execute("INSERT INTO population VALUES('Dallas','TX', 20000)")
    c.execute("INSERT INTO population VALUES('Austin','TX', 40000)")
    #conn.close() <script will not run??


