import pandas as pd
import folium
from data.utilities import returnLastWeekDate

lastWeekdate = returnLastWeekDate()
locationStart = [35, -102]
zoomStart = 5

url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"

df = pd.read_csv('files/merge.csv')
dfFips = pd.read_csv('files/fips.csv')

df = df[['State', 'Week', 'LEVEL']]
df['State'] = df.State[df['Week'] == lastWeekdate]
df['LEVEL'] = df.LEVEL[df['Week'] == lastWeekdate]

state_data = df.drop(['Week', 'State'], axis=1)
state_data = state_data.dropna().reset_index(drop=True)
state_data.insert(0, 'State', dfFips['postal code'], True)

m = folium.Map(location=locationStart, zoom_start=zoomStart)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "LEVEL"],
    key_on="feature.id",
    fill_color="YlOrRd",
    highlight=True,
    fill_opacity=0.65,
    line_opacity=0.4,
    legend_name="Drought Today",
).add_to(m)

folium.LayerControl().add_to(m)

m.save('CurrentlyDrought.html')