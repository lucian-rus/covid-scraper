import pandas

class ScrapedData:
    ### class constructor containing all the scraped data
    def __init__(self, id, country_name, total_cases, new_cases, total_deaths, new_deaths, population):
        self.id            = id
        self.country_name  = country_name
        self.total_cases   = total_cases
        self.new_cases     = new_cases
        self.total_deaths  = total_deaths
        self.new_deaths    = new_deaths 
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
    population    = []
        
    for obj in list_raw:
        country_name.append(obj.country_name)
        total_cases.append(obj.total_cases)
        new_cases.append(obj.new_cases)
        total_deaths.append(obj.total_deaths)
        new_deaths.append(obj.new_deaths)
        population.append(obj.population)
    
    table_raw = pandas.DataFrame(list(zip(country_name, total_cases, new_cases, total_deaths, new_deaths, population)),
                                columns = ['country', 'total cases', 'new cases', 'total deaths', 'new_deaths', 'population'])
    pandas.set_option('display.max_rows', MAX_ROWS)
    return table_raw

ERROR = 400
### print the raw data 
def print_raw(data_raw):
    dataframe_raw = create_dataframe(data_raw)
    print(dataframe_raw)
    


        
