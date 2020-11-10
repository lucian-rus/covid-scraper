import sqlite3, os
from datetime import date
from configuration import *

### create a new table
def create_new_table():
    today = date.today()
    title = 'date' +  today.strftime("%d%m%Y")
    print(title)
    #query = 'CREATE TABLE ' +

### create a database connection (or the database if it doesn't exist yet)
def connect_database():

   ### create a database file 
    db_filename = 'test-database'
    db_is_new = not os.path.exists(db_filename)

    ### create connection to local database and check if the file already exists ###
    DB_CONNECTION   = sqlite3.connect(db_filename)    
    container_check = False

    if db_is_new:
        print('database does not exist. creating local database file...')
        container_check = True
    else:
        print('connecting to the database file...')

    create_new_table()