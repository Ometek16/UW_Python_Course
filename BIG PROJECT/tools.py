import numpy as np

EARTH_RADIUS = 6371000.0


def get_distance(point_A, pointB):
	"""
	:param point_A: tuple of floats (latitude, longitude)
	:param pointB: tuple of floats (latitude, longitude)
	:return: float
	"""
	lat_A, lon_A = point_A
	lat_B, lon_B = pointB

	lat_A = np.radians(lat_A)
	lon_A = np.radians(lon_A)
	lat_B = np.radians(lat_B)
	lon_B = np.radians(lon_B)

	dlon = lon_B - lon_A
	dlat = lat_B - lat_A

	a = np.sin(dlat / 2)**2 + np.cos(lat_A) * np.cos(lat_B) * np.sin(dlon / 2)**2
	c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

	return EARTH_RADIUS * c

def ms_to_kmh(speed):
	return speed * 3.6