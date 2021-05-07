import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696')
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", attrs={"class": "data"})
i = 0

stateName = []
postalCode = []
fips = []

for data in table.find_all("td"):
    if i % 3 == 0:
        stateName.append(data.text.replace("\r\n\t\t\t\t", ""))
    elif i % 3 == 1:
        postalCode.append(data.text.replace("\r\n\t\t\t\t", ""))
    else:
        fips.append(data.text.replace("\r\n\t\t\t\t", ""))
    i += 1

data = {
    "state name": stateName,
    "potal code": postalCode,
    "fips": fips
}

df = pd.DataFrame(data)
print(df.shape)