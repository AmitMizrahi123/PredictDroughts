import pandas as pd
from folium import Map
from folium.plugins import HeatMapWithTime

locationStart = [35, -102]
zoomStart = 5

df = pd.read_csv('files/merge.csv')
df = list(df.groupby('Week'))

dates = []
info = []

for i in range(len(df)):
    dates.append(df[i][0])
    cur_date = []
    for j in list(map(list, zip(df[i][1]['Latitude'], df[i][1]['Longitude'], df[i][1]['LEVEL'] / 10))):
        cur_date.append(j)
    info.append(cur_date)

m = Map(location=locationStart, zoom_start=zoomStart)

HeatMapWithTime(data=info, index=dates, name='Drought').add_to(m)

m.save('VideoDrought.html')