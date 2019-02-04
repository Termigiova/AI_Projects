from queue import Queue

from main.Graph.Utilities.Constants import Constants
from main.Graph.Data.CSV import CSV
from main.Graph.Data_Structures.Node import Node


class Graph(object):

    data = None
    graph = {}
    diary = Queue()

    def loadData(self, data):
        self.data = data

    def createGraph(self):
        self.addFirstNodeToDiary()
        if not self.diary.empty():
            self.addNodeToGraph(self.diary.get())

    def addFirstNodeToDiary(self):
        firstDataItem = self.data[Constants.FIRST_ITEM];
        node = Node(firstDataItem[Constants.ORIGIN], firstDataItem[Constants.WEIGHT])
        self.diary.put(node)

    def addNodeToGraph(self, node):
        if not self.findNodeInGraph(node):
            self.graph[node.name] = []

        connections = self.findAllConnections(node)
        if connections:
            for connection in connections:
                nodeInGraph = self.findNodeInGraph(connection)
                if not nodeInGraph:
                    self.addNodeToGraph(connection)
                    nodeInGraph = self.findNodeInGraph(connection)
                self.graph[nodeInGraph].append(node)

    def findNodeInGraph(self, node):
        if self.graph:
            for graphKey, graphNode in self.graph.items():
                if graphKey == node.name or graphKey == node.name:
                    return graphKey
        return False

    def findAllConnections(self, node):
        connections = []
        for nodeData in self.data:
            if node.name == nodeData[Constants.ORIGIN]:
                newNode = Node(nodeData[Constants.DESTINATION], nodeData[Constants.WEIGHT])
                connections.append(newNode)
            elif node.name == nodeData[Constants.DESTINATION]:
                newNode = Node(nodeData[Constants.ORIGIN], nodeData[Constants.WEIGHT])
                connections.append(newNode)
        return connections

    def getGraph(self):
        return self.graph

    def printGraph(self):
        print("--- Printing graph ---")
        for key, values in self.graph.items():
            for value in values:
                print(key, ' -> ', value.name, ' | ', value.weight)
        print("--- --- --- ---")




# graphData = CSV('./../../files/test.csv')
#
# graph = Graph()
# graph.loadData(graphData.getData())
# graph.createGraph()
# graph.printGraph()