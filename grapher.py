from folium import plugins
from folium.plugins import HeatMap
import folium
import stats
import parser
import config

def heatMap():
    stats.loadData()
    m = folium.Map([49.2827, -123.1207], zoom_start=11)
    newData = []
    for x in range(0, len(config.data[0])):
        temp = [config.data[2][x], config.data[3][x]]
        newData.append(temp)
    HeatMap(newData).add_to(m)
    f = open("./Templates/heatmap.html", "w+")
    f.write(m._repr_html_())
    f.close()
