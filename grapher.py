from folium import plugins
from folium.plugins import HeatMap
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt, mpld3
import numpy as np
import folium
import stats
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

def pieChart(startDate, endDate):
    ratios = stats.pieChart(startDate, endDate)
    fig1, ax1 = plt.subplots()
    x = np.char.array(ratios.keys())
    y = np.array(ratios.values())
    colors = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120), (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150), (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148), (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199), (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
    porcent = 100.*y/y.sum()
    for i in range(len(colors)):    
        r , g, b = colors[i]    
        colors[i] = (r / 255., g / 255., b / 255.)
    patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, porcent)]
    sort_legend = True
    if sort_legend:
        patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))

    plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)
    plt.savefig('./Templates/piechart.png', bbox_inches='tight')

def timeSeries():
    

pieChart("01-01-2001", "01-01-2100")


