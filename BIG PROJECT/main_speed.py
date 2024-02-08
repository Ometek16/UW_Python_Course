import sys
import os
from tools import bcolors
from filter_data import filter_and_save_data
from plot_data_set_speed import plot_data_set_speed

parameters = sys.argv[1:]

# Check if there is at most one argument and call it DataSetId
if len(parameters) > 1 or (len(parameters) == 1 and not parameters[0].isdigit()):
	print(bcolors.FAIL + "Error: Too many arguments provided. Please provide at most one integer argument." + bcolors.ENDC)
	sys.exit(1)

DataSetId = int(parameters[0]) if parameters else 1

# Check if the DATA_SET_{DataSetId} file exists
data_set_file = os.path.join("DATA_SETS", f"DATA_SET_{DataSetId}")
if not os.path.exists(data_set_file):
	print(bcolors.FAIL + f"Error: {data_set_file} does not exist." + bcolors.ENDC)
	sys.exit(1)

filter_and_save_data(DataSetId)
plot_data_set_speed(DataSetId)
