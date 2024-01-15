import geopandas as gpd
import matplotlib.pyplot as plt

warsaw_gdf = gpd.read_file('warszawa-dzielnice.geojson')

mapa = warsaw_gdf.plot(figsize=(10, 10), edgecolor='black', linewidth=0.5, color=warsaw_gdf["color"], legend=True)	

mapa.set_title('Miejsca w Warszawie, w których autobusy\n przekraczały prędkość 50 km/h', fontdict={'fontsize': 15, 'fontweight': 'medium'})

plt.show()