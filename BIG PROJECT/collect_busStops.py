import requests
import json
import os

def get_info(info):
    good_info = dict()
    
    for dic in info["values"]:
        good_info[dic["key"]] = dic["value"]
  
    return good_info


api_key = "c7fc874d-fcff-4480-8671-f452e945b35a"  # API key for UM API
url = 'https://api.um.warszawa.pl/api/action/dbstore_get' # URL for UM API

# Parameters for UM API
params = {
	'apikey': api_key,
	# 'id': 'ab75c33d-3a26-4342-b36a-6e5fef0a3ac3',
	'id' : '1c08a38c-ae09-46d2-8926-4f9d25cb0630'
}

# Get data from UM API
response = requests.get(url, params=params).json()

busStops = dict()

for info in response['result']:
	info = get_info(info)
	key = "|".join((info["zespol"], info["slupek"]))
	busStops[key] = info

# Save to file
with open(os.path.join('./SCHEDULE','busStops_curr.json'), 'w') as file:
	json.dump(busStops, file)

