## Writen By Jonathan Nope
## Last Edited 10/13/2021
## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import os
import csv
import glob
import shutil


main_path = os.path.dirname(__file__)                                                                                      ## get the current working directory(cwd) of the RAW_CSV_Mod.py file
raw_path = main_path+'/RAW_STOCK_DATA/'                                                                                    ## add path to cwd for raw csv file path
ex_location = main_path + '/ML_STOCK_DATA/'                                                                                ## add path to cwd for export of data csv files
flip_location = main_path + '/FL_CSVs/'

os.chdir(raw_path)                                                                                                         ## changes cwd raw_path
prevClose = float()
file_extension = ".csv"                                                                                                    ## sets desired file_extension
all_filenames = [i for i in glob.glob(f"*{file_extension}")]                                                               ## gets all files with the set file_extention

for file in all_filenames:
    fliped_filename = file[:file.find('_')] + "_Flipped.csv"
    with open(file) as rawCSV, open(fliped_filename, 'w', newline='\n') as flippedCSV:
        rows_read = csv.reader(rawCSV, delimiter=',')  ## set up the row reader
        header = next(rows_read)  ## sets first row to header
        if header != None:
            cw = csv.writer(flippedCSV, delimiter=",")

shutil.move(file, flip_location+fliped_filename)


os.chdir(flip_location)  ## changes cwd flip_location
prevClose = float()
file_extension = ".csv"  ## sets desired file_extension
all_filenames = [i for i in glob.glob(f"*{file_extension}")]  ## gets all files with the set file_extention

for file in all_filenames:                                                                                                 ## parses through desired files
   ex_filename = file[:file.find('_')]+"_READY.csv"                                                                        ## sets export filename

   os.chdir(ex_location)                                                                                                   ## change cwd to export location
   with open(ex_filename, 'w', newline='\n') as newCSV:                                                                    ## creates export csv file
       fieldnames = ['Date', 'OpenValue', 'CloseValue', 'DayChange%', 'OpenChange%']                                       ## sets header names
       write = csv.DictWriter(newCSV, fieldnames=fieldnames)                                                               ## creates formats writer
       write.writeheader()                                                                                                 ## writes header
       os.chdir(flip_location)                                                                                                  ## change cwd the raw file location
       with open(file, 'r', newline='\n') as rawCSV:                                                                       ## opens csv file
           rows_read = csv.reader(rawCSV, delimiter=',')                                                                   ## set up the row reader
           header = next(rows_read)                                                                                        ## sets first row to header
           if header != None:                                                                                              ## if row is not the header
               for row in rows_read:                                                                                       ## reads each row
                   index = '$'                                                                                             ## sets value index
                   date = row[0]                                                                                           ## sets date value
                   openVal = float(row[3].replace(index, ''))                                                              ## sets openVal value to flaot anf removes value index
                   closeVal = float(row[1].replace(index, ''))                                                             ## sets closeVal value to flaot anf removes value index
                   dayChangeP = ((closeVal-openVal)/openVal)*100                                                           ## compares openVal to closeVal and get percentage
                   if prevClose == 0.0:
                       openChangeP = 0
                   else:
                       openChangeP = ((openVal - prevClose) / prevClose) * 100
                   os.chdir(ex_location)                                                                                   ## change cwd to export location
                   ##write.writerow({'Date': date, 'OpenValue': openVal, 'CloseValue': closeVal, 'DayChange%': dayChangeP, 'OpenChange%' : openChangeP})  ## writes values to export File
                   write.writerow({'Date': date, 'OpenValue': openVal, 'CloseValue': closeVal, 'DayChange%': dayChangeP, 'OpenChange%' : openChangeP})
                   prevClose = float(row[1].replace(index, ''))

