import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from analyse_sth import collect_all_segments

SPEED_LIMIT = 50

# Load the Warsaw districts GeoJSON file
warsaw_gdf = gpd.read_file('warszawa-dzielnice.geojson')

def line_in_Warsaw(line):
    start_district = point_in_Warsaw(Point(line[0]))
    end_district = point_in_Warsaw(Point(line[1]))
    if (start_district is None or end_district is None):
        return None
    return (start_district, end_district)

def point_in_Warsaw(point):
    for index, district_polygon in warsaw_gdf[1:].iterrows():
        if point.within(district_polygon['geometry']):
            return district_polygon["name"]
    return None

all_segments = collect_all_segments(2)	
speeding_segments_in_warsaw = []
district_counter = dict()
district_speeding_counter = dict()

for segment in all_segments:
    districts = line_in_Warsaw((segment[0], segment[1]))
    if (districts is None):
        continue

    district_counter[districts[0]] = district_counter.get(districts[0], 0) + 1
    district_counter[districts[1]] = district_counter.get(districts[1], 0) + 1	

    if segment[2] > 50:
        speeding_segments_in_warsaw.append((segment[0], segment[1]))
        district_speeding_counter[districts[0]] = district_speeding_counter.get(districts[0], 0) + 1
        district_speeding_counter[districts[1]] = district_speeding_counter.get(districts[1], 0) + 1


speeding_percentage = dict()

for district in district_counter:
    if district in district_speeding_counter:
        speeding_percentage[district] = district_speeding_counter[district] / district_counter[district] * 100

print(speeding_percentage)

speeding_lines_gdf = gpd.GeoDataFrame(geometry=[LineString([line[0], line[1]]) for line in speeding_segments_in_warsaw])
speeding_lines_gdf = speeding_lines_gdf.set_crs(epsg=4326)

# plot the map
mapa = warsaw_gdf.plot(figsize=(10, 10), edgecolor='black', linewidth=0.5, color=warsaw_gdf["color"], legend=True)	
mapa.set_title('Miejsca w Warszawie, w których autobusy\n przekraczały prędkość 50 km/h', fontdict={'fontsize': 15, 'fontweight': 'medium'})

# Plot the speeding lines
speeding_lines_gdf.plot(ax=mapa, color='red')

plt.show()