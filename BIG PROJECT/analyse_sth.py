import os
import json
from datetime import datetime
from tools import get_distance

def transform_data_to_simple_dict(data):
	simple_data = dict()
	for bus in data['result']:
		simple_data[bus['VehicleNumber']] = {"Lon": bus['Lon'], "Lat": bus['Lat'], "Time": bus['Time']}
	return simple_data

def get_speeding_lines(dataSet=1):
	speeding_lines = []
	
	path = os.path.join("DATA_SETS", f"DATA_SET_{dataSet}")

	file_count = sum(1 for item in os.listdir(path) if os.path.isfile(os.path.join(path, item)))

	prev_file_path = os.path.join(path, "0.json")
	prev_file = open(prev_file_path, "r")
	prev_data = transform_data_to_simple_dict(json.load(prev_file))

	for i in range(1, file_count):
		curr_file_path = os.path.join(path, f"{i}.json")
		curr_file = open(curr_file_path, "r")
		curr_data = transform_data_to_simple_dict(json.load(curr_file))
	
		for key in prev_data:
			prev = prev_data.get(key)
			curr = curr_data.get(key)
			if (prev == None or curr == None):
				continue
		
			prev_time = datetime.strptime(prev["Time"], '%Y-%m-%d %H:%M:%S')
			curr_time = datetime.strptime(curr["Time"], '%Y-%m-%d %H:%M:%S')

			time_diff = curr_time - prev_time
			if (time_diff.seconds == 0):
				continue

			distance = get_distance((prev["Lat"], prev["Lon"]), (curr["Lat"], curr["Lon"]))
			velocity = (distance / time_diff.seconds) * 3.6
		
			if (velocity > 50):
				speeding_lines.append(((prev["Lon"], prev["Lat"]), (curr["Lon"], curr["Lat"])))

		prev_file.close()
		prev_file = curr_file
		prev_data = curr_data
	
	prev_file.close()
 
	return speeding_lines
