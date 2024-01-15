import numpy as np
from typing import Tuple, NewType

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
