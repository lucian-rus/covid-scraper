import configparser
import os 

### macros used for passing the status of a function
NULL   = 0

### macros used as parameters for config file edits
LOG_PATH       = 'log_path'
REFRESH_RATE   = 'refresh_rate'
XLSX_PATH      = 'xlsx_path' 

DB_FILE_PATH   = 'db_file_path'
DB_LAST_UPDATE = 'db_last_update'

COUNTRY_NAME   = 'country_name'
TOTAL_CASES    = 'total_cases'
NEW_CASES      = 'new_cases'   
CASES_STATUS   = 'cases_status'  
TOTAL_DEATHS   = 'total_deaths'  
NEW_DEATHS     = 'new_deaths'    
DEATHS_STATUS  = 'deaths_status' 
CASES_BY_POP   = 'cases_by_pop'  
DEATHS_BY_POP  = 'deaths_by_pop'
POPULATION     = 'population'    

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
        'refresh_rate': ''
    }

    ### create the database configuration 
    config['database'] = {
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
