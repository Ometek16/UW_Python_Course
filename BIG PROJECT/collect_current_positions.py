import requests
import json
import time
import os

api_key = "c7fc874d-fcff-4480-8671-f452e945b35a"  # API key for UM API
url = 'https://api.um.warszawa.pl/api/action/busestrams_get/' # URL for UM API

# Parameters for UM API
params = {
    'resource_id': 'f2e5503e-927d-4ad3-9500-4ab9e55deb59',
    'type':	'1',
	'apikey': api_key
}

# Directory path
directory = './DATA_SETS'

# Get the number of directories
num_directories = sum(1 for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item)))

# Create a new folder
new_folder_name = f'DATA_SET_{num_directories + 1}'
new_folder_path = os.path.join(directory, new_folder_name)
os.mkdir(new_folder_path)


# Collect data
for i in range(720):
	# Get data from UM API
	response = requests.get(url, params=params).json()

	print(f"Collected {i + 1} out of 720 data sets.")

	# Save to file
	path = os.path.join(new_folder_path, f'{i}.json')
	with open(path, 'w') as file:
		json.dump(response, file)
	
	time.sleep(10)
