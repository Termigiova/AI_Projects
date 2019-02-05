from main.Search_Algorithms.DefaultGraph import DefaultGraph


class DFS:

    result = []

    def __init__(self):
        defaultGraph = DefaultGraph()
        defaultGraph.graph.printGraph()
        self.graph = defaultGraph.getGraph()

    def DFS(self, startingVertex):
        visitedVertex = {}
        for key in self.graph.keys():
            visitedVertex[key] = False

        self.findDFS(startingVertex, visitedVertex)

    def findDFS(self, currentVertex, visitedVertex):
        visitedVertex[currentVertex] = True
        self.result.append(currentVertex)

        for vertex in self.graph[currentVertex]:
            if not visitedVertex[vertex.name]:
                self.findDFS(vertex.name, visitedVertex)

    def printResult(self):
        for item in self.result:
            print(item, end=' -> ')

graph = DFS()
graph.DFS('Acapulco')
graph.printResult()