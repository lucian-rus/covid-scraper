### this file handles the configuration related functions

import configparser
import os 

from macro import *

### todo
#   better document the code 
#   add function parameters description

### flags used for the application config file
CONFIG_REFRESH_STATUS = 'refresh_status'
CONFIG_REFRESH_RATE   = 'refresh_rate'
CONFIG_APP_LOG_PATH   = 'app_log_path'
CONFIG_EXCEL_PATH     = 'excel_path' 

CONFIG_APP_SETTING = ['refresh_status', 'refresh_rate', 'app_log_path', 'excel_path']

### function that creates the config file for the application 
def create_app_config_file():
    config = configparser.ConfigParser()

    ### create the settings configuration 
    config['settings'] = {
        'refresh_status' : 'false',
        'refresh_rate'   : '',
        'app_log_path'   : 'resources/logs/',
        'excel_path'     : 'resources/spreadsheets/'
    }

    with open('resources/config/application-config.ini', 'w') as config_file:
        config.write(config_file)

### flags used for the database config gile
CONFIG_DB_LOG_PATH    = 'db_log_path'
CONFIG_DB_LAST_UPDATE = 'db_last_update'

CONFIG_DB_SETTINGS = ['db_log_path', 'db_last_update']
### function that creates a config file for the database
def create_db_config_file():
    config = configparser.ConfigParser()

    ### create the database configuration 
    config['settings'] = {
        'db_log_path'    : '',
        'db_last_update' : ''
    }

    with open('resources/config/database-config.ini', 'w') as config_file:
        config.write(config_file)

def init_config_files():
    ### check for the existence of a config file
    db_config_path  = not os.path.exists('resources/config/database-config.ini')
    app_config_path = not os.path.exists('resources/config/application-config.ini') 

    if db_config_path and app_config_path:
        create_db_config_file()
        create_app_config_file()
        
    elif db_config_path:
        create_db_config_file()

    elif app_config_path:
        create_app_config_file()

    else:
        print("config files already exist...")
