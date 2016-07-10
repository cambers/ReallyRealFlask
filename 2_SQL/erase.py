
import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT invent.make, invent.model,
            invent.inventory, orders.order_date FROM invent INNER JOIN orders
            ON invent.model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3]
        print
