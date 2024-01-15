import os
import json
from datetime import datetime
from tools import get_distance

dataSet = 1

path = os.path.join("DATA_SETS", f"DATA_SET_{dataSet}")

file_count = sum(1 for item in os.listdir(path) if os.path.isfile(os.path.join(path, item)))

prev_file_path = os.path.join(path, "0.json")
prev_file = open(prev_file_path, "r")
prev_data = json.load(prev_file)

for i in range(1, file_count):
	curr_file_path = os.path.join(path, f"{i}.json")
	curr_file = open(curr_file_path, "r")
	curr_data = json.load(curr_file)
 
	prev = prev_data['result'][0]	
	curr = curr_data['result'][0]
 
	prev_time = datetime.strptime(prev["Time"], '%Y-%m-%d %H:%M:%S')
	curr_time = datetime.strptime(curr["Time"], '%Y-%m-%d %H:%M:%S')

	time_diff = curr_time - prev_time

	distance = get_distance((prev["Lat"], prev["Lon"]), (curr["Lat"], curr["Lon"]))


	print(prev)
	print(curr)
	print(time_diff, time_diff.seconds, distance, sep=" | ")
	print()
 
	prev_file.close()
	prev_file = curr_file
	prev_data = curr_data
 
prev_file.close()
