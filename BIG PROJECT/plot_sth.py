import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
import analyse_sth

warsaw_gdf = gpd.read_file('warszawa-dzielnice.geojson')

def line_in_Warsaw(line):
	return point_in_Warsaw(Point(line[0])) and point_in_Warsaw(Point(line[1]))

def point_in_Warsaw(point):
	is_inside_warsaw = False
	for index, district_polygon in warsaw_gdf.iterrows():
		if point.within(district_polygon['geometry']):
			is_inside_warsaw = True
			break
	return is_inside_warsaw

mapa = warsaw_gdf.plot(figsize=(10, 10), edgecolor='black', linewidth=0.5, color=warsaw_gdf["color"], legend=True)	

mapa.set_title('Miejsca w Warszawie, w których autobusy\n przekraczały prędkość 50 km/h', fontdict={'fontsize': 15, 'fontweight': 'medium'})

speeding_lines = list(filter(line_in_Warsaw, analyse_sth.get_speeding_lines()))

speeding_lines_gdf = gpd.GeoDataFrame(geometry=[LineString([line[0], line[1]]) for line in speeding_lines])
speeding_lines_gdf = speeding_lines_gdf.set_crs(epsg=4326)

# Plot the speeding lines
speeding_lines_gdf.plot(ax=mapa, color='red')

plt.show()