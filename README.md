# covid-scraper

## Reasoning
This Python application represents a web scraper that was designed to scrape data about COVID-19 from the website https://www.worldometers.info/. The idea was born from a personal desire to study the evolution of the virus by monitoring the daily evolution of the number of new cases in my home country. 

## Application overview
Currently, the application scrapes 7 points of interest from the data tables:\
* `country_name` - the name of the country 
* `total_cases`  - the total number of cases in the given country 
* `new_cases` - the number of new cases in the given country 
* `total_deaths` - the total number of deaths in the given country 
* `new_deaths` - the number of new deaths in the given country 
* `total_cases` - the number of total cases in the country 
* `population` - the population of the country 

What to expect from further updates to this project:
* local database containing data from previously scraped days
* integrated statistics
* more user control regarding what is being scraped and how it is stored and displayed
* fully automated scraping at a user defined time rate

## Notes
* the specific webpage that is being parsed by this application can be found [here](https://www.worldometers.info/coronavirus/). *This project is currently work in progress.*
* this is my first fully-fledged project written in Python, so updates may not come as often as I'd want to since I'm learning the language while working on it


