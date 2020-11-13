### this file handles the database related functions

import sqlite3, os
from datetime import date

from scraper import *
from macros import *

### todo
#   clean the code
#   allow dynamic table selection
#   name the tables dynamically based on the date
#   better document the code 
#   add function parameters description

### create a new table
def create_new_table(cursor, DB_CONNECTION):
    #today = date.today()
    #title = 'date' +  today.strftime("%d%m%Y")
    title = 'test'
    query  = 'CREATE TABLE ' + title 
    query += ''' (
                id integer PRIMARY KEY NOT NULL,
                country_name text NOT NULL,
                total_cases text NOT NULL,
                new_cases text NOT NULL,
                total_deaths text NOT NULL,
                new_deaths text NOT NULL,
                total_tests text NOT NULL,
                population text NOT NULL
             ); '''
    cursor.execute(query)
    print('table created')
    DB_CONNECTION.commit()

### function that allows insertion into selected table
def insert_into_table(cursor, DB_CONNECTION):
    print('inserting...')
    data = []
    item = []

    for obj in data:
        if obj.id == 0:
            continue
        item.append(obj.id)
        item.append(obj.country_name)
        item.append(obj.total_cases)
        item.append(obj.new_cases)
        item.append(obj.total_deaths)
        item.append(obj.new_deaths)
        item.append(obj.total_tests)
        item.append(obj.population)

        print(item)
        cursor.execute("INSERT INTO test VALUES (?,?,?,?,?,?,?,?)", item)
        DB_CONNECTION.commit()
        item.clear()
    print('inserted...\n')

### function that prints the selected table
def print_from_table(cursor, DB_CONNECTION):
    cursor.execute('SELECT * FROM test')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

### create a database connection (or the database if it doesn't exist yet)
def connect_database():

   ### create a database file 
    db_filename = 'database.db'
    db_is_new = not os.path.exists(db_filename)

    ### create connection to local database and check if the file already exists ###
    DB_CONNECTION   = sqlite3.connect(db_filename)    

    table_check = True
    if db_is_new:
        print('database does not exist. creating local database file...')
        connect_database()
        table_check = False
    else:
        print('connecting to the database file...')

    cursor = DB_CONNECTION.cursor()
    
    if table_check:
        #create_new_table(cursor, DB_CONNECTION)
        #insert_into_table(cursor, DB_CONNECTION)
        print_from_table(cursor, DB_CONNECTION) 