import os, json, urllib, requests, webbrowser
from bs4 import BeautifulSoup
import pandas as pd
from utilities import getLonAndLat, returnLastWeekDate

output = "JSON"

lastWeekDate = str(returnLastWeekDate()).replace('-', '')
lon, lat = getLonAndLat()
locations = list(zip(lat, lon))
# locations = [(32.318231, -86.902298)]

output_folder = r''
base_url = r"https://power.larc.nasa.gov/cgi-bin/v1/DataAccess.py?request=execute&identifier=SinglePoint&tempAverage=DAILY&parameters=WS10M_MIN,QV2M,T2M_RANGE,WS10M,T2M,WS50M_MIN,T2M_MAX,WS50M,TS,WS50M_RANGE,WS50M_MAX,WS10M_MAX,WS10M_RANGE,PS,T2MDEW,T2M_MIN,T2MWET,PRECTOT&startDate=20000104&endDate=20210518&lat={latitude}&lon={longitude}&outputList={output}&userCommunity=SSE"

dfList = []

for latitude, longitude in locations:
    TIME = []
    WS10M_MIN = []
    QV2M = []
    T2M_RANGE = []
    WS10M = []
    T2M = []
    WS50M_MIN = []
    T2M_MAX = []
    WS50M = []
    TS = []
    WS50M_RANGE = []
    WS50M_MAX = []
    WS10M_MAX = []
    WS10M_RANGE = []
    PS = []
    T2MDEW = []
    T2M_MIN = []
    T2MWET = []
    PRECTOT = []

    api_request_url = base_url.format(longitude=longitude, latitude=latitude, output=output.upper())
    json_response = json.loads(requests.get(api_request_url).content)
    params = json_response['features'][0]['properties']['parameter']

    for index, date in enumerate(params['PRECTOT'].keys()):
        date = str(date)
        if index % 7 == 0:
            TIME.append(date)
            PRECTOT.append(params['PRECTOT'][date])
            WS10M_MIN.append(params['WS10M_MIN'][date])
            QV2M.append(params['QV2M'][date])
            T2M_RANGE.append(params['T2M_RANGE'][date])
            WS10M.append(params['WS10M'][date])
            T2M.append(params['T2M'][date])
            WS50M_MIN.append(params['WS50M_MIN'][date])
            T2M_MAX.append(params['T2M_MAX'][date])
            WS50M.append(params['WS50M'][date])
            TS.append(params['TS'][date])
            WS50M_RANGE.append(params['WS50M_RANGE'][date])
            WS50M_MAX.append(params['WS50M_MAX'][date])
            WS10M_MAX.append(params['WS10M_MAX'][date])
            WS10M_RANGE.append(params['WS10M_RANGE'][date])
            PS.append(params['PS'][date])
            T2MDEW.append(params['T2MDEW'][date])
            T2M_MIN.append(params['T2M_MIN'][date])
            T2MWET.append(params['T2MWET'][date])
            
        if date == lastWeekDate:
            index = 0

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
        'T2MWET': T2MWET
    }

    df = pd.DataFrame(data)
    dfList.append(df)

dataframe = pd.DataFrame()
for df in dfList:
    dataframe = dataframe.append(df)
dataframe.reset_index(drop=True, inplace=True)

dataframe.to_csv('files/meteorological.csv')