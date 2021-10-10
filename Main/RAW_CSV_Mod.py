## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os
import os.path
import csv
import sys

current_path = os.path.dirname(__file__)             ## get the current working directory(cwd) of the RAW_CSV_Mod.py file
print(current_path)
raw_path = current_path+'/RAW_STOCK_DATA/'      ## add path to cwd for raw csv file path
print(raw_path)
export_location = current_path + '/ML_STOCK_DATA/'   ## add path to cwd for export of data csv files

assert os.path.isfile(raw_path)
for filename in os.listdir(raw_path):
    with open(filename, newline='') as rawCSV:
        rows_read = csv.reader(rawCSV, delimiter=',')
    for row in rows:
        print(row)