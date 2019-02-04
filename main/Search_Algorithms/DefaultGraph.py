from main.Graph.Data.CSV import CSV
from main.Graph.Graph import Graph


class DefaultGraph:

    def __init__(self):
        graphData = CSV('./../../files/Ciudades_Mexico.csv')
        self.graph = Graph()
        self.graph.loadData(graphData.getData())
        self.graph.createGraph()

    def getGraph(self):
        return self.graph.getGraph()