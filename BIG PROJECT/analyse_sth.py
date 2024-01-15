import os
import json
from datetime import datetime
from tools import calculate_distance
from typing import Dict, List

MS_TO_KMH = 3.6


def get_important_data(raw_data: List[Dict]) -> Dict:
    '''Returns a dictionary with important bus data from all API data'''
    data = dict()
    for bus_info in raw_data['result']:
        data[bus_info['VehicleNumber']] = {
            "Position": (bus_info['Lon'], bus_info['Lat']),
            "Time": bus_info['Time']
        }

    return data


def collect_all_segments(dataSet: int = 1) -> List:
    all_segments = []

    data_path = os.path.join("DATA_SETS", f"DATA_SET_{dataSet}")

    file_count = sum(1 for item in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, item)))

    prev_file_path = os.path.join(data_path, "0.json")
    prev_file = open(prev_file_path, "r")
    prev_data = get_important_data(json.load(prev_file))

    for i in range(1, file_count):
        curr_file_path = os.path.join(data_path, f"{i}.json")
        curr_file = open(curr_file_path, "r")
        curr_data = get_important_data(json.load(curr_file))

        for VehicleNumber in prev_data:
            prev = prev_data.get(VehicleNumber)
            curr = curr_data.get(VehicleNumber)
            
            # If the bus is not in the current data set, skip it
            if (curr is None):
                continue

            prev_time = datetime.strptime(prev["Time"], '%Y-%m-%d %H:%M:%S')
            curr_time = datetime.strptime(curr["Time"], '%Y-%m-%d %H:%M:%S')
            time_diff = curr_time - prev_time
            
            # If the bus has not moved, skip it
            if (time_diff.seconds == 0):
                continue

            distance = calculate_distance(prev["Position"], curr["Position"])
            velocity = (distance / time_diff.seconds) * MS_TO_KMH

            all_segments.append((prev["Position"], curr["Position"], velocity))

        prev_file.close()
        prev_file = curr_file
        prev_data = curr_data

    prev_file.close()

    return all_segments
