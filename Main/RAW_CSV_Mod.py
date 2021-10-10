## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os
import csv
import glob

main_path = os.path.dirname(__file__)             ## get the current working directory(cwd) of the RAW_CSV_Mod.py file
raw_path = main_path+'/RAW_STOCK_DATA/'      ## add path to cwd for raw csv file path
ex_location = main_path + '/ML_STOCK_DATA/'   ## add path to cwd for export of data csv files

os.chdir(raw_path)
file_extension = ".csv"
all_filenames = [i for i in glob.glob(f"*{file_extension}")]

for file in all_filenames:
   ex_filename = file[:file.find('_')]+"_READY.csv"

   os.chdir(main_path)
   os.chdir(ex_location)
   with open(ex_filename, 'w', newline='\n') as newCSV:
       fieldnames = ['Date', 'OpenValue', 'CloseValue', 'Change%']
       write = csv.DictWriter(newCSV, fieldnames=fieldnames)
       write.writeheader()
       os.chdir(main_path)
       os.chdir(raw_path)
       with open(file, 'r', newline='\n') as rawCSV:
           rows_read = csv.reader(rawCSV, delimiter=',')
           header = next(rows_read)
           if header != None:
               for row in rows_read:
                   index = '$'
                   date = row[0]
                   openVal = float(row[3].replace(index, ''))
                   closeVal = float(row[1].replace(index, ''))
                   changeP = (openVal // closeVal)
                   os.chdir(main_path)
                   os.chdir(ex_location)
                   write.writerow({'Date': date, 'OpenValue': openVal, 'CloseValue': closeVal, 'Change%': changeP})
                   os.chdir(main_path)
                   os.chdir(raw_path)






