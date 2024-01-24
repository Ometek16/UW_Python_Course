import geopandas as gpd
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from shapely.geometry import Point, LineString
from alive_progress import alive_it
from tools import bcolors
import numpy as np

SPEED_LIMIT = 50

def plot_data_set_speed(dataSet: int = 1) -> None:
    all_segments = open(os.path.join("DATA_SETS", f"filtered_segments_{dataSet}.csv"), "r").readlines()[1:]
    speeding_segments_in_warsaw = []
    district_counter = dict()
    district_speeding_counter = dict()

    for segment in alive_it(all_segments, title=bcolors.OKCYAN+ "Filtering segments..." + bcolors.ENDC):
        segment = segment.split(",")
        start_position = (float(segment[0]), float(segment[1]))
        end_position = (float(segment[3]), float(segment[4]))

        district_counter[segment[2]] = district_counter.get(segment[2], 0) + 1
        district_counter[segment[5]] = district_counter.get(segment[5], 0) + 1	

        # If the bus was speeding but did not magically teleport 
        if 150 > float(segment[6]) > 50:
            speeding_segments_in_warsaw.append((start_position, end_position))
            district_speeding_counter[segment[2]] = district_speeding_counter.get(segment[2], 0) + 1
            district_speeding_counter[segment[5]] = district_speeding_counter.get(segment[5], 0) + 1


    speeding_percentage = dict()

    for district in district_counter:
        if district in district_speeding_counter:
            speeding_percentage[district] = district_speeding_counter[district] / district_counter[district] * 100
 
    speeding_percentage_sorted = sorted(speeding_percentage.items(), key=lambda item: item[1])
 
    speeding_lines_gdf = gpd.GeoDataFrame(geometry=[LineString([line[0], line[1]]) for line in speeding_segments_in_warsaw])
    speeding_lines_gdf = speeding_lines_gdf.set_crs(epsg=4326)

    # Load the Warsaw districts GeoJSON file
    warsaw_gdf = gpd.read_file('warszawa-dzielnice.geojson')
 
    # plot the map
    mapa = warsaw_gdf.plot(figsize=(12, 10), edgecolor='black', linewidth=0.5, color=warsaw_gdf["color"], legend=True)	
    mapa.set_title('Miejsca w Warszawie, w których autobusy\nprzekraczały prędkość 50 km/h', fontdict={'fontsize': 15, 'fontweight': 'medium'})
    
    for district, percentage in speeding_percentage_sorted:
        mapa.scatter([], [], label=f'{district}: {round(percentage, 2)}%', marker="none")

    # Display the legend
    mapa.legend(title="Procnt autobusów\nprzekraczających prędkość\ndla każdej dzielnicy", loc='center left', bbox_to_anchor=(1, 0.5), fontsize='medium', handlelength=0)


    # Plot the speeding lines
    print(bcolors.OKCYAN + "Plotting..." + bcolors.ENDC)
    speeding_lines_gdf.plot(ax=mapa, color='red')

    plt.show()
 