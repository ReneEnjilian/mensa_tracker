from subprocess import call
import datetime
from datetime import date,  timedelta
from datetime import datetime as dt
import calendar
from mensa.time_calculator import calculate_days


def start_scrapers():
    dates = calculate_days()
    #call_cafeterias(dates)
    call_mathe_cafe()
    #call_personalkantine()

def call_cafeterias(dates):
    cafeteria_ids = ['321', '631', '540', '657', '538', '539']
    #cafeteria_ids = ['321', '631']
    for id in cafeteria_ids:
        for i in range(5):
            call(['scrapy', 'crawl', 'AllTU', '-a', 'id='+id, '-a', 'date='+dates[i]])

def call_mathe_cafe():
    call(['scrapy', 'crawl', 'Mathecafe'])

def call_personalkantine():
    call(['scrapy', 'crawl', 'Personalkantine'])

    

start_scrapers()

