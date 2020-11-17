### this file handles the CLI related functions

from scraper import *
from database import *
from macro import *
from configuration import *

### initial message
print("additional information about this application as well as the code can be found at the link https://github.com/lucian-rus/covid-scraper. type 'help' for a list of commands")

### create application log file for the current session
if not init_app_log_file():
    print('error creating application log file...')

### create database log file for the current session
if not init_db_log_file():
    print('error creating database log file...')

### check for the existence of the configuration file
#init_config_file()

### todo
#   implement the basic ui and commands
#   implement database and link it to the scraper - partially done
#   scrape for total tests - done
#       * the total number of tests will be used to calculate the tests done in the current day
#       * based on this, we can calculate the infection rate (new_tests / new_cases) to provide a better insight
#   link the configuration to the scraper 
#   use fire module to implement a better cli 
#   better document the code 
#   add function parameters description

### function that prints an error
def command_error():
    print('unknown command')

### function that prints the available commands
def command_help():
    print('HELP             - prints a list of implemented commands')
    print('EXIT             - exits the applcation')
    print('EXPORTRXLS       - export a .xlsx data file with data about the current day')
    print('SCRAPECDAY       - prints data about the current day')
    print('SCRAPEPDAY       - prints data about the previous day')
    print('CURRDAYDATA      - prints data about the previous day')
    print('     -c          - prints the total number of cases')
    print('     -d          - prints the total number of deaths')
    print('     -r          - prints the total number of recoveries')

### set the application loop to true
LOOP = RUN

### aplication loop
while LOOP:
    user_input = input('cs-command> ')

    if user_input == 'exit':
        log_app_event(APP_LOG, INFO, 'logfile stopped')
        log_app_event(DB_LOG, INFO, 'logfile stopped')
        LOOP = EXIT
    elif user_input == 'help':
        command_help()
    elif user_input == 'scrapecday':
        print_raw_data(TABLE, CURRENT_DAY)
    elif user_input == 'scrapepday':
        print_raw_data(TABLE, PREVIOUS_DAY)
    elif user_input == 'exportrxls':
        data_raw = get_raw_table_data(TABLE, '#main_table_countries_yesterday tr')
        export_raw_xlsx(data_raw)
    elif user_input == 'currdaydata':
        aux_input = input()
        if aux_input == '-c':
            print_raw_data(CASES, NULL_TARGET)
        if aux_input == '-d':
            print_raw_data(DEATHS, NULL_TARGET)
        if aux_input == '-r':
            print_raw_data(RECOVERED, NULL_TARGET)
    elif user_input == 'debug':
        log_app_event(DB_LOG, INFO, 'TEST')
    else:
        command_error()