#use UPDATE and DELETE statement

import sqlite3

with sqlite3.connect('newbie.db') as conn:
    c = conn.cursor()

#update data
c.execute("UPDATE population SET population = 9000000 WHERE state='TX'")

#delete data
c.execute("DELETE FROM population WHERE city='Housten'")

print "\nNEW DATA:\n"

c.execute("SELECT * FROM population")

rows = c.fetchall()

for r in rows:
    print r[0],r[1],r[2]


