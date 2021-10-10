## This program takes the Raw Stock DATA and Modifies it, it can be added to the Machine Learning Algorium

import csv

with open("..\\RAW_STOCK_DATA\\AAPL_historical_data.csv") as rawCSV:
    csv_read = csv.reader(rawCSV, delimiter=',')
print(csv_read)
