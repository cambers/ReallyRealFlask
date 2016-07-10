#Use the JOIN command to join the region and population tables

import sqlite3

with sqlite3.connect('newbie.db') as conn:
    c = conn.cursor()

    #retrieve data, use table_name.column_name (i.e., population.city ).
    c.execute("""SELECT population.city, population.population,
            regions.region FROM population, regions
            WHERE population.city = regions.city""")

    rows = c.fetchall()
    for r in rows:
        print 'City:' + r[0]
        print 'Population:' + str(r[1])
        print 'Region:' + r[2]


