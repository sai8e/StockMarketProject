## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os.path
import csv

current_path = os.path.dirname(__file__)
raw_path = current_path + '/RAW_STOCK_DATA/'
export_location = current_path + '/ML_STOCK_DATA/'
raw_csv = raw_path+'AAPL_historical_data.csv'

with open(raw_csv) as rawCSV:
    raw_read = csv.reader(rawCSV, delimiter=',')
print(raw_read)
