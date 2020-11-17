### this file contains macros and functions that are used throughout the entire project

import logging, datetime, os

### general use macros
NULL   = 0
OK     = 1
NOT_OK = 0

### macros used inside the application loop 
RUN  = 1
EXIT = 0

### decide what data to be scraped 
CASES     = 101
DEATHS    = 102
RECOVERED = 103
TABLE     = 104

NULL_TARGET  = ''
CURRENT_DAY  = '#main_table_countries_today tr'
PREVIOUS_DAY = '#main_table_countries_yesterday tr'

### variable initialisation 
NULL_INT = 0
NULL_DEF = ''
NULL_STR = '0'

### log flags for the log function
INFO     = 41
DEBUG    = 42
ERROR    = 43
WARNING  = 44
CRITICAL = 45

### target flags for the logging process
APP_LOG  = 50
DB_LOG   = 60

### initialise the log file for the current session
def init_app_log_file():

    ### get the current date and time and name the file
    current_date = datetime.datetime.now()
    file_name   = current_date.strftime('%d%m%y-%H-%M-%S')
    file_path   = '..\\resources\\logs\\app-logs\\'
    log_file    =  file_path + file_name

    ### set the basic configuration for the logger and send the first message
    try:

        ### create relative path to the log directory 
        curr_path = os.path.dirname(__file__)
        new_path  = os.path.relpath(log_file, curr_path)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", datefmt='%H:%M:%S')

        ### setup the application logger
        logger  = logging.getLogger('app_logger')
        handler = logging.FileHandler(new_path)
        handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler) 

        ### initial log
        log_app_event(APP_LOG, INFO, 'application logfile ' + file_name + ' initiated')
    
        return OK
    except Exception as e:
        print(e)
        return NOT_OK

### initialise the db file for the current session    
def init_db_log_file():

    ### get the current date and time and name the file
    current_date = datetime.datetime.now()
    file_name   = current_date.strftime('%d%m%y-%H-%M-%S')
    file_path   = '..\\resources\\logs\\db-logs\\'
    log_file    =  file_path + file_name
    DB_LOGGER   = log_file

    ### set the basic configuration for the logger and send the first message
    try:

        ### create relative path to the log directory 
        curr_path = os.path.dirname(__file__)
        new_path  = os.path.relpath(log_file, curr_path)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s", datefmt='%H:%M:%S')

        ### setup the database logger
        logger  = logging.getLogger('db_logger')
        handler = logging.FileHandler(new_path)
        handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler) 

        ### initial log
        log_app_event(DB_LOG, INFO, 'database logfile ' + file_name + ' initiated')
    
        return OK
    except Exception as e:
        print(e)
        return NOT_OK

### log to file
def log_app_event(target_file, flag, log_message):

    ### placeholder logger
    logger = logging.getLogger('app_logger')
    
    ### check where to log
    if target_file == APP_LOG:
        logger = logging.getLogger('app_logger')
    if target_file == DB_LOG:
        logger = logging.getLogger('db_logger')

    if flag == INFO:
        logger.info(log_message)
    elif flag == DEBUG:
        logger.debug(log_message)
    elif flag == ERROR:
        logger.error(log_message)
    elif flag == WARNING:
        logger.warning(log_message)
    elif flag == CRITICAL:
        logger.critical(log_message)
    else:
        print('error logging')