from queue import Queue

import xlrd

from main.Graph.Utilities.Constants import Constants


class Excel(object):

    sheet = None

    def __init__(self, workbookName, sheetName):
        workbook = xlrd.open_workbook(workbookName)
        self.sheet = workbook.sheet_by_name(sheetName)

    def getData(self):
        row = 1
        graphData = Queue()
        while self.rowHasData(self.sheet, row):
            graphData.put([
                self.sheet.cell(row, Constants.WEIGHT).value,
                self.sheet.cell(row, Constants.ORIGIN).value,
                self.sheet.cell(row, Constants.DESTINATION).value
            ])
            row += 1
        return graphData


    def rowHasData(self, graphSheet, row):
        try:
            if graphSheet.cell(row, Constants.WEIGHT).value and graphSheet.cell(row,Constants.ORIGIN).value and graphSheet.cell(row,Constants.DESTINATION).value:
                return True
            else:
                return False
        except:
            return False