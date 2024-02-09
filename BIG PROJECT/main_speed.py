import sys
from tools import check_params
from filter_data import filter_and_save_data
from plot_data_set_speed import plot_data_set_speed

DataSetId = check_params(sys.argv[1:])

filter_and_save_data(DataSetId)
plot_data_set_speed(DataSetId)
