### this file handles the database related functions

import sqlite3, os
import datetime

from scraper import *
from macro import *
from configuration import *

### todo
#   clean the code
#   allow dynamic table selection
#   name the tables dynamically based on the date
#   better document the code 
#   add function parameters description

### create a new table
def create_new_table():
    ### establish database connection
    db_connection = connect_database()
    cursor = db_connection.cursor()

    today = datetime.date.today()
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
    db_connection.commit()

### function that allows insertion into selected table
def insert_into_table(origin):
    ### establish database connection
    db_connection = connect_database()
    cursor = db_connection.cursor()

    data = get_raw_table_data(TABLE, CURRENT_DAY)
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

        cursor.execute("INSERT INTO test VALUES (?,?,?,?,?,?,?,?)", item)
        db_connection.commit()
        item.clear()
    print('inserted...\n')

### function that prints the selected table
def print_from_table():
    ### establish database connection
    db_connection = connect_database()
    cursor = db_connection.cursor()

    cursor.execute('SELECT * FROM test')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

DATABASE_FILE = '..\\resources\\database\\database.db'

### create a database connection (or the database if it doesn't exist yet)
def connect_database():
    log_event(DB_LOG, INFO, 'database connection requested')

    if get_config_data(CONFIG_DB_FILE_PATH, CONFIG_DB_PATH_EXISTS) == FALSE:
        log_event(DB_LOG, INFO, 'database file does not exist. creating database file')
        update_config_data(CONFIG_DB_FILE_PATH, CONFIG_DB_PATH_EXISTS, TRUE)

        ### update the database file path 
        update_config_data(CONFIG_DB_FILE_PATH, CONFIG_DATABASE_PATH, DATABASE_FILE)

    db_filename = get_config_data(CONFIG_DB_FILE_PATH, CONFIG_DATABASE_PATH)

    ### create connection to local database and check if the file already exists ###
    db_connection   = sqlite3.connect(db_filename)    
    log_event(DB_LOG, INFO, 'database connection established')

    return db_connection
