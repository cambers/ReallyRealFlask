import sqlite3

#Only use single quotes around strings

'''
$python sql.py
$sqlite3 sample.db
>select * from posts;
>
>insert into posts values('hey','baby');

--To erase the table in the script:
    c.execute("""DROP TABLE posts""")
    '''



#create a db 
with sqlite3.connect('new.db') as conn:
    #Create cursor object to execute SQL commands
    c = conn.cursor()
    #Create a db table with 3 field/rows
    #Don't use three quotes in a row aka """ """
    c.execute(" CREATE TABLE population (name TEXT, age TEXT, population INTEGER)")
    #conn.commit()   < not necessary if u use the 'with' statement
    conn.close()



