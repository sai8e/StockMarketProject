## Written By Jonathan Nope ##

import pandas_datareader as pdr
import yfinance as yf
import os
import csv
import datetime as dt
import glob



main_path = os.path.dirname(__file__)
Export_Folder = main_path+"/Stock Data/"
index_file = "INDEX.csv"
index = []
date = dt.datetime.now()
end = date.strftime('%Y') + '-' + date.strftime('%m') + '-' + date.strftime('%d')
start = str(int(date.strftime('%Y'))-2) + '-' + date.strftime('%m') + '-' + date.strftime('%d')
yf.pdr_override()
file_extension = ".csv"



with open(index_file, 'r', newline='\n') as INDEX_CSV:
    INDEX_read = csv.reader(INDEX_CSV, delimiter=',')
    header = next(INDEX_read)
    if header != None:
        for row in INDEX_read:
            index.append(row[0])



os.chdir(Export_Folder)
all_filenames = [i for i in glob.glob(f"*{file_extension}")]
for file in all_filenames:
    os.remove(file)



for ticker in index:
    data = pdr.get_data_yahoo(ticker, start, end)
    data.to_csv(ticker+'.csv')



all_filenames = [i for i in glob.glob(f"*{file_extension}")]
for file in all_filenames:

    ex_filename = file[:file.find('.')]+"_READY.csv"
    with open(ex_filename, 'w', newline='\n') as newCSV:
        fieldnames = ['Date', 'OpenValue', 'CloseValue', 'DayAverage']
        write = csv.DictWriter(newCSV, fieldnames=fieldnames)
        write.writeheader()
        with open(file, 'r', newline='\n') as rawCSV:
            rows_read = csv.reader(rawCSV, delimiter=',')
            header = next(rows_read)
            if header != None:
                for row in rows_read:
                    sym = '$'
                    date = row[0]
                    openVal = float(row[3].replace(sym, ''))
                    closeVal = float(row[4].replace(sym, ''))
                    dayAVG = (openVal+closeVal)/2
                    write.writerow({'Date': date, 'OpenValue': openVal, 'CloseValue': closeVal, 'DayAverage': dayAVG})
                    prevClose = float(row[1].replace(sym, ''))
    os.remove(file)