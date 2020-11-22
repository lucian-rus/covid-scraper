### this file handles the configuration related functions

import os, json

from macro import *

### todo
#   better document the code 
#   add function parameters description

### config file paths and 
CONFIG_APP_FILE_PATH  = '..\\resources\\config\\application-config.json'
CONFIG_DB_FILE_PATH   = '..\\resources\\config\\database-config.json'
CONFIG_SETTINGS       = 'settings' 

### flags used for the application config file
CONFIG_SETUP          = 'setup'
CONFIG_REFRESH_STATUS = 'refresh_status'
CONFIG_REFRESH_RATE   = 'refresh_rate'
CONFIG_APP_LOG_PATH   = 'log_file_path'
CONFIG_EXCEL_PATH     = 'excel_path'
CONFIG_JSON_PATH      = 'json_path'
CONFIG_CSV_PATH       = 'csv_path'
CONFIG_TEMP_PATH      = 'temp_path'

### function that creates the config file for the application 
def create_app_config_file():

    ### initialise the dictionary that contains the settings for the config file
    init_app_config = {}

    init_app_config[CONFIG_SETTINGS] = []
    init_app_config[CONFIG_SETTINGS].append(
        {
            CONFIG_SETUP          : 'true',
            CONFIG_REFRESH_STATUS : 'false',
            CONFIG_REFRESH_RATE   : '',
            CONFIG_APP_LOG_PATH   : '..\\resources\\logs\\app-logs\\',
            CONFIG_EXCEL_PATH     : '..\\resources\\output\\xls\\',
            CONFIG_JSON_PATH      : '..\\resources\\output\\json\\',
            CONFIG_CSV_PATH       : '..\\resources\\output\\csv\\', 
            CONFIG_TEMP_PATH      : '..\\resources\\temp\\temp.json'
        }
    )

    ### set the path for the config file
    config_file = CONFIG_APP_FILE_PATH 
    curr_path   = os.path.dirname(__file__)
    target_path = os.path.relpath(config_file, curr_path)

    with open(target_path, 'w') as out:
        json.dump(init_app_config, out, indent=2)

### flags used for the database config gile
CONFIG_DB_PATH_EXISTS = 'db_path_exists'
CONFIG_DATABASE_PATH  = 'database_path'
CONFIG_DB_LAST_UPDATE = 'db_last_update'
CONFIG_DB_LOG_PATH    = 'db_log_path'

### function that creates a config file for the database
def create_db_config_file():

    ### initialise the dictionary that contains the settings for the config file
    init_db_config = {}

    init_db_config[CONFIG_SETTINGS] = []
    init_db_config[CONFIG_SETTINGS].append(
        {
            CONFIG_DB_PATH_EXISTS : 'false',
            CONFIG_DATABASE_PATH  : '',
            CONFIG_DB_LAST_UPDATE : '',
            CONFIG_DB_LOG_PATH    : '..\\resources\\logs\\db-logs\\'
        }
    )

    ### set the path for the config file
    config_file = CONFIG_DB_FILE_PATH
    curr_path   = os.path.dirname(__file__)
    target_path = os.path.relpath(config_file, curr_path)

    with open(target_path, 'w') as out:
        json.dump(init_db_config, out, indent=2)

### function that returns data from the config file based on a key
def get_config_data(target_file, key):
    result = NULL_STR

    log_event(APP_LOG, INFO, 'requested get_config_data({}, {})'.format(target_file, key))
    ### open the config file and search for the value stored by the given key
    with open(target_file) as read_file:
        data = json.load(read_file)

    for obj in data[CONFIG_SETTINGS]:
        result = obj[key]    

    log_event(APP_LOG, INFO, 'done executing function. return value: {}'.format(result))

    ### return the value of the requested key
    return result

### function that updates the configuration data based on a key
def update_config_data(target_file, key, update):
    log_event(APP_LOG, INFO, 'requested update_config_data({}, {})'.format(target_file, key))

    ### open the config file and search for the value stored by the given key
    with open(target_file) as read_file:
        data = json.load(read_file)

    for obj in data[CONFIG_SETTINGS]:
        obj[key] = update
        
    with open(target_file, 'w') as out:
        json.dump(data, out, indent=2)

    return OK

### initialise the configuration files
def init_config_files():
        create_app_config_file()
        create_db_config_file()
