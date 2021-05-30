import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation

stateDf = pd.read_csv('files/state_info.csv', encoding="ISO-8859-1")
stateDf = stateDf[['GeoId', 'Aland_SQMI', 'Longitude', 'Latitude']]
drDf = pd.read_csv('files/drought.csv')

drDf['Week'] = pd.to_datetime(drDf['Week'], format='%Y-%m-%d')
drDf.drop(columns=['State', 'Unnamed: 0'], axis=1, inplace=True)

drDf = drDf.set_index('Week').groupby(['Fips']).resample('M').mean().reset_index(level=1)

drDf = drDf.rename_axis(None)

dr_final = pd.merge(drDf, stateDf, left_on='Fips', right_on='GeoId', how='inner', sort='False')
dr_final = dr_final[['Fips', 'Week', 'LEVEL', 'Aland_SQMI', 'Longitude', 'Latitude']]
dr_final = dr_final.sort_values('Week').reset_index(drop=True)
dr_final = dr_final.groupby('Fips')

fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)
m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49, projection='lcc', lat_1=33, lat_2=45, lon_0=-95)
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

anim = FuncAnimation(plt.gcf(), update, interval=200, repeat=False, frames=203, blit=True)
anim.save('wow/Heatmap_animation_US_Drought.gif', writer='imagemagick')