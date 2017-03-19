""" Creating the board environment and deciding on the eligible moves on the board """

class board(object):

    def __init__(self, f):
        """ f: file name """
        self.file = f
        self.goal = []
        self.matrix = []
        self.xSize = 0
        self.ySize = 0
        self.emptyTiles = []
        self.initial = []

    def getXSize(self):
        return self.xSize

    def getYSize(self):
        return self.ySize

    def getInitials(self):
        return self.initial

    def getGoal(self):
        return self.goal

    def setBoard(self):
        """ reads the input file
        and constructs the matrix
        """
        fileName = self.file
        goalXcor = 0

        with open(fileName, 'r') as fObj:
            lines = fObj.readlines()
            self.xSize = len(lines)
            for line in lines:
                row = line.replace("\n", "").split(" ")
                self.ySize = len(row)
                colCount = 0
                for x in row:
                    if x == 'G': # Goal Tile
                        goalYcor = row.index('G')
                        self.goal = list([goalXcor, goalYcor])

                    if x == 'X': # Empty Tiles
                        self.emptyTiles.append(list([goalXcor,colCount]))

                    if x == 'S': # Initial Position of the block
                        self.initial.append(list([goalXcor, colCount]))

                    colCount += 1

                self.matrix.append(row)
                goalXcor += 1


    def checkCor(self, xCor, yCor):
        """ Checks if the selected
        coordinate is a valid coordinate or not
        """
        if (list([xCor, yCor]) not in self.emptyTiles) and (not xCor >= self.xSize and not yCor >= self.ySize) and (not xCor < 0 and not yCor < 0):
            return True
        else:
            return False

    def getNeighbours(self, coor):
        """ returns the eligible
        neighbours of node at coor"""
        erected = True if len(coor) == 1 else False
        neighbours = []
        if erected:
            xCor = coor[0][0]
            yCor = coor[0][1]
            if self.checkCor(xCor-1, yCor) and self.checkCor(xCor-2,yCor):
                north = list([list([xCor-2,yCor]),list([xCor-1,yCor])])
                neighbours.append(north)
            if self.checkCor(xCor+1,yCor) and self.checkCor(xCor+2,yCor):
                south = list([list([xCor+1,yCor]),list([xCor+2,yCor])])
                neighbours.append(south)
            if self.checkCor(xCor,yCor-2) and self.checkCor(xCor,yCor-1):
                west = list([list([xCor,yCor-2]),list([xCor,yCor-1])])
                neighbours.append(west)
            if self.checkCor(xCor,yCor+1) and self.checkCor(xCor,yCor+2):
                east = list([list([xCor,yCor+1]),list([xCor,yCor+2])])
                neighbours.append(east)

            return neighbours

        else:
            xCor1 = coor[0][0]
            xCor2 = coor[1][0]
            yCor1 = coor[0][1]
            yCor2 = coor[1][1]

            if xCor1 == xCor2: #horizontal position
                if self.checkCor(xCor1 - 1, yCor1) and self.checkCor(xCor2 - 1, yCor2):
                    north = list([list([xCor1 - 1, yCor1]), list([xCor2 - 1, yCor2])])
                    neighbours.append(north)
                if self.checkCor(xCor1 + 1, yCor1) and self.checkCor(xCor2 + 1, yCor2):
                    south = list([list([xCor1 + 1, yCor1]), list([xCor2 + 1, yCor2])])
                    neighbours.append(south)
                if self.checkCor(xCor1, yCor1 - 1):
                    west = [list([xCor1, yCor1 - 1])]
                    neighbours.append(west)
                if self.checkCor(xCor2, yCor2 + 1):
                    east = [list([xCor2, yCor2 + 1])]
                    neighbours.append(east)
                return neighbours
            else: # vertical position
                if self.checkCor(xCor1 - 1, yCor1):
                    north = [list([xCor1 - 1, yCor1])]
                    neighbours.append(north)
                if self.checkCor(xCor2 + 1, yCor2):
                    south = [list([xCor2 + 1, yCor2])]
                    neighbours.append(south)
                if self.checkCor(xCor1, yCor1 - 1) and self.checkCor(xCor2, yCor2 - 1):
                    west = list([list([xCor1, yCor1 - 1]), list([xCor2, yCor2 - 1])])
                    neighbours.append(west)
                if self.checkCor(xCor1, yCor1 + 1) and self.checkCor(xCor2, yCor2 + 1):
                    east = list([list([xCor1, yCor1 + 1]), list([xCor2, yCor2 + 1])])
                    neighbours.append(east)
                return  neighbours