from main.Search_Algorithms.DefaultGraph import DefaultGraph


class DFS:

    result = []

    def __init__(self):
        defaultGraph = DefaultGraph()
        defaultGraph.graph.printGraph()
        self.graph = defaultGraph.getGraph()
        self.visitedVertex = self.initializeVisitedVertex()

    def initializeVisitedVertex(self):
        visitedVertex = {}
        for key in self.graph.keys():
            visitedVertex[key] = False
        return visitedVertex

    def DFS(self, startingVertex):
        for vertex in self.graph.keys():
            if not self.visitedVertex[vertex]:
                self.findDFS(startingVertex)

    def findDFS(self, currentVertex):
        self.visitedVertex[currentVertex] = True
        self.result.append(currentVertex)

        for vertex in self.graph[currentVertex]:
            if not self.visitedVertex[vertex.name]:
                self.findDFS(vertex.name)

    def printResult(self):
        for item in self.result:
            print(item, end=' -> ')

graph = DFS()
graph.DFS('S')
graph.printResult()