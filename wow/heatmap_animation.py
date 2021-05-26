import pandas as pd

stateDf = pd.read_csv('files/state_info.csv', encoding="ISO-8859-1")
stateDf = stateDf[['GeoId', 'Aland_SQMI', 'Longitude', 'Latitude']]

drDf = pd.read_csv('files/drought.csv')

drDf['Week'] = pd.to_datetime(drDf['Week'])
num_m = len(drDf.Week.unique())
drDf.drop(columns=['State', 'Unnamed: 0'], axis=1, inplace=True)

drDf['LEVEL'] = (drDf['D4'] * 5 + (drDf['D3-D4'] - drDf['D4']) * 4 + (drDf['D2-D4'] - drDf['D3-D4']) * 3 + (drDf['D1-D4'] - drDf['D2-D4']) * 2 + (drDf['D0-D4'] - drDf['D1-D4'])) /100

dr_final = pd.merge(drDf, stateDf, left_on='Fips', right_on='GeoId', how='inner', sort='False')
dr_final = dr_final[['Fips', 'Week', 'LEVEL', 'Aland_SQMI', 'Longitude', 'Latitude']]
dr_final = dr_final.sort_values('Week')
dr_final = dr_final.groupby('Fips')


import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
m.drawcoastlines()
m.drawmapboundary(zorder=0)
m.fillcontinents(color='#ffffff',zorder=1)
m.drawcountries(linewidth=1)
m.drawstates()

x, y = m(dr_final.nth(0).Longitude.tolist(), dr_final.nth(0).Latitude.tolist())
colors = (dr_final.nth(0).LEVEL).tolist()
sizes = (dr_final.nth(0).Aland_SQMI / 7.5).tolist()
cmap = plt.cm.YlOrRd
sm = ScalarMappable(cmap=cmap)
plt.title('US Drought Level (Year-Month): ' + dr_final.nth(0).Week.iloc[0].strftime('%Y-%m'))

scatter = ax.scatter(x,y,s=sizes,c=colors,cmap=cmap,alpha=1,edgecolors='face',marker='H',vmax=5,vmin=0,zorder=1.5)
plt.colorbar(scatter)

def update(ii):
    colors = (dr_final.nth(ii).LEVEL).tolist()
    scatter.set_color(sm.to_rgba(colors))
    plt.title('US Drought Level (Year-Month): ' + dr_final.nth(ii).Week.iloc[0].strftime('%Y-%m'))
    return scatter, 

anim = FuncAnimation(plt.gcf(), update, interval=40, repeat=False, frames=1100, blit=True)
anim.save('wow/Heatmap_animation_US_Drought.gif', writer='imagemagick')