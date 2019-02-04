import csv
from queue import Queue

from main.graph.Constants import Constants


class CSV(object):

    data = []

    def __init__(self, filePath):
        file = open(filePath, 'r')
        csvFile = csv.reader(file)
        for row in csvFile:
            self.data.append(row)

    def getDataInQueueStructure(self):
        queue = Queue()
        for row in self.data:
            queue.put(row)
        return queue

    def getData(self):
        return self.data

    def printData(self):
        for row in self.data:
            print(row[Constants.ORIGIN], row[Constants.DESTINATION], row[Constants.WEIGHT])