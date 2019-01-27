import csv
import os


def parse():
    data = [[] for x in range(0,6)]
    with open('data.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        flag = False
        for row in reader:
            if (not flag):
                flag = True
                continue
            # print(row)
            for x in range(0, 6):
                data[x].append(row[x])
    return data

