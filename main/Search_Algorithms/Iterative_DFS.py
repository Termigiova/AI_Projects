from queue import Queue

from main.Search_Algorithms.DefaultGraph import DefaultGraph


class Iterative_DFS:

    result = []
    stack = Queue()

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
                self.stack.put(startingVertex)
                self.findDFS()

    def findDFS(self):
        if not self.stack.empty():
            currentVertex = self.stack.get()
            if not self.visitedVertex[currentVertex]:
                self.visitedVertex[currentVertex] = True
                self.result.append(currentVertex)

            for vertex in self.graph[currentVertex]:
                if not self.visitedVertex[vertex.name]:
                    self.stack.put(vertex.name)

            self.findDFS()

    def printResult(self):
        for item in self.result:
            print(item, end=' -> ')

graph = Iterative_DFS()
graph.DFS('S')
graph.printResult()