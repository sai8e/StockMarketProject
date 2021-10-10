## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os
import os.path
import csv
import glob

current_path = os.path.dirname(__file__)             ## get the current working directory(cwd) of the RAW_CSV_Mod.py file
raw_path = current_path+'/RAW_STOCK_DATA/'      ## add path to cwd for raw csv file path
export_location = current_path + '/ML_STOCK_DATA/'   ## add path to cwd for export of data csv files

os.chdir(raw_path)
file_extension = ".csv"
all_filenames = [i for i in glob.glob(f"*{file_extension}")]

for file in all_filenames:
   with open(file, newline='\n') as rawCSV:
      rows_read = csv.reader(rawCSV, delimiter=',')
      for row in rows_read:
        print(row)
