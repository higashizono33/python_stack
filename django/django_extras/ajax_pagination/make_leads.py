from leads_app.models import Lead
import random
import pandas as pd

from datetime import datetime, timedelta

def rand_first_name():
    names = ['Michael', 'Joe', 'Steve', 'Robert', 'Josh', 'Henry', 'Tory', 'Damian', 'Donovan', 'Cade']
    i = random.randint(0,9)
    name = names[i]
    # email = f"{name}@example.com"
    # print(email)
    return name

def rand_last_name():
    names = ['James', 'Mitchell', 'Smith', 'Jordan', 'Haywood', 'Choi', 'Carter', 'Trump', 'Jones', 'Cunningham']
    i = random.randint(0,9)
    name = names[i]

    return name

def rand_date(min_year=2016, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    random_date = start + (end - start) * random.random()
    new_random_date = random_date.strftime('%Y-%m-%d')
    return new_random_date

def make_lead():
        first_name = rand_first_name() 
        last_name = rand_last_name()
        email = f"{first_name.lower()}@example.com"
        registered_at = rand_date()
        
        Lead.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            registered_at = registered_at,
        )

def make_leads():
    for i in range(1, 100):
        first_name = rand_first_name()
        last_name = rand_last_name()
        email = f"{first_name.lower()}@example.com"
        registered_at = rand_date()
        
        Lead.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            registered_at = registered_at,
        )