import os, json, urllib, requests, webbrowser
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from lanAndLat import getLonAndLat

output = "JSON"

lon, lat = getLonAndLat()
locations = list(zip(lat, lon))
# locations = [(32.318231, -86.902298)]

output_folder = r''
base_url = r"https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint&tempAverage=DAILY&parameters=WS10M_MIN,QV2M,T2M_RANGE,WS10M,T2M,WS50M_MIN,T2M_MAX,WS50M,TS,WS50M_RANGE,WS50M_MAX,WS10M_MAX,WS10M_RANGE,PS,T2MDEW,T2M_MIN,T2MWET,PRECTOT&startDate=20000104&endDate=20210518&lat={latitude}&lon={longitude}&outputList={output}&userCommunity=SSE"

dfList = []

for latitude, longitude in tqdm(locations):
    api_request_url = base_url.format(longitude=longitude, latitude=latitude, output=output.upper())
    json_response = json.loads(requests.get(api_request_url).content)
    TIME = [key for key in json_response['features'][0]['properties']['parameter']['PRECTOT'].keys()]
    WS10M_MIN = [value for value in json_response['features'][0]['properties']['parameter']['WS10M_MIN'].values()]
    QV2M = [value for value in json_response['features'][0]['properties']['parameter']['QV2M'].values()]
    T2M_RANGE = [value for value in json_response['features'][0]['properties']['parameter']['T2M_RANGE'].values()]
    WS10M = [value for value in json_response['features'][0]['properties']['parameter']['WS10M'].values()]
    T2M = [value for value in json_response['features'][0]['properties']['parameter']['T2M'].values()]
    WS50M_MIN = [value for value in json_response['features'][0]['properties']['parameter']['WS50M_MIN'].values()]
    T2M_MAX = [value for value in json_response['features'][0]['properties']['parameter']['T2M_MAX'].values()]
    WS50M = [value for value in json_response['features'][0]['properties']['parameter']['WS50M'].values()]
    TS = [value for value in json_response['features'][0]['properties']['parameter']['TS'].values()]
    WS50M_RANGE = [value for value in json_response['features'][0]['properties']['parameter']['WS50M_RANGE'].values()]
    WS50M_MAX = [value for value in json_response['features'][0]['properties']['parameter']['WS50M_MAX'].values()]
    WS10M_MAX = [value for value in json_response['features'][0]['properties']['parameter']['WS10M_MAX'].values()]
    WS10M_RANGE = [value for value in json_response['features'][0]['properties']['parameter']['WS10M_RANGE'].values()]
    PS = [value for value in json_response['features'][0]['properties']['parameter']['PS'].values()]
    T2MDEW = [value for value in json_response['features'][0]['properties']['parameter']['T2MDEW'].values()]
    T2M_MIN = [value for value in json_response['features'][0]['properties']['parameter']['T2M_MIN'].values()]
    T2MWET = [value for value in json_response['features'][0]['properties']['parameter']['T2MWET'].values()]
    PRECTOT = [value for value in json_response['features'][0]['properties']['parameter']['PRECTOT'].values()]

    data = {
        'week': TIME,
        'PRECTOT': PRECTOT,
        'WS10M_MIN': WS10M_MIN,
        'QV2M': QV2M,
        'T2M_RANGE': T2M_RANGE,
        'WS10M': WS10M,
        'T2M': T2M,
        'WS50M_MIN': WS50M_MIN,
        'T2M_MAX': T2M_MAX,
        'WS50M': WS50M,
        'TS': TS,
        'WS50M_RANGE': WS50M_RANGE,
        'WS50M_MAX': WS50M_MAX,
        'WS10M_MAX': WS10M_MAX,
        'WS10M_RANGE': WS10M_RANGE,
        'PS': PS,
        'T2MDEW': T2MDEW,
        'T2M_MIN': T2M_MIN,
        'T2MWET': T2MWET,
        'PRECTOT': PRECTOT
    }

    df = pd.DataFrame(data)
    dfList.append(df)

dataframe = pd.DataFrame()
for df in dfList:
    dataframe = dataframe.append(df)
dataframe.reset_index(drop=True, inplace=True)

dataframe.to_csv('files/meteorological.csv')