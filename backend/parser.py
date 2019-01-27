import csv
import os
import config
from datetime import date

# Returns a Array[Column][Row] with all the information
# from the data.csv file. Fixed 6 column, does not handle
# errors
def parseDataCSV():
    config.data = [[] for x in range(0,6)]
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            for x in range(0, 6):
                if (x == 3 or x == 2 or x == 4):
                    row[x] = float(row[x])
                elif (x == 0):
                    asList = row[x].split('-')
                    converted = list(map(lambda x: int(x), asList))
                    row[x] = date(converted[2], converted[1], converted[0])
                config.data[x].append(row[x])

# Returns a dictionary with name:(lat, long)
def parseLocationCSV():
    with open('location.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            config.locations[row[0]] = (float(row[1]), float(row[2]))



