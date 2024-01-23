import os
import json
from datetime import datetime
from tools import calculate_distance, bcolors
from typing import Dict, List
from alive_progress import alive_bar, alive_it
import geopandas as gpd
from shapely.geometry import Point
from itertools import product
from shapely.prepared import prep

MS_TO_KMH = 3.6

warsaw_gdf = gpd.read_file('warszawa-dzielnice.geojson')
warsaw_simple_gdf = gpd.read_file('warszawa-simple.geojson')
warsaw_prepared_polygon = [prep(geom) for geom in warsaw_gdf[1:]["geometry"]]
warsaw_simple_prepared_polygon = [prep(geom) for geom in warsaw_simple_gdf[1:]["geometry"]]


def point_in_simple_Warsaw(point):
    for index, prepared_polygon in enumerate(warsaw_simple_prepared_polygon):
        if prepared_polygon.contains(point):
            return warsaw_simple_gdf.loc[index + 1, "name"]
    
    return None


def point_in_Warsaw(point):
    simple = point_in_simple_Warsaw(point)
    if (simple is not None):
        return simple
    
    for index, prepared_polygon in enumerate(warsaw_prepared_polygon):
        if prepared_polygon.contains(point):
            return warsaw_simple_gdf.loc[index + 1, "name"]
    
    return None


def get_important_data(raw_data: List[Dict]) -> Dict:
    '''Returns a dictionary with important bus data from all API data'''
    data = dict()
    for bus_info in raw_data['result']:
        data[bus_info['VehicleNumber']] = {
            "Position": (bus_info['Lon'], bus_info['Lat']),
            "Time": bus_info['Time'],
            "Line": bus_info['Lines']
        }

    return data


def filter_and_save_segments(dataSet: int = 1) -> List:
    data_path = os.path.join("DATA_SETS", f"DATA_SET_{dataSet}")
    
    segments_file = open(os.path.join("DATA_SETS", f"filtered_segments_{dataSet}.csv"), "w")
    segments_file.write("start_lon,start_lat,start_district,end_lon,end_lat,end_district,velocity,line\n")

    file_count = sum(1 for item in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, item)))

    prev_file_path = os.path.join(data_path, "0.json")
    prev_file = open(prev_file_path, "r")
    prev_data = get_important_data(json.load(prev_file))

    # count vehicles in each file
    vehicles = 0
    for i in alive_it(range(0, file_count - 1), title=bcolors.OKCYAN+ "Estimating data size..." + bcolors.ENDC, spinner='dots'):
        curr_file_path = os.path.join(data_path, f"{i}.json")
        curr_file = open(curr_file_path, "r")
        vehicles += len(json.load(curr_file)["result"])
        curr_file.close()

    with alive_bar(vehicles, spinner='dots') as bar:
        bar.title(bcolors.OKCYAN+ "Generating segments..." + bcolors.ENDC)
        
        for i in range(1, file_count):
            curr_file_path = os.path.join(data_path, f"{i}.json")
            curr_file = open(curr_file_path, "r")
            curr_data = get_important_data(json.load(curr_file))

            for VehicleNumber in prev_data:
                prev = prev_data.get(VehicleNumber)
                curr = curr_data.get(VehicleNumber)
                
                # If the bus is not in the current data set, skip it
                if (curr is None):
                    bar(skipped=True)
                    continue

                try:
                    prev_time = datetime.strptime(prev["Time"], '%Y-%m-%d %H:%M:%S')
                    curr_time = datetime.strptime(curr["Time"], '%Y-%m-%d %H:%M:%S')
                    time_diff = curr_time - prev_time
                except:
                    print(bcolors.WARNING + "[ERROR] Could not parse time." + bcolors.ENDC)
                    bar(skipped=True)
                    continue
                
                # If the bus has not moved, skip it or if it has moved more than 30 seconds ago
                if (time_diff.seconds < 10 or time_diff.seconds > 20):
                    bar(skipped=True)
                    continue

                distance = calculate_distance(prev["Position"], curr["Position"])
                velocity = (distance / time_diff.seconds) * MS_TO_KMH
                start_district = point_in_Warsaw(Point(prev["Position"]))
                end_district = point_in_Warsaw(Point(curr["Position"]))
                
                if (start_district is None or end_district is None):
                    bar(skipped=True)
                    continue

                segments_file.write(f"{prev['Position'][0]},{prev['Position'][1]},{start_district},{curr['Position'][0]},{curr['Position'][1]},{end_district},{velocity},{prev['Line']}\n")
                bar(skipped=False)
                
            prev_file.close()
            prev_file = curr_file
            prev_data = curr_data

    prev_file.close()
    segments_file.close()
