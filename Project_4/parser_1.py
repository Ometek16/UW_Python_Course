'''
python3 parser_1.py styczeń,luty pn-wt,pt r,w
python3 parser_1.py styczeń,marzec pn-cz,śr-pn
'''
import sys

day_id_names = {"pn" : [0, "poniedziałek"], "wt" : [1, "wtorek"], "śr" : [2, "środa"], 
             "cz" : [3, "czwartek"], "pt" : [4, "piątek"], "so" : [5, "sobota"], "nd" : [6, "niedziela"]}

time_names = {"r" : "rano", "w" : "wieczorem"}

def parse_day(day):
	if (len(day) == 2):
		return [day_id_names[day][1]]
	low = day_id_names[day[0:2]][0]
	high = day_id_names[day[3:5]][0]
 
	ans = []
	for i in range(low, high + 1):
		for key in day_id_names:
			val = day_id_names[key]
			if val[0] == i:
				ans.append(val[1])
    
	if (high < low):
		for i in range(low, 7):
			for key in day_id_names:
				val = day_id_names[key]
				if val[0] == i:
					ans.append(val[1])
		for i in range(0, high + 1):
			for key in day_id_names:
				val = day_id_names[key]
				if val[0] == i:
					ans.append(val[1])
	return ans

def get_time(time, time_cnt):
	if (time_cnt >= len(time)):
		return time_names["r"]
	return time_names[time[time_cnt]]

params = sys.argv + ["r"]

months = params[1].split(',')
days = params[2].split(',')
time = params[3].split(',')

days = [parse_day(day) for day in days]

n = len(months)
time_cnt = 0

for i in range(n):
	for day in days[i]:
		print(months[i].capitalize(), day, get_time(time, time_cnt))
		time_cnt += 1

