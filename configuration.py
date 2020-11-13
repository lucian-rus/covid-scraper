### this file handles the configuration related functions

import configparser
import os 

from macros import *

### todo
#   better document the code 
#   add function parameters description

### constants used as placeholders for the config file keys
CONFIG_LOG_PATH       = 'log_path'
CONFIG_REFRESH_RATE   = 'refresh_rate'
CONFIG_XLSX_PATH      = 'xlsx_path' 

CONFIG_DB_FILE_PATH   = 'db_file_path'
CONFIG_DB_LAST_UPDATE = 'db_last_update'

CONFIG_COUNTRY_NAME   = 'country_name'
CONFIG_TOTAL_CASES    = 'total_cases'
CONFIG_NEW_CASES      = 'new_cases'   
CONFIG_CASES_STATUS   = 'cases_status'  
CONFIG_TOTAL_DEATHS   = 'total_deaths'  
CONFIG_NEW_DEATHS     = 'new_deaths'    
CONFIG_DEATHS_STATUS  = 'deaths_status' 
CONFIG_CASES_BY_POP   = 'cases_by_pop'  
CONFIG_DEATHS_BY_POP  = 'deaths_by_pop'
CONFIG_POPULATION     = 'population'    

SETTINGS     = {'log_path', 'refresh_rate'}
DATABASE     = {'db_file_path', 'db_last_update'}
TABLE_LAYOUT = {'country_name', 'total_cases', 'new_cases', 'cases_status',
                'total_deaths', 'new_deaths', 'deaths_status','cases_by_pop'  
                'deaths_by_pop', 'population'}

### function that creates the config file 
def create_config_file():
    config = configparser.ConfigParser()

    ### create the settings configuration 
    config['settings'] = {
        'log_path'    : '',
        'refresh_rate': '',
        'xls_path'    : ''
    }

    ### create the database configuration 
    config['database'] = {
        'db_file_exists' : '',
        'db_file_path'   : '',
        'db_last_update' : ''
    }

    ### create the output table configuration 
    config['table_layout'] = {
        'country_name'  : 'true',
        'total_cases'   : 'false',
        'new_cases'     : 'true',
        'cases_status'  : 'true',
        'total_deaths'  : 'false',
        'new_deaths'    : 'false',
        'deaths_status' : 'false',
        'cases_by_pop'  : 'true',
        'deaths_by_pop' : 'false',
        'total_cases'   : 'false',
        'population'    : 'true'
    }

    with open('./config.ini', 'w') as config_file:
        config.write(config_file)

### function that gets a property from the config file
#
# param_1: key   -> dictates where modifications will be made
def get_config_property(key):
    check = False

    ### check what section the key belongs to
    for it in SETTINGS:
        if it == key:
            check   = True
            section = 'settings'

    for it in DATABASE:
        if it == key:
            check   = True 
            section = 'database'
    
    for it in TABLE_LAYOUT:
        if it == key:
            check   = True 
            section = 'table_layout'
    
    if not check:
        return NULL

    ### create the parser and iterate through the file 
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    
    value = parser.get(section, key)
    if value == '':
        return NULL

    return value

def config_init():
    ### check for the existence of a config file
    config_file = not os.path.exists('config.ini')

    if config_file:
        create_config_file()
    else:
        print('config file already exists')
