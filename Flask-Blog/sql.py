import sqlite3

with sqlite3.connect('blog.db') as conn:
    c = conn.cursor()
    
    c.execute("DROP TABLE if exists posts")
    c.execute("CREATE TABLE posts(title TEXT, post TEXT)")

    #insert stupid data into it
    c.execute("INSERT INTO posts VALUES('Its the beginning','Get ready')")
    c.execute("INSERT INTO posts VALUES('Still hanging tuff','Tuff n up')")
    c.execute("INSERT INTO posts VALUES('Its the end','Shit outta luck')")


