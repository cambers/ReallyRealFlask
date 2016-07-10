#from homework on page 76

import sqlite3

with sqlite3.connect('cars.db') as conn:
    c = conn.cursor()
    c.execute("DROP TABLE orders")
    c.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date INT)")
    
    cars = [
            ('ford','pickup',1982-01-03),
            ('ford','pickup',1982-03-04),
            ('ford','ranger',1978-04-23),
            ('ford','ranger',1878-07-12),
            ('ford','ranger',1978-04-21),
            ('honda','civic',1976-02-13),
            ('honda','civic',1298-34-90),
            ('honda','cobalt',1234-34-05),
            ('honda','cobalt',1234-67-54)
            ]
    c.executemany("INSERT INTO orders VALUES(?,?,?)", cars)

    c.execute("""SELECT invent.make, invent.model, invent.inventory, orders.order_date
                FROM invent, orders WHERE invent.model = orders.model""")
    rows = c.fetchall()
    for r in rows:
        print  r[0] + r[1]
        print  str(r[2])
        print  str(r[3])



