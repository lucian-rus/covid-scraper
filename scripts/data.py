### this file handles the dataframe related functions and printing

import pandas, os
import xlrd

from macro import *
from configuration import *

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
    
    log_event(APP_LOG, INFO, 'new dataframe created')
    ### clear the lists after building the dataframe
    country_name.clear()
    total_cases.clear()
    new_cases.clear()
    total_deaths.clear()
    return table_raw

### print the raw data scraped 
def print_raw(data_raw):
    dataframe_raw = create_dataframe(data_raw)
    log_event(APP_LOG, INFO, 'printed requested dataframe to the terminal')
    print(dataframe_raw)

### flags that signal the the way the raw data will be exported
TO_CSV  = 81
TO_XLS  = 82
TO_JSON = 83

### function that export raw scraped data to a .xls file 
def export_raw(target, data_raw):
    table_raw = create_dataframe(data_raw)

    cwd_path = os.path.dirname(__file__)
    
    if target == TO_XLS:    
        title = 'test.xls'
        path = get_config_data(CONFIG_APP_FILE_PATH, CONFIG_EXCEL_PATH) + title
    if target == TO_CSV:  
        title = 'test.csv'  
        path = get_config_data(CONFIG_APP_FILE_PATH, CONFIG_CSV_PATH) + title
    if target == TO_JSON:
        title = 'test.json'    
        path = get_config_data(CONFIG_APP_FILE_PATH, CONFIG_JSON_PATH) + title

    ### set relative path of the output file
    target_path = os.path.relpath(path, cwd_path)
    
    try:
        if target == TO_XLS:
            table_raw.to_excel(target_path)
            log_event(APP_LOG, INFO, 'exported the dataframe as .xls file ' + title)

        if target == TO_CSV:
            table_raw.to_csv(target_path)
            log_event(APP_LOG, INFO, 'exported the dataframe as .csv file ' + title)

        if target == TO_JSON:
            json_table = table_raw.to_json(orient='index')

            ### parse the dataframe with the json module
            parser = json.loads(json_table)
            with open(target_path, 'w') as out:
                json.dump(parser, out, indent=4)
            log_event(APP_LOG, INFO, 'exported the dataframe as .json file ' + title)

        print('dataframe {} exported succesfully...'.format(title))
    except Exception as e:
        log_event(APP_LOG, ERROR, e)

### function that is used to import data from files 
def import_raw(target_file):
    try:
        target = xlrd.open_workbook(target_file)
        sheet = target.sheet_by_index(0)
        
        ### save the imported data to a list
        raw_imported_data = []

        ### variables that store the scraped data 
        country_name  = NULL_DEF
        total_cases   = NULL_DEF
        new_cases     = NULL_DEF
        total_deaths  = NULL_DEF
        new_deaths    = NULL_DEF
        total_tests   = NULL_DEF
        population    = NULL_DEF
        country_id    = 1
        for i in range(sheet.nrows):
            if i > 1:
                country_name = sheet.cell_value(i, 1)
                total_cases  = sheet.cell_value(i, 2)
                new_cases    = sheet.cell_value(i, 3)
                total_deaths = sheet.cell_value(i, 4)
                new_deaths   = sheet.cell_value(i, 5)
                total_tests  = sheet.cell_value(i, 6)
                population   = sheet.cell_value(i, 7)

                raw_imported_data.append(ScrapedData(country_id, country_name, total_cases, 
                                new_cases, total_deaths, new_deaths, total_tests, population))
                country_id += 1

        return raw_imported_data

    except Exception as e:
        print(e)
    return NOT_OK

### function that creates a temporary file 
def export_temp_file(data_raw):
    table_raw = create_dataframe(data_raw)

    cwd_path = os.path.dirname(__file__)
    path = get_config_data(CONFIG_APP_FILE_PATH, CONFIG_TEMP_PATH)

    target_path = os.path.relpath(path, cwd_path)
    json_table = table_raw.to_json(orient='index')

    try:
        ### parse the dataframe with the json module
        parser = json.loads(json_table)
        with open(target_path, 'w') as out:
            json.dump(parser, out, indent=4)
        log_event(APP_LOG, INFO, 'exported the dataframe as temporary file')

    except Exception as e:
        log_event(APP_LOG, ERROR, e)