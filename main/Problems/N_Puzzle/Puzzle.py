import random

"""
This puzzle uses the A* Algorithm
Heuristic: create children from state with shortest f-score = g-score + h-score
Where:
    g-score = Number of nodes traversed from the start node to current node
    h-score = Number of misplaced tiles
"""

class Puzzle:

    openList = []
    closedList = []
    g_score = 0
    h_score = 0

    lastItem = -1

    def __init__(self):
        self.startPuzzle = self.generateRandomPuzzle()
        self.goalPuzzle = self.generateRandomPuzzle()
        # self.printPuzzles()

    def generateRandomPuzzle(self):
        puzzle = random.sample(range(0,9), 9)
        puzzle[puzzle.index(0)] = "_"
        return puzzle

    def printPuzzles(self):
        print("Start puzzle: ", self.startPuzzle)
        print("Goal puzzle: ", self.goalPuzzle)

    def solvePuzzle(self):
        self.closedList.append(self.startPuzzle)
        self.processPuzzle()

    def processPuzzle(self):
        # start
        # take last item from closedList
        # if last item from closedList == goal, finish execution
        # look for its children (children = possible movements)
        # find the lowest cost children
        # append lowest cost children to closedList
        # go to start
        currentTile = self.closedList[self.lastItem]
        if currentTile is self.goalPuzzle:
            print("Solved the puzzle!")
            return True
        print("Last item from closed list:   ",self.closedList[self.lastItem])
        print("Goal:                         ", self.goalPuzzle)
        print("------------------------")
        combinations = self.findCombinationsWithLowestF_Score(currentTile)

    def findCombinationsWithLowestF_Score(self, tile):


puzzle = Puzzle()
puzzle.solvePuzzle()