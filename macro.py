### this file contains macros and files that are used throughout the entire project

import logging, datetime

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

### initialise the log file for the current session
def init_log_file():

    ### get the current date and time and name the file
    current_date = datetime.datetime.now()
    file_name = current_date.strftime('%d%m%y-%H-%M-%S')
    file_path = 'resources/logs/'
    log_file =  file_path + file_name

    ### set the basic configuration for the logger and send the first message
    try:
        logging.basicConfig(filename=log_file, filemode='w', level=logging.DEBUG, 
                        format="%(asctime)s | %(levelname)s | %(message)s", datefmt='%H:%M:%S')
        log(INFO, 'logfile ' + file_name + ' initiated')
    
        return OK
    except Exception as e:
        print(e)
        return NOT_OK
    

### log to file
def log(flag, log_message):

    if flag == INFO:
        logging.info(log_message)
    elif flag == DEBUG:
        logging.debug(log_message)
    elif flag == ERROR:
        logging.error(log_message)
    elif flag == WARNING:
        logging.warning(log_message)
    elif flag == CRITICAL:
        logging.critical(log_message)
    else:
        print('error logging')