### this file handles the scraping of the table

import requests, bs4
import schedule

from data import *
from macro import *
### todo
#   better document the code 
#   add function parameters description
#   implement action specific functions
#   implement returns for the functions to check if everything went as intended

### table cell x coordinates based on the data tables
SCRAPER_COUNTRY_NAME = 1
SCRAPER_TOTAL_CASES  = 2
SCRAPER_NEW_CASES    = 3
SCRAPER_TOTAL_DEATHS = 4
SCRAPER_NEW_DEATHS   = 5
SCRAPER_TOTAL_TESTS  = 12
SCRAPER_POPULATION   = 14

### coordinates for the specific data
SCRAPER_CASES     = 0
SCRAPER_DEATHS    = 1
SCRAPER_RECOVERED = 2

### url of the page that is going to be scraped
PAGE_URL = 'https://www.worldometers.info/coronavirus/'

### initiate the page scraping
def init_scraper(target_type, target):
    print('requesting page...')

    ### create a request
    page = requests.get(PAGE_URL)
    ### parse table with bs4
    page_soup = bs4.BeautifulSoup(page.text, 'html.parser')
    log_app_event(APP_LOG, INFO, 'succesfully connected to the target page')
  
    if target_type == TABLE:
        return scrape_table_data(page_soup, target)
    else:
        return scrape_page_data(page_soup, target_type)


### specify the string format
CASE  = 10
TOTAL = 20

### function used to get the text from a table cell 
def get_cell_data(cell_data, str_format):
    result = NULL_STR

    ### check if the data is null
    if len(cell_data) == NULL_DEF:
        result = NULL_STR
    else:
        result = cell_data

    ### remove the '+' character from the number of new cases
    if str_format == CASE and result != NULL_STR:
        result = result[1:]

    return result 

### scrape the data from the data tables   
def scrape_table_data(page_soup, target):
    print('scraping table...')

    ### keep track of number of countries
    country_id = NULL_INT

    ### save the scraped table data into a list
    raw_scraped_data = []

    ### iterate through the desired table
    for table_row in page_soup.select(target):

        ### keep track of the current cell in the table
        cell_it = NULL_INT

        ### variables that store the scraped data 
        country_name  = NULL_DEF
        total_cases   = NULL_DEF
        new_cases     = NULL_DEF
        total_deaths  = NULL_DEF
        new_deaths    = NULL_DEF
        total_tests   = NULL_DEF
        population    = NULL_DEF

        ### test cases to find and store desired data 
        for table_cell in table_row.findAll('td'):

            ### scrape the name of the country
            if cell_it == SCRAPER_COUNTRY_NAME:
                aux = table_cell.find('a')
                if aux == None:
                    country_name = "SKIP"
                    break
                else: 
                    country_name = aux.get_text()
                    country_id += 1 

            ### scrape the total number of cases
            if cell_it == SCRAPER_TOTAL_CASES:
                total_cases = get_cell_data(table_cell.get_text(), TOTAL)
            ### scrape the new number of cases
            if cell_it == SCRAPER_NEW_CASES:
                new_cases = get_cell_data(table_cell.get_text(), CASE)
            ### scrape the total number of deaths
            if cell_it == SCRAPER_TOTAL_DEATHS:
                total_deaths = get_cell_data(table_cell.get_text(), TOTAL)
            ### scrape the new number of deaths
            if cell_it == SCRAPER_NEW_DEATHS:
                new_deaths = get_cell_data(table_cell.get_text(), CASE)
            ### scrape the total number of tests
            if cell_it == SCRAPER_TOTAL_TESTS:
                total_tests = get_cell_data(table_cell.get_text(), TOTAL)
            ### scrape the population of the country
            if cell_it == SCRAPER_POPULATION:
                population = get_cell_data(table_cell.get_text(), TOTAL)

            ### increment the cell counter
            cell_it += 1

        ### create list of objects with number of cases per country ###
        if country_name == "SKIP":
            continue
        raw_scraped_data.append(ScrapedData(country_id, country_name, total_cases, 
                                new_cases, total_deaths, new_deaths, total_tests, population))
    return raw_scraped_data

### scrape data from the page
def scrape_page_data(page_soup, target_type):
    print('scraping data...')
    result = page_soup.find_all('div', {'class': 'maincounter-number'})

    res_counter = NULL_INT

    ### check which data has been requested
    for obj in result:
        if target_type == CASES and res_counter == SCRAPER_CASES: 
            return obj.get_text()
        if target_type == DEATHS and res_counter == SCRAPER_DEATHS:
            return obj.get_text()
        if target_type == RECOVERED and res_counter == SCRAPER_RECOVERED:
            return obj.get_text()
        res_counter += 1

    return NOT_OK

### print the raw scraped data
def print_raw_data(target_type, target):
    if target_type == TABLE:
        print_raw(init_scraper(target_type, target))

    ### get the current local date and time
    current_time = datetime.datetime.now().strftime('%d-%m-%Y, %H:%M local time')

    ### 
    if target_type == CASES:
        result = init_scraper(target_type, target)
        print('as of {}, the total number of cases is: {}'.format(current_time, result))
    if target_type == DEATHS:
        result = init_scraper(target_type, target)
        print('as of {}, the total number of deaths is: {}'.format(current_time, result))
    if target_type == RECOVERED:
        result = init_scraper(target_type, target)
        print('as of {}, the total number of recoveries is: {}'.format(current_time, result))

### returns the raw scraped data as a list
def get_raw_table_data(target_type, target):
    return init_scraper(target_type, target)