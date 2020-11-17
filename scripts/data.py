### this file handles the dataframe related functions and printing

import pandas, os
from xlwt import Workbook

from macro import *

### todo
#   allow excel file exporting based on the dataframes
#   better document the code 
#   add function parameters description

class ScrapedData:
    ### class constructor containing all the scraped data
    def __init__(self, id, country_name, total_cases, new_cases, total_deaths,
                 new_deaths, total_tests, population):
        self.id            = id
        self.country_name  = country_name
        self.total_cases   = total_cases
        self.new_cases     = new_cases
        self.total_deaths  = total_deaths
        self.new_deaths    = new_deaths 
        self.total_tests   = total_tests
        self.population    = population

MAX_ROWS = 256
### create a dataframe ###
def create_dataframe(list_raw):
    country_name  = []
    total_cases   = []
    new_cases     = []
    total_deaths  = []
    new_deaths    = []
    total_tests   = []
    population    = []
        
    ### iterate through the raw list and create the dataframe
    for obj in list_raw:
        country_name.append(obj.country_name)
        total_cases.append(obj.total_cases)
        new_cases.append(obj.new_cases)
        total_deaths.append(obj.total_deaths)
        new_deaths.append(obj.new_deaths)
        total_tests.append(obj.total_tests)
        population.append(obj.population)
    
    table_raw = pandas.DataFrame(list(zip(country_name, total_cases, new_cases, total_deaths, new_deaths, total_tests, population)),
                                columns = ['country', 'total cases', 'new cases', 'total deaths', 'new deaths', 'total tests', 'population'])
    pandas.set_option('display.max_rows', MAX_ROWS)
    
    ### clear the lists after building the dataframe
    country_name.clear()
    total_cases.clear()
    new_cases.clear()
    total_deaths.clear()
    return table_raw

### print the raw data scraped 
def print_raw(data_raw):
    dataframe_raw = create_dataframe(data_raw)
    print(dataframe_raw)

NULL = 0
### function that export raw scraped data to a .xls file 
def export_raw_xlsx(data_raw):
    table_raw = create_dataframe(data_raw)

    try:
        dir_path = os.path.dirname(__file__)
        title = 'test.xls'
        path = '..\\resources\\spreadsheets\\' + title
        relative_path = os.path.relpath(path, dir_path)

        table_raw.to_excel(relative_path)
        print('table {} printed succesfully...'.format(title))
    except Exception as e:
        log_app_event(APP_LOG, ERROR, e)


        
