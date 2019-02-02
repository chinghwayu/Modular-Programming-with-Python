""" chart.py

    This module implements the chart-related functions for the Charter package.
"""

class Chart:
    def __init__(self):
        self.chart = {}

    def set_title(self, title):
        self.chart["title"] = title

    def set_x_axis(self, x_axis):
        self.chart['x_axis'] = x_axis

    def set_y_axis(self, minimum, maximum, labels):
        self.chart['y_min']    = minimum
        self.chart['y_max']    = maximum
        self.chart['y_labels'] = labels

    def set_series_type(self, series_type):
        self.chart['series_type'] = series_type

    def set_series(self, series):
        self.chart['series'] = series
