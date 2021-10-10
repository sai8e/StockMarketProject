## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os
import os.path
import csv

current_path = os.path.dirname(__file__)             ## get the current working directory(cwd) of the RAW_CSV_Mod.py file
raw_path = current_path + '/RAW_STOCK_DATA/'         ## add path to cwd for raw csv file path
export_location = current_path + '/ML_STOCK_DATA/'   ## add path to cwd for export of data csv files

raw_csv = raw_path+'AAPL_historical_data.csv'
print(raw_csv)

with open(raw_csv) as rawCSV:
    raw_read = csv.reader(rawCSV, delimiter=',')
print(raw_read)
