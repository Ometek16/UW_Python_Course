import geopandas as gpd
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
from shapely.geometry import Point, LineString
from alive_progress import alive_it
from tools import bcolors
import numpy as np
import json
import matplotlib.ticker as mticker
import matplotlib.image as mpimg


def prepare_plot(ax, pos, name, data):
	total_count = sum(data.values())
	# Calculate percentages
	percentages = {key: (value / total_count) * 100 for key, value in data.items()}

	# Plotting the percentages
	
	ax[pos].bar(percentages.keys(), percentages.values())
	ax[pos].set_title(f"{name}", fontsize=8)

	# Format y-axis tick labels as percentages
	formatter = mticker.PercentFormatter()
	ax[pos].yaxis.set_major_formatter(formatter)

	# Set smaller font size for x and y labels
	ax[pos].tick_params(axis='x', labelsize=4)
	ax[pos].tick_params(axis='y', labelsize=4)

	# Set x-axis ticks to [0, 20, 40, 60]
	ax[pos].set_xticks([0, 20, 40, 60])
 

def plot_data_set_schedule(dataSet: int = 1) -> None:
	with open(f"./FILTERED_DATA/FILTERED_POSITIONS/filtered_positions_{dataSet}.json", "r") as file:
		data = json.load(file)
		
	time_diffs = map(lambda x: (x[0] // 60, x[1]), map(lambda x: (x["Time"], x["District"]), data))

	delay_per_district = dict()
	delay_total = dict()
 
	for time_diff in time_diffs:
		if (time_diff[1] not in delay_per_district):
			delay_per_district[time_diff[1]] = dict()
		delay_per_district[time_diff[1]][time_diff[0]] = delay_per_district[time_diff[1]].get(time_diff[0], 0) + 1
		delay_total[time_diff[0]] = delay_total.get(time_diff[0], 0) + 1


	fig, ax = plt.subplots(4, 5, gridspec_kw={'hspace': 0.5})
	fig.suptitle('Opóźnienia w Warszawie w poszczególnych dzielnicach')
	

	plt.get_current_fig_manager().full_screen_toggle()
 
	positions = [(0, i) for i in range(5)] + [(i, j) for i in range(1, 3) for j in (0, 1, 3, 4)] + [(3, i) for i in range(5)]
	idx = 0

	for district in list(sorted(delay_per_district.keys())):
		prepare_plot(ax, positions[idx], district, delay_per_district[district])
		idx += 1

	img = mpimg.imread('bus.webp')
	ax[2, 2].imshow(img)
	ax[2, 2].axis('off')
	
	prepare_plot(ax, (1, 2), "WARSZAWA", delay_total)

	plt.show()


plot_data_set_schedule(2)    
        
    