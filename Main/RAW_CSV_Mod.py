## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os
import csv

current_path = os.path.dirname(__file__)
raw_path = os.path.relpath("..\\RAW_STOCK_DATA\\AAPL_historical_data.csv", current_path)
export_location = os.path.relpath("..\\ML_STOCK_DATA\\AAPL_historical_data.csv", current_path)

with open(raw_path) as rawCSV:
    csv_read = csv.reader(rawCSV, delimiter=',')

