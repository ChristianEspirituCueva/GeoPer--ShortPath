import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap

url_data = 'https://raw.githubusercontent.com/juaneladio/peru-geojson/master/peru_departamental_simple.geojson'


#lista de 25 colores en blanco
cmap = ListedColormap(['white' for _ in range(25)],name='test')

#plotear la figura con esa lista y lineas de color negro
region_geojson = gpd.read_file(url_data)
region_geojson.head()
region_geojson.plot(figsize=(20,20),edgecolor='black',cmap=cmap)
#etiquetas de la figura
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.show()


