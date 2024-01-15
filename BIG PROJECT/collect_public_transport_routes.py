import requests
import json

api_key = "c7fc874d-fcff-4480-8671-f452e945b35a"  # API key for UM API
url = 'https://api.um.warszawa.pl/api/action/public_transport_routes/' # URL for UM API

# Parameters for UM API
params = {
	'apikey': api_key
}

# Get data from UM API
response = requests.get(url, params=params).json()

# Save to file
with open('public_transport_routes.json', 'w') as file:
	json.dump(response, file)

