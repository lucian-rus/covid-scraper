import requests, bs4
import schedule, time

from data import *

### todo
#   better document the code 
#   add function parameters description
#   implement action specific functions

### macros used across the entire file
NULL_INT = 0
NULL_DEF = ''
NULL_STR = '0'

### macros used by the get_cell_data function as parameters that specify the string format
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

### macros used to determine in which table cell the iterator can be found
SCRAPER_COUNTRY_NAME = 1
SCRAPER_TOTAL_CASES  = 2
SCRAPER_NEW_CASES    = 3
SCRAPER_TOTAL_DEATHS = 4
SCRAPER_NEW_DEATHS   = 5
SCRAPER_TOTAL_TESTS  = 12
SCRAPER_POPULATION   = 14

### store the scraped data globally for easier access
RAW_SCRAPED_DATA  = []

### url of the page that is going to be scraped
PAGE_URL = 'https://www.worldometers.info/coronavirus/'

### scrape for the desired data 
def scrape_current_day(TABLE):
    page = requests.get(PAGE_URL)
    
    ### keep track of how many countries the parser find
    country_id = NULL_INT

    ### parse table with bs4
    page_soup = bs4.BeautifulSoup(page.text, 'html.parser')

    ### iterate through the desired table
    for table_row in page_soup.select(TABLE):
        
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
        RAW_SCRAPED_DATA.append(ScrapedData(country_id, country_name, total_cases, 
                                new_cases, total_deaths, new_deaths, total_tests, population))
    print_raw(RAW_SCRAPED_DATA)
