import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stuff = pd.read_csv('/Users/dhirenkakkar/nwHacksProject2019/backend/data.csv')

m = folium.Map([49.26743,-123.2529], zoom_start=11)

for index, row in stuff.iterrows():
    folium.CircleMarker([row['49.26743'], row['-123.2529']],
                        radius=15,
                        popup=row['Pay For Print'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)

stationArr = stuff[['49.26743', '-123.2529']].as_matrix()

m.add_children(plugins.HeatMap(stationArr, radius=30))
f = open("chart.html", "w+")
f.write(m._repr_html_())
f.close()



