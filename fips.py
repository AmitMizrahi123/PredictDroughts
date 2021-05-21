import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function that return fips data
def returnFipsDataFrame():
    response = requests.get(r'https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696')
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", attrs={"class": "data"})

    stateName = []
    postalCode = []
    fips = []

    for index, data in enumerate(table.find_all("td")):
        if index % 3 == 0:
            stateName.append(data.text.replace("\r\n\t\t\t\t", ""))
        elif index % 3 == 1:
            postalCode.append(data.text.replace("\r\n\t\t\t\t", ""))
        else:
            fips.append(data.text.replace("\r\n\t\t\t\t", ""))
    
    stateName.insert(8, 'District of Columbia')
    postalCode.insert(8, 'DC')
    fips.insert(8, 11)

    data = {
        "state name": stateName,
        "potal code": postalCode,
        "fips": fips
    }

    df = pd.DataFrame(data)
    df.drop(df.index[[51, 52, 53, 55]], inplace=True)
    df.sort_values('state name', ascending=True, inplace=True)

    return df