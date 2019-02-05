from main.Search_Algorithms.DefaultGraph import DefaultGraph


class Hill:

    result = []
    goal = None

    def __init__(self):
        defaultGraph = DefaultGraph()
        defaultGraph.graph.printGraph()
        self.graph = defaultGraph.getGraph()

    def Hill(self, startingVertex, goalVertex):
        self.goal = goalVertex
        self.findHill(startingVertex)

    def findHill(self, currentVertex):
        self.result.append(currentVertex)
        if not self.checkGoal(currentVertex):
            connections = self.graph.findAllConnections(currentVertex)
            if connections:
                nextVertex = self.heuristicSort(connections)
                self.findHill(nextVertex)

    def heuristicSort(self, connections):
        currentWeight = 0
        for connection in connections:
            if (connection.weight>= currentWeight):
                bestHeuristic = connection
        return bestHeuristic

    def checkGoal(self, currentVertex):
        if (currentVertex.name == self.goalVertex.name):
            self.result.append(currentVertex)
            return True
        return False

    def printResult(self):
        for item in self.result:
            print(item, end=' -> ')

graph = Hill()
graph.Hill('Acapulco', 'Cuernavaca')
graph.printResult()