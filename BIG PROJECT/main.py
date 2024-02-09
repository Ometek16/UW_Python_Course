import sys
from tools import check_params
from filter_data import filter_and_save_data
from filter_positions import filter_positions
from plot_data_set_speed import plot_data_set_speed
from plot_data_set_schedule import plot_data_set_schedule

DataSetId = check_params(sys.argv[1:])

filter_and_save_data(DataSetId)
plot_data_set_speed(DataSetId)

filter_positions(DataSetId)
plot_data_set_schedule(DataSetId)
