import pandas as pd

dfDrought = pd.read_csv('files/drought.csv')
dfMeteorological = pd.read_csv('files/meteorological.csv')
dfStateInfo = pd.read_csv('files/state_info.csv')

dfMeteorological.drop(columns='week', inplace=True)
dfMeteorological['Week'] = dfDrought['Week']
dfMeteorological['LEVEL'] = dfDrought['LEVEL']

for col in dfStateInfo.columns:
    dfMeteorological[col] = dfStateInfo[col]

dfMerge = dfMeteorological.drop(columns='Unnamed: 0')
dfMerge = dfMerge[['Week', 'State', 'GeoId', 'Longitude', 'Latitude', 'PRECTOT' ,'WS10M_MIN' ,'QV2M' ,'T2M_RANGE' ,'WS10M' ,'T2M' ,'WS50M_MIN' ,'T2M_MAX' ,'WS50M' ,'TS' ,'WS50M_RANGE' ,'WS50M_MAX' ,'WS10M_MAX' ,'WS10M_RANGE' ,'PS' ,'T2MDEW', 'T2M_MIN', 'T2MWET', 'Aland', 'Awater', 'Aland_SQMI', 'Awater_SQMI', 'LEVEL']]

dfMerge.to_csv('files/merge.csv')