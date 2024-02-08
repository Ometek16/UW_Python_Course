import os
import json
from datetime import datetime
from tools import calculate_distance, bcolors
from typing import Dict, List
from alive_progress import alive_bar, alive_it
from shapely.geometry import Point


def filter_positions(dataSet: int = 1) -> None:
    
    file_busStops = f"SCHEDULE/busStops.json"
    with open(file_busStops, 'r') as file:
        busStops = json.load(file)
    
    
    file_path = f"./FILTERED_DATA/VALID_POSITIONS/valid_positions_{dataSet}.json"
    with open(file_path, 'r') as file:
        valid_positions = json.load(file)
        
    filtered_positions = []
    
    for bus in alive_it(valid_positions, title=bcolors.OKCYAN+ "Filering positions..." + bcolors.ENDC, spinner='dots'):
        try:
            file_bus_positions = f"SCHEDULE/LINES/line_{bus["Line"]}.json"
            with open(file_bus_positions, 'r') as file:
                bus_positions = json.load(file)
        except:
            print(bcolors.WARNING + f"[ERROR] Line {bus["Line"]} does not exist." + bcolors.ENDC)
            continue

        # Bus does not exist in the schedule :)
        if (bus["Brigade"] not in bus_positions):
            continue
        
        # If a bus is over 1h late, it is not considered, as it is probably wrong
        bestTime = 3600
        
        bus_time = datetime.strptime(bus["Time"], "%Y-%m-%d %H:%M:%S").strftime("%H:%M:%S")

        for busStop in bus_positions[bus["Brigade"]]:
            # Bus stop does not exist :)
            if busStop not in busStops:
                continue
            
            busStopPosition = (float(busStops[busStop]["dlug_geo"]), float(busStops[busStop]["szer_geo"]))
            
            distance = calculate_distance(bus["Position"], busStopPosition)
            
            # To hard to check if bus is around any bus stop
            if (distance > 50):
                continue
            
            for curr_time in bus_positions[bus["Brigade"]][busStop]:
                if (int(curr_time[:2]) >= 24):
                    curr_time = str(int(curr_time[:2]) - 24) + curr_time[2:]
                time_diff = abs((datetime.strptime(curr_time, "%H:%M:%S") - datetime.strptime(bus_time, "%H:%M:%S")).seconds)
                
                bestTime = min(bestTime, time_diff)
            
            if (bestTime >= 3600):
                continue
            
            bus["Time"] = bestTime
            filtered_positions.append(bus)
            
    with open(f"./FILTERED_DATA/FILTERED_POSITIONS/filtered_positions_{dataSet}.json", "w") as file:
        json.dump(filtered_positions, file)
                
 
filter_positions(2)
    
    