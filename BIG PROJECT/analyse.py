from tools import check_params
from filter_data import filter_and_save_data
from filter_positions import filter_positions
from plot_data_set_speed import plot_data_set_speed
from plot_data_set_schedule import plot_data_set_schedule


def analyse_all(dataSet: int = 1) -> None:
    check_params(dataSet)
    filter_and_save_data(dataSet)
    plot_data_set_speed(dataSet)
    filter_positions(dataSet)
    plot_data_set_schedule(dataSet)


def analyse_speed(dataSet: int = 1) -> None:
    check_params(dataSet)
    filter_and_save_data(dataSet)
    plot_data_set_speed(dataSet)


def analyse_schedule(dataSet: int = 1) -> None:
    check_params(dataSet)
    filter_and_save_data(dataSet)
    filter_positions(dataSet)
    plot_data_set_schedule(dataSet)
