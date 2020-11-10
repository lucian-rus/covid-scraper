import requests, bs4
import schedule, time
from selenium import webdriver

from data import *

### todo
#   refactor scraping conditions

### macros
NULL_INT = 0
NULL_DEF = ''
NULL_STR = '0'
PAGE_URL = 'https://www.worldometers.info/coronavirus/'

CURRENT_DAY_DATA  = []
PREVIOUS_DAY_DATA = []

### scrape for data regarding the current day and print it
def scrape_current_day():
    page = requests.get(PAGE_URL)

    no_of_countries   = NULL_INT

    ### parse table with bs4
    page_soup = bs4.BeautifulSoup(page.text, 'html.parser')
    for table_row in page_soup.select('#main_table_countries_today tr'):
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
            if cell_it == 1:
                aux = table_cell.find('a')
                if aux == None:
                    country_name = "SKIP"
                    break
                else: 
                    country_name = aux.get_text()
                    no_of_countries += 1 

            ### scrape the total number of cases
            if cell_it == 2:
                if len(table_cell.get_text()) == NULL_INT:
                    total_cases = NULL_STR
                else:
                    total_cases = table_cell.get_text()

            ### scrape the new number of cases
            if cell_it == 3:
                if len(table_cell.get_text()) == NULL_INT:
                    new_cases = NULL_STR
                else:
                    new_cases = table_cell.get_text()
                    new_cases = new_cases[1:]
            
            ### scrape the total number of deaths
            if cell_it == 4:
                if len(table_cell.get_text()) == NULL_INT:
                    total_deaths = NULL_STR
                else:
                    total_deaths = table_cell.get_text()

            ### scrape the new number of deaths
            if cell_it == 5:
                if len(table_cell.get_text()) == NULL_INT:
                    new_deaths = NULL_STR
                else:
                    new_deaths = table_cell.get_text()
                    new_deaths = new_deaths[1:]
            
            ### scrape the total number of tests
            if cell_it == 12:
                if len(table_cell.get_text()) == NULL_INT:
                    total_tests = NULL_STR
                else:
                    total_tests = table_cell.get_text()

            ### scrape the population of the country
            if cell_it == 14:
                if len(table_cell.get_text()) == NULL_INT:
                    population = NULL_STR
                else:
                    population = table_cell.get_text()
            
            cell_it += 1

        ### create list of objects with number of cases per country ###
        if country_name == "SKIP":
            continue
        CURRENT_DAY_DATA.append(ScrapedData(no_of_countries, country_name, total_cases, 
                                new_cases, total_deaths, new_deaths, total_tests, population))

    ### print the raw data
    #print_raw(CURRENT_DAY_DATA)

### function that returns the current day data
def get_current_day_data():
    scrape_current_day()
    return CURRENT_DAY_DATA

### scrape for data regarding the previous day a
def scrape_previous_day():
    browser = webdriver.Firefox()
    browser.get(PAGE_URL)
    page = requests.get(PAGE_URL)