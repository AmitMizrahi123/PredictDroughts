import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = r'https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_area'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
div = soup.find('table')
table = pd.read_html(str(div))[0]

table = table.drop(columns=['Rank', '% land', '% water'], level=1)
table = table.drop(table.index[[55, 56, 57, 58, 59]])
table = table.sort_values([('State', 'State')], ascending=True)
table.reset_index(drop=True, inplace=True)
table = table.drop(table.index[[2, 35, 47]])
table.reset_index(drop=True, inplace=True)
table = table.drop(columns='Total area[2]', level=0)
table.to_csv('files/state_info.csv')

aland = [float(x) * 1000 for x in table['Land area[2]']['km2']]
awater = [float(x) * 1000 for x in table['Water[2]']['km2']]
aland_sqmi = [float(x) * 0.62 for x in table['Land area[2]']['sq mi']]
awater_sqmi = [float(x) * 0.62 for x in table['Water[2]']['sq mi']]

data = {
    'State': table['State']['State'],
    'Aland': aland,
    'Awater': awater,
    'Aland_SQMI': aland_sqmi,
    'Awater_SQMI': awater_sqmi,
}

df = pd.DataFrame(data)

df.to_csv('files/state_info.csv')