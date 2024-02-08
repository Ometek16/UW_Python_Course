import numpy as np
from typing import Tuple, NewType
import requests
import time, json

Coordinates = NewType('Coordinate', Tuple[float, float])
EARTH_RADIUS = 6371000.0


def calculate_distance(point_A: Coordinates, point_B: Coordinates) -> float:
    '''Calculates distance between two points on Earth using Haversine formula.'''
    lon_A, lat_A = point_A
    lon_B, lat_B = point_B

    lat_A, lon_A = np.radians(lat_A), np.radians(lon_A)
    lat_B, lon_B = np.radians(lat_B), np.radians(lon_B)

    lon_diff = lon_B - lon_A
    lat_diff = lat_B - lat_A

    # Magic formula calculating distance between two points on Earth
    a = np.sin(lat_diff / 2)**2 + np.cos(lat_A) * np.cos(lat_B) * np.sin(lon_diff / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return EARTH_RADIUS * c

def force_response(url, params, i, timeout=100, allowFail=False):
    error_count = 0
    error_message = ""
    response = {"result": []}
    # Get data from UM API
    while (True):
        try:
            response = requests.get(url, params=params).json()
        except:
            error_count += 1
        
        if len(response['result']) == 0 or response['result'][0] == 'B':
            error_count += 1
            
            if (error_message == "" and not allowFail):
                print(bcolors.WARNING + "[ERROR]" + bcolors.ENDC)
                
            error_message = f"[ERROR] Could not get data from UM API. ({error_count})"
            if (not allowFail):
                print(bcolors.PREV_LINE + bcolors.MOVE_RIGHT * (5 + len(str(i))) + bcolors.WARNING + error_message + bcolors.ENDC)
            time.sleep(0.1)
        else:
            break
        
        if (error_count >= timeout):
            if (not allowFail):
                print(bcolors.PREV_LINE + bcolors.MOVE_RIGHT * (5 + len(str(i))) + bcolors.FAIL + "[FAIL] Could not get data from UM API." + " " * 20 + bcolors.ENDC)
            return response
        
    if (error_message != "" and not allowFail):
        print(bcolors.PREV_LINE + bcolors.MOVE_RIGHT * (5 + len(str(i))) + bcolors.WARNING + error_message + bcolors.OKGREEN + " [OK]" + bcolors.ENDC)
    
    return response

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PREV_LINE = "\033[F"
    MOVE_RIGHT = "\033[C"
