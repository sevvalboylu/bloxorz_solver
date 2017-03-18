""" Node class for storing the related information """

class node(object):
    def __init__(self, cor, p=[], c=0, g=0):
        self.cor = cor
        self.parent = p
        self.successors = []
        if len(self.cor) == 2:
            self.erected = False
        else:
            self.erected = True
        self.cost = c
        self.gcost = g

    def getCor(self):
        return self.cor

    def getCost(self):
        return self.cost

    def setCost(self, val):
        self.cost = val

    def setGcost(self,g):
        self.gcost = g

    def getGcost(self):
        return self.gcost

    def getParent(self):
        return self.parent

    def setParent(self, p):
        self.parent = p

    def __eq__(self, otherNode):
        """ Equality operator """
        if self.cor == otherNode.cor:
            return True
        else:
            return False

    def __lt__(self, otherNode):
        """ Less than operator """
        if self.cost < otherNode.cost:
            return True
        else:
            return False
