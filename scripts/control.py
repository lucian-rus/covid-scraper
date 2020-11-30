### this file handles the CLI related functions

import time

from threading import *
from scraper import *
from database import *
from macro import *
from configuration import *

### initial message
print("additional information about this application as well as the code can be found at the link https://github.com/lucian-rus/covid-scraper. type 'help' for a list of commands")

### create application log file for the current session
if not init_app_log_file():
    print('error creating application log file...')

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
    print('EXPORTRAWDATA    - export raw data files')
    print('     -x          - exports the raw data as a .xls file')
    print('     -j          - exports the raw data as a .json file')
    print('     -c          - exports the raw data as a .csv file')
    print('SCRAPECDAY       - prints data about the current day')
    print('SCRAPEPDAY       - prints data about the previous day')
    print('CURRDAYDATA      - prints data about the previous day')
    print('     -c          - prints the total number of cases')
    print('     -d          - prints the total number of deaths')
    print('     -r          - prints the total number of recoveries')
    print('DEBUG            - placeholder command for development debug purposes, will be removed')
    print('DELETELOGS       - deletes all logs in specific the folder, except for the current session log file')
    print('     -a          - deletes the logs in the application log folder')
    print('     -d          - deletes the logs in the application log folder')

### function that acts as a newsfeed
def create_temp_file():
    data_raw = get_raw_table_data(TABLE, CURRENT_DAY)
    export_temp_file(data_raw)

### function that handles the applcation loopss
def application_loop(status):
    ### set the application loop to true
    LOOP = status

    ### aplication loop
    while LOOP:
        user_input = input('cs-command> ')

        if user_input == 'exit':
            
            update_config_data(CONFIG_APP_FILE_PATH, CONFIG_REFRESH_STATUS, FALSE)
            update_config_data(CONFIG_APP_FILE_PATH, CONFIG_REFRESH_RATE, NULL_TARGET)
            
            log_event(APP_LOG, INFO, 'logfile stopped')
            
            LOOP = EXIT
        elif user_input == 'help':
            command_help()
        elif user_input == 'scrapecday':
            print_raw_data(TABLE, CURRENT_DAY)
        elif user_input == 'scrapepday':
            print_raw_data(TABLE, PREVIOUS_DAY)
        elif user_input == 'exportrawdata':
            aux_input = input()
            if aux_input == '-x':
                data_raw = get_raw_table_data(TABLE, '#main_table_countries_yesterday tr')
                export_raw(TO_XLS, data_raw)
            if aux_input == '-c':
                data_raw = get_raw_table_data(TABLE, '#main_table_countries_yesterday tr')
                export_raw(TO_CSV, data_raw)
            if aux_input == '-j':
                data_raw = get_raw_table_data(TABLE, '#main_table_countries_yesterday tr')
                export_raw(TO_JSON, data_raw)
        elif user_input == 'currdaydata':
            aux_input = input()
            if aux_input == '-c':
                print_raw_data(CASES, NULL_TARGET)
            if aux_input == '-d':
                print_raw_data(DEATHS, NULL_TARGET)
            if aux_input == '-r':
                print_raw_data(RECOVERED, NULL_TARGET)
        elif user_input == 'deletelogs':
            aux_input = input()
            if aux_input == '-a':
                aux_input2 = input('are you sure you want to delete all the logs in the specified folder? you might lose some important information. [y] for yes: ')
                if aux_input2 == 'y':
                    delete_log_files(APP_LOG)
            if aux_input == '-d':
                aux_input2 = input('are you sure you want to delete all the logs in the specified folder? you might lose some important information. [y] for yes: ')
                if aux_input2 == 'y':
                    delete_log_files(DB_LOG)
        elif user_input == 'debug':
            data_raw = import_raw('..\\resources\\output\\xls\\date22112020.xls')
            print_raw(data_raw)
        elif user_input == 'resetconfig':
            init_config_files()
            log_event(APP_LOG, INFO, 'requested configuration files reset')
        elif user_input == 'connectdb':
            if not init_db_log_file():
                print('error creating database log file...')
            create_new_table()
            insert_into_table('ok')
            print_from_table()
        elif user_input == 'createtable':
            print('ok')
        elif user_input == 'newsfeed':
            update_config_data(CONFIG_APP_FILE_PATH, CONFIG_REFRESH_STATUS, TRUE)
            timer = input('timer for refresh rate (in seconds): ')
            timer = int(timer)
            update_config_data(CONFIG_APP_FILE_PATH, CONFIG_REFRESH_RATE, timer)

            log_event(APP_LOG, INFO, 'newsfeed enabled with a refresh rate of {} minutes '.format(timer/60))

            create_temp_file()
        else:
            command_error()

### main function of the application
def main():

    ### check if there is a path to the config files
    config_file = CONFIG_DB_FILE_PATH
    curr_path   = os.path.dirname(__file__)
    target_path = os.path.relpath(config_file, curr_path)

    ### if not, create the config files and run the application loop
    ### this function is a placeholder for a future better implementation
    config_path = not os.path.exists(target_path)
    if config_path:
        init_config_files()

    application_loop(RUN)

main_thread = Thread(target = main)
main_thread.start()
log_event(APP_LOG, INFO, 'main_thread started')
main_thread.join()

#scrape_thread.start()
#scrape_thread.join
