'''
python3 parser_3.py --months january march --days mon-tue fri --time m e
python3 parser_3.py --months january march --days mon-tue fri-wed
python3 parser_3.py --months january february march --days mon-tue fri fri-wed --time m e m e 
'''

import argparse
import os
import pathlib
import csv
import random

_day_id_names = {"mon" : [0, "monday"], "tue" : [1, "tuesday"], "wed" : [2, "wednesday"], 
             "thu" : [3, "thursday"], "fri" : [4, "friday"], "sat" : [5, "saturday"], "sun" : [6, "sunday"]}

_time_names = {"m" : "morning", "e" : "evening"}

_time_cnt = 0

def parse_day(day):
	if (len(day) == 3):
		return [_day_id_names[day][1]]
	low = _day_id_names[day[0:3]][0]
	high = _day_id_names[day[4:7]][0]
 
	ans = []
	for i in range(low, high + 1):
		for key in _day_id_names:
			val = _day_id_names[key]
			if val[0] == i:
				ans.append(val[1])
    
	if (high < low):
		for i in range(low, 7):
			for key in _day_id_names:
				val = _day_id_names[key]
				if val[0] == i:
					ans.append(val[1])
		for i in range(0, high + 1):
			for key in _day_id_names:
				val = _day_id_names[key]
				if val[0] == i:
					ans.append(val[1])
	return ans

def get_time(time):
	global _time_cnt
	_time_cnt += 1
	if (_time_cnt - 1>= len(time)):
		return _time_names["m"]
	return _time_names[time[_time_cnt - 1]]

def get_data():
	data = []
	data.append(random.choice(['A', 'B', 'C']))
	data.append(random.randint(0, 1000))
	data.append(str(random.randint(0, 1000)) + "ms")
	return data


parser = argparse.ArgumentParser()

parser.add_argument("--months", help="select months", nargs="+")
parser.add_argument("--days", help="select days", nargs="+")
parser.add_argument("--time", help="select time", nargs="*")

args = parser.parse_args()

args.days = [parse_day(day) for day in args.days]

# print(args)

n = len(args.months)

data_path = os.path.join(os.getcwd(), "DATA_3")

for i in range(n):
	for day in args.days[i]:
		new_path = os.path.join(data_path, args.months[i].capitalize(), day, get_time(args.time))
		if not os.path.exists(new_path):
			os.makedirs(new_path)
		
		with open(os.path.join(new_path, "Solutions.csv"), "w") as file:
			writer = csv.writer(file)
			writer.writerow(["Model", "Output value", "Time of computation"])
			writer.writerow(get_data())

total_time_of_computation_A = 0

for month in os.listdir(data_path):
	for day in os.listdir(os.path.join(data_path, month)):
		for time in os.listdir(os.path.join(data_path, month, day)):
			solution_path = os.path.join(data_path, month, day, time, "Solutions.csv")
			with open(solution_path, "r") as solutions_file:
				reader = list(csv.reader(solutions_file))
				# print(reader)
				if (reader[1][0] == "A"):
					total_time_of_computation_A += (int) (reader[1][2][:-2])

print("Total time of computation for model A: ", total_time_of_computation_A, "ms", sep="")