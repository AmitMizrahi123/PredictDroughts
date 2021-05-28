import requests
from bs4 import BeautifulSoup
import pandas as pd

def getLonAndLat():
    url = r'https://developers.google.com/public-data/docs/canonical/states_csv'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('table')
    table = pd.read_html(str(div))[0]
    table.sort_values('name', ascending=True, inplace=True)
    lon = table['longitude'].to_list()
    lat = table['latitude'].to_list()
    return lon, lat

def returnLastWeekDate():
    df = pd.read_csv('files/drought.csv')
    return df['Week'][0]

def returnFirstWeekDate():
    df = pd.read_csv('files/drought.csv')
    firstWeek = returnNumberOfWeeks()
    return df['Week'][firstWeek]

def returnNumberOfWeeks():
    df = pd.read_csv('files/drought.csv')
    weekLines = len(df.loc[df['State'] == 'Alabama'])
    return weekLines

def returnStates():
    df = pd.read_csv('files/fips.csv')
    states = df['state name']
    return states