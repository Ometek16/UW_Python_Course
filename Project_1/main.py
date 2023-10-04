from random import random

def dist(x, y):
	return x**2 + y**2

all_points = 1000000
in_circle = 0

for _ in range(all_points):
	in_circle += (dist(random(), random()) <= 1)
	
print(4 * in_circle / all_points)
