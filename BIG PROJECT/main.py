from collect import collect_all
from analyse import analyse_all

api_key = "c7fc874d-fcff-4480-8671-f452e945b35a"  # API key for UM API

dataSet = collect_all(api_key)
analyse_all(dataSet)
