
import sqlite3

con = sqlite3.connect('mydatabase.db')

#to create a table in database , call the execute() methods on the connection

con.execute(''' 
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER ,
            email text PRIMARY KEY NOT NULL,
            password text NOT NULL
            );
''')
con.close()