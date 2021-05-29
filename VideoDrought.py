import pandas as pd
from folium import Map
from folium.plugins import HeatMapWithTime

locationStart = [35, -102]
zoomStart = 5

df = pd.read_csv('files/merge.csv')

heatmap_time_data = list(df.groupby(['Week']))           
info = []
dates = []
for i in range(len(heatmap_time_data)):
    dates.append(heatmap_time_data[i][0])
    cur_date = []
    for j in list(map(list, zip(heatmap_time_data[i][1]['Latitude'], heatmap_time_data[i][1]['Longitude'], heatmap_time_data[i][1]['LEVEL'] / 10))) :
        cur_date.append(j)
    info.append(cur_date)

m = Map(location=locationStart, zoom_start=zoomStart)

gradient = {1: '#ffffb2', 0.7: '#fecc5c', 0.4: '#fd8d3c', 0.2: '#f03b20', 0.1: '#bd0026'}

HeatMapWithTime(data=info, index=dates, name='Drought', gradient=gradient).add_to(m)

m.save('VideoDrought.html')