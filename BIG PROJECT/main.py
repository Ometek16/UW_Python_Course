from collect import collect_all
from analyse import analyse_all
import os 

api_key = "c7fc874d-fcff-4480-8671-f452e945b35a"  # API key for UM API
directory = os.getcwd()

dataSet = collect_all(directory, api_key, 3)
analyse_all(directory, dataSet)
