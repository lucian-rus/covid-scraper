from scraper import *
from database import *
print("additional information about this application as well as the code can be found at the link https://github.com/lucian-rus/covid-scraper. type 'help' for a list of commands")

### todo
#   implement the basic ui and commands
#   implement a global macro file and remove the file specific macros  
#   implement database and link it to the scraper - partially done
#   scrape for total tests - done
#       * the total number of tests will be used to calculate the tests done in the current day
#       * based on this, we can calculate the infection rate (new_tests / new_cases) to provide a better insight
#   link the configuration to the scraper 
#   add a save_to_spreadsheet option (for both current and previous day as well as database tables)
#   create a log file
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

### MACROS
RUN  = 1
EXIT = 0
LOOP = RUN

### flags used to determine which day to scrape based on the tables name
CURRENT_DAY  = '#main_table_countries_today tr'
PREVIOUS_DAY = '#main_table_countries_yesterday tr'

### aplication loop
while LOOP:
    user_input = input('cs-command> ')

    if user_input == 'exit':
        LOOP = EXIT
    elif user_input == 'help':
        command_help()
    elif user_input == 'scrapecday':
        scrape_current_day(CURRENT_DAY)
    elif user_input == 'scrapepday':
        scrape_current_day(PREVIOUS_DAY)
    elif user_input == 'exportrxls':
        command_error()
    elif user_input == 'debug':
        connect_database()
    else:
        command_error()