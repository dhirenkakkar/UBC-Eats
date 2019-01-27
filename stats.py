import parser
import config
from datetime import date
import numpy as np
import re

# Populates the data and locations variables
def loadData():
    if (not config.loaded):
        parser.main()
        config.loaded = True
    parser.parseDataCSV()

# Returns a tuple that has (startRow, endRow) from data
# for specified dates
def getRows(startDate, endDate):
    startDateSplit = startDate.split('-')
    endDateSplit = endDate.split('-')
    startDateMod = list(map(lambda x: int(x), startDateSplit))
    endDateMod = list(map(lambda x: int(x), endDateSplit))
    startDateForm = date(startDateMod[2], startDateMod[1], startDateMod[0])
    endDateForm = date(endDateMod[2], endDateMod[1], endDateMod[0])
    for x in range(len(config.data[0])):
        if (startDateForm < config.data[0][x]):
            startRow = x
            break
    else:
        startRow = 0
    for x in range(len(config.data[0])):
        if (endDateForm < config.data[0][x]):
            endRow = x
            break
    else:
        endRow = len(config.data[0])-1
    return (startRow, endRow)


def getNumDays(startDate, endDate):
    startDateSplit = startDate.split('-')
    endDateSplit = endDate.split('-')
    startDateMod = list(map(lambda x: int(x), startDateSplit))
    endDateMod = list(map(lambda x: int(x), endDateSplit))
    startDateForm = date(startDateMod[2], startDateMod[1], startDateMod[0])
    endDateForm = date(endDateMod[2], endDateMod[1], endDateMod[0])
    numDays = (endDateForm-startDateForm).days + 1
    return numDays

# Assumes populated variables, startDate and endDate
# produces a list of elements (i.e. startDate isn't
# at the end). Produces average spending per day in that range
def avg(startDate, endDate):
    loadData()
    rows = getRows(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    return np.mean(selectedRange)

def stDev(startDate, endDate):
    loadData()
    rows = getRows(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    return np.std(selectedRange)

def var(startDate, endDate):
    loadData()
    rows = getRows(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    return np.var(selectedRange)

# Returns the date range of all data in data.csv
def dateRange():
    loadData()
    return(config.data[0][0], config.data[0][len(config.data[0])-1])

def pieChart(startDate, endDate):
    loadData()
    rows = getRows(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    total = np.sum(selectedRange)
    ratios = {}
    regex = re.compile(r'(\D)+')
    for x in range(rows[0], rows[1]):
        nameGrouped = regex.search(config.data[1][x])
        name = nameGrouped.group()
        if (name == 'Domino\'s Pizza (' or name == 'Domino\'s Pizza (Dunbar)'):
            name = 'Domino\'s Pizza'
        elif (name == 'TrekTims'):
            name = 'TimHortons'

        if ratios.get(name, -1) == -1:
            ratios[name] = 0
        else:
            ratios[name] += config.data[4][x]

    print(ratios)
    # for key in ratios:
    #     ratios[key] = (ratios[key] / total)
    # print(ratios)

    sum = 0
    for key in ratios:
        sum += ratios[key]

    print(sum)


