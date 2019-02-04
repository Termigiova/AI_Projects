class Node:

    name = None
    weight = None

    def __init__(self, name = None, weight = None, connections = None):
        self.name = name
        self.weight = weight
        self.connections = connections

    def __hash__(self):
        return hash((self.name, self.weight))

    def __eq__(self, other):
        return (self.name, self.weight) == (other.name, other.weight)

    def setName(self, name):
        self.name = name

    def setWeight(self, weight):
        self.weight = weight