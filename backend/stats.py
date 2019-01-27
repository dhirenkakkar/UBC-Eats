import parser
from datetime import date

# Global variables
# data = []
# locations = {}

# # Populates the data and locations variables
# def loadData():
#     data = parser.parseDataCSV()
#     # locations = parser.parseLocationCSV()

# Assumes populated variables, startDate and endDate
# produces a list of elements (i.e. startDate isn't 
# at the end). Produces average spending per day in that range
def avg(startDate, endDate):
    avg = 0
    startDateSplit = startDate.split('-')
    endDateSplit = endDate.split('-')
    startDateMod= list(map(lambda x: int(x), startDateSplit))
    endDateMod= list(map(lambda x: int(x), endDateSplit))
    numDays = (date(endDateMod[2], endDateMod[1], endDateMod[0]) - date(startDateMod[2], startDateMod[1], startDateMod[0])).days
    startRow = 0
    endRow = 0
    for x in range(len(data[0])):
        if (startDate > date[0][x]):
            startRow = x - 1

data = parser.parseDataCSV()
avg("01-01-2019", "06-01-2019")