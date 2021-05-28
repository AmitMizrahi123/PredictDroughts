import pandas as pd
import matplotlib.pyplot as plt
import folium
from data.utilities import returnStates
import branca

df = pd.read_csv('files/merge.csv')
fipsDf = pd.read_csv('files/fips.csv')
states = returnStates()

colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 50e3)
level_series = df.set_index("Fips")["LEVEL"]

m = folium.Map(location=[48, -102], tiles="cartodbpositron", zoom_start=3)

def style_function(feature):
    employed = level_series.get(int(feature["id"][-5:]), None)
    return {
        "fillOpacity": 0.5,
        "weight": 0,
        "fillColor": "#black" if employed is None else colorscale(employed),
    }

folium.TopoJson(
    fipsDf['fips'],
    style_function=style_function,
).add_to(m)

m.save('m.html')

# dfLevelD0 = df[df['LEVEL'] == 0].reset_index(drop=True)
# dfLevelD1 = df[df['LEVEL'] == 1].reset_index(drop=True)
# dfLevelD2 = df[df['LEVEL'] == 2].reset_index(drop=True)
# dfLevelD3 = df[df['LEVEL'] == 3].reset_index(drop=True)
# dfLevelD4 = df[df['LEVEL'] == 4].reset_index(drop=True)
# sizes = [len(dfLevelD0), len(dfLevelD1), len(dfLevelD2), len(dfLevelD3), len(dfLevelD4)]
# labels = ['DO', 'D1', 'D2', 'D3', 'D4']
# explode = (0.05, 0.05, 0.05, 0.05, 0.05)
# fig, ax = plt.subplots()
# ax.pie(sizes,explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=180)
# ax.legend(bbox_to_anchor=(1.0, .5), prop={'size': 12})
# plt.title('Drought hist level count')
# plt.show()

# fig = plt.figure(figsize=(7, 7))
# ax = plt.axes()
# ax.scatter(df.Latitude, df.Longitude)
# ax.scatter(df.Latitude[df.LEVEL == 0], df.Longitude[df.LEVEL == 0], c='red')
# ax.scatter(df.Latitude[df.LEVEL == 1], df.Longitude[df.LEVEL == 1], c='green')
# ax.scatter(df.Latitude[df.LEVEL == 2], df.Longitude[df.LEVEL == 2], c='yellow')
# ax.scatter(df.Latitude[df.LEVEL == 3], df.Longitude[df.LEVEL == 3], c='black')
# ax.scatter(df.Latitude[df.LEVEL == 4], df.Longitude[df.LEVEL == 4], c='pink')
# plt.xlabel('Latitude')
# plt.ylabel('Longitude')
# ax.legend(bbox_to_anchor=(1.0, .5), prop={'size': 12})
# plt.show()

# df.LEVEL.hist(bins=20, grid=False, rwidth=0.8, color='blue', alpha=0.5)
# plt.xlabel('LEVEL')
# plt.ylabel('COUNT')
# plt.title('Drought hist level count')
# plt.show()

# sns.violinplot(df['LEVEL'], df['Awater']) # האורך של הקו (1,2) מראה על חריגים בגלל שיש הרבה נתונים אז חריגים פוטנציאלים
# plt.show()

# fig = plt.figure(figsize=(12, 7))
# ax = plt.axes()
# ax.scatter(df.Awater, df.LEVEL)
# plt.xlabel('Awater')
# plt.ylabel('Level')
# ax.scatter(df.Awater[df.LEVEL == 4], df.Aland[df.LEVEL == 4], c='black')
# plt.show()