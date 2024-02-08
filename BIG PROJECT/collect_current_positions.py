import requests
import json
import time
import os
from tools import bcolors, force_response
import sys
from alive_progress import alive_it

parameters = sys.argv[1:]

# Check if there is at most one argument and call it DataSetId
if len(parameters) > 1 or (len(parameters) == 1 and not parameters[0].isdigit()):
	print(bcolors.FAIL + "Error: Too many arguments provided. Please provide at most one integer argument." + bcolors.ENDC)
	sys.exit(1)

dataSize = int(parameters[0]) if parameters else 100

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
for i in alive_it(range(dataSize), title=bcolors.OKCYAN + "Downloading data from API..." + bcolors.ENDC, spinner='dots'):
    if (i != 0):
        time.sleep(10)
    
    # Get data from UM API
    response = force_response(url, params, i)
    # Save to file
    path = os.path.join(new_folder_path, f'{i}.json')
    with open(path, 'w') as file:
        json.dump(response, file)
