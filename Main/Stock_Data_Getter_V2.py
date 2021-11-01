# Written By Jonathan Nope #
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import os
import csv
import datetime as dt
import glob
import numpy as np

main_path = os.path.dirname(__file__)
Export_Folder = main_path + "/Stock Data/"
index_file = "INDEX.csv"
index = []
date = dt.datetime.now()
end = date.strftime('%Y') + '-' + date.strftime('%m') + '-' + date.strftime('%d')
start = str(int(date.strftime('%Y')) - 10) + '-' + date.strftime('%m') + '-' + date.strftime('%d')
yf.pdr_override()
file_extension = ".csv"
time_format = "%Y-%m-%d"

with open(index_file, 'r', newline='\n') as INDEX_CSV:
    INDEX_read = csv.reader(INDEX_CSV, delimiter=',')
    header = next(INDEX_read)
    if header is not None:
        for row in INDEX_read:
            index.append(row[0])

os.chdir(Export_Folder)
all_filenames = [i for i in glob.glob(f"*{file_extension}")]
for file in all_filenames:
    os.remove(file)

for ticker in index:
    add_avg = []
    add_dayChange = []
    df = pdr.get_data_yahoo(ticker, start, end)
    previousAVG = 0
    open_list = df['Open'].tolist()
    close_list = df['Close'].tolist()
    for i in range(len(open_list)):
        dayAVG = (open_list[i] + close_list[i]) / 2
        add_avg.append(dayAVG)
        dayAVGChange = (dayAVG - previousAVG)
        previousAVG = dayAVG
        add_dayChange.append(dayAVGChange)
    AVG = np.array(add_avg)
    dChange = np.array(add_dayChange)
    df['Average'] = AVG.tolist()
    df['AVGChange'] = dChange.tolist()
    df.to_csv(ticker + file_extension)
