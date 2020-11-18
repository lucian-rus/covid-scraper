### this file contains macros and functions that are used throughout the entire project

import logging, datetime
import os, shutil

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

### flags related to the log directories
APP_LOG_DIR_PATH = '..\\resources\\logs\\app-logs\\'
DB_LOG_DIR_PATH  = '..\\resources\\logs\\db-logs\\'

CURRENT_SESSION_APP_LOG = NULL_STR
CURRENT_SESSION_DB_LOG  = NULL_STR

### initialise the log file for the current session
def init_app_log_file():

    ### get the current date and time and name the file
    current_date = datetime.datetime.now()
    file_name    = current_date.strftime('%d%m%y-%H-%M-%S')
    file_path    = APP_LOG_DIR_PATH
    log_file     = file_path + file_name

    ### set the name of the current session app log file to avoid deletion
    CURRENT_SESSION_APP_LOG = file_name

    ### set the basic configuration for the logger and send the first message
    try:

        ### create relative path to the log directory 
        curr_path = os.path.dirname(__file__)
        new_path  = os.path.relpath(log_file, curr_path)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | - %(message)s", datefmt='%H:%M:%S')

        ### setup the application logger
        logger  = logging.getLogger('app_logger')
        handler = logging.FileHandler(new_path)
        handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler) 

        ### initial log
        log_event(APP_LOG, INFO, 'application logfile ' + file_name + ' initiated')
    
        return OK
    except Exception as e:
        print(e)
        return NOT_OK

### initialise the db file for the current session    
def init_db_log_file():

    ### get the current date and time and name the file
    current_date = datetime.datetime.now()
    file_name    = current_date.strftime('%d%m%y-%H-%M-%S')
    file_path    = DB_LOG_DIR_PATH
    log_file     = file_path + file_name

    ### set the name of the current session db log file to avoid deletion
    CURRENT_SESSION_DB_LOG = file_name

    ### set the basic configuration for the logger and send the first message
    try:

        ### create relative path to the log directory 
        curr_path = os.path.dirname(__file__)
        new_path  = os.path.relpath(log_file, curr_path)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | - %(message)s", datefmt='%H:%M:%S')

        ### setup the database logger
        logger  = logging.getLogger('db_logger')
        handler = logging.FileHandler(new_path)
        handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler) 

        ### initial log
        log_event(DB_LOG, INFO, 'database logfile ' + file_name + ' initiated')
    
        return OK
    except Exception as e:
        print(e)
        return NOT_OK

### function that deletes all the log files that are not used by the current session
def delete_log_files(target_directory):
    directory       = NULL_STR
    current_session = NULL_STR
    log_event(target_directory, INFO, 'deleting log files from the target directory: {}'.format(target_directory))

    ### select which log directory is the target based on the flag
    if target_directory == APP_LOG:
        directory       = APP_LOG_DIR_PATH
        current_session = CURRENT_SESSION_APP_LOG 

    if target_directory == DB_LOG:
        directory       = DB_LOG_DIR_PATH
        current_session = CURRENT_SESSION_DB_LOG

    ### chunk of code got from https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
    for filename in os.listdir(directory):
        
        ### skip the current session log file
        if current_session == filename:
            continue
        
        file_path = os.path.join(directory, filename)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            log_event(target_directory, ERROR, 'Failed to delete {}. Reason: {}'.format(file_path, e))
    
    log_event(target_directory, INFO, 'log files deleted')
    print('done deleting log files...')

### log to file
def log_event(target_file, flag, log_message):

    ### placeholder logger
    logger = logging.getLogger('app_logger')
    
    ### check where to log
    if target_file == APP_LOG:
        logger = logging.getLogger('app_logger')
    if target_file == DB_LOG:
        logger = logging.getLogger('db_logger')

    ### check what flag has been triggered
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