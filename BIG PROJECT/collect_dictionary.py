

import requests
import json
import os

api_key = "c7fc874d-fcff-4480-8671-f452e945b35a"  # API key for UM API
url = 'https://api.um.warszawa.pl/api/action/public_transport_dictionary/' # URL for UM API

# Parameters for UM API
params = {
	'apikey': api_key
}

# Get data from UM API
response = requests.get(url, params=params)

print(response.text)

# Save to file
with open(os.path.join('./SCHEDULE', 'dictionary.json'), 'w') as file:
	json.dump(response.json(), file)

