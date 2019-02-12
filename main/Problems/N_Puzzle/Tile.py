class Tile:

    topLeftCorner       = 0
    topMiddle           = 1
    topRightCorner      = 2
    midLeft             = 3
    center              = 4
    midRight            = 5
    bottomLeftCorner    = 6
    bottomMiddle        = 7
    bottomRightCorner   = 8

    def possibleMovementsBasedOnIndex(self, tileIndex):
        switch = {
            self.topLeftCorner      : self.topLeftCorner(),
            self.topMiddle          : self.topMiddle(),
            self.topRightCorner     : self.topRightCorner(),
            self.midLeft            : self.midLeft(),
            self.center             : self.center(),
            self.midRight           : self.midRight(),
            self.bottomLeftCorner   : self.bottomLeftCorner(),
            self.bottomMiddle       : self.bottomMiddle(),
            self.bottomRightCorner  : self.bottomRightCorner()
        }

        print(switch.get(tileIndex, lambda: "Invalid tile index"))

    def topLeftCorner(self):
        return [
            self.topMiddle,
            self.midLeft
        ]

    def topMiddle(self):
        return [
            self.topLeftCorner,
            self.topRightCorner,
            self.center
        ]

    def topRightCorner(self):
        return [
            self.topMiddle,
            self.midLeft
        ]

    def midLeft(self):
        return [
            self.topLeftCorner,
            self.center,
            self.bottomLeftCorner
        ]

    def center(self):
        return [
            self.topMiddle,
            self.midLeft,
            self.midRight,
            self.bottomMiddle
        ]

    def midRight(self):
        return [
            self.topRightCorner,
            self.center,
            self.bottomRightCorner
        ]

    def bottomLeftCorner(self):
        return [
            self.midLeft,
            self.bottomMiddle
        ]

    def bottomMiddle(self):
        return [
            self.center,
            self.bottomLeftCorner,
            self.bottomRightCorner
        ]

    def bottomRightCorner(self):
        return [
            self.midRight,
            self.bottomMiddle
        ]