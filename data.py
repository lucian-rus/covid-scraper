import pandas
from xlwt import Workbook

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
    #cases_status  = []
    total_deaths  = []
    new_deaths    = []
    #deaths_status = []
    total_tests   = []
    population    = []
        
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
    return table_raw

### print the raw data scraped 
def print_raw(data_raw):
    dataframe_raw = create_dataframe(data_raw)
    print(dataframe_raw)

NULL = 0
### function that creates a .xlsx file based on the scraped data
def export_raw_xlsx(data_raw):
    
    ### create a new workbook and add a sheet
    write_file = Workbook()
    sheet = write_file.add_sheet('test')

    ### iterate through the raw data and write it to the file
    row = NULL
    for obj in data_raw:
        sheet.write(obj.id, 0, obj.country_name)
        sheet.write(obj.id, 1, obj.total_cases)
        sheet.write(obj.id, 2, obj.new_cases)
        sheet.write(obj.id, 3, obj.total_deaths)
        sheet.write(obj.id, 4, obj.new_deaths)
        sheet.write(obj.id, 5, obj.total_tests)
        sheet.write(obj.id, 6, obj.population)

    write_file.save('test.xls')
    print('done...')


        
