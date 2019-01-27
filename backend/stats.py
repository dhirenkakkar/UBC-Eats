import parser
import config
from datetime import date
import numpy as np

# Populates the data and locations variables
def loadData():
    parser.parseDataCSV()
    parser.parseLocationCSV()

# Returns a tuple that has (startRow, endRow) from data
# for specified dates
def getRows(startDate, endDate):
    startDateSplit = startDate.split('-')
    endDateSplit = endDate.split('-')
    startDateMod = list(map(lambda x: int(x), startDateSplit))
    endDateMod = list(map(lambda x: int(x), endDateSplit))
    startDateForm = date(startDateMod[2], startDateMod[1], startDateMod[0])
    endDateForm = date(endDateMod[2], endDateMod[1], endDateMod[0]) 
    startRow = 0
    endRow = 0
    for x in range(len(config.data[0])):
        if (startDateForm < config.data[0][x]):
            startRow = x - 1
            break
    else:
        startRow = 0
    for x in range(len(config.data[0])):
        if (endDateForm < config.data[0][x]):
            endRow = x - 1
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
    rows = getRows(startDate, endDate)
    numDays = getNumDays(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    return np.mean(selectedRange)

def stDev(startDate, endDate):
    rows = getRows(startDate, endDate)
    numDays = getNumDays(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    return np.std(selectedRange)

def var(startDate, endDate):
    rows = getRows(startDate, endDate)
    numDays = getNumDays(startDate, endDate)
    selectedRange = config.data[4][rows[0]:rows[1]+1]
    return np.var(selectedRange)

loadData()
print(avg("02-01-2019", "08-01-2019"))
print(stDev("02-01-2019", "08-01-2019"))
print(var("02-01-2019", "08-01-2019"))

