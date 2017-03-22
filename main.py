from boardClass import board
from node import node
from math import sqrt
import heapq
import time

def heuristicFunc(goal, curr):
    x = goal[0][0]
    y = goal[0][1]

    xcurr = curr[0][0]
    ycurr = curr[0][1]

    dx = abs(x - xcurr)
    dy = abs(y - ycurr)
    return 0.66 * (dx + dy) # scaled manhattan distance

    #return sqrt((x - xcurr) ** 2 + (y - ycurr) ** 2) # euclidian distance

def aStar(bd, goal):
    """ A* Search implementation
    brd: game board, board class object
    """
    frontier = [node(bd.getInitials(), [], 0, 0)]
    closed = {}

    while frontier:
        curr = heapq.heappop(frontier)
        path = curr.getParent() + [curr.getCor()]
        if curr == goal:
            print "Number of nodes in closed (A*): ", len(closed)
            return path

        curCor = str(curr.getCor())

        #closed[curCor] = curr.getCost()

        expand = bd.getNeighbours(curr.getCor())
        successors = []
        for x in expand:
            successors.append(node(x, path, heuristicFunc(goalState.getCor(), x) + 1 + curr.getGcost(), 1 + curr.getGcost()))

        for successor in successors:
            cost = successor.getCost()
            try:  # to prevent calling index method multiple times
                index = frontier.index(successor)
            except Exception:
                pass

            if str(successor.getCor()) not in closed and successor not in frontier:
                heapq.heappush(frontier, successor)
            elif successor in frontier and frontier[index].getCost() < cost:
                frontier[index].setCost(cost)
                frontier[index].setParent(successor.getParent())
            for x in closed:
                if x == successor.getCor() and closed[x] > cost:
                    newNode = node(x, path, closed[x])
                    heapq.heappush(frontier, newNode)

        closed[curCor] = curr.getCost()

    return None

def ucs(bd, goal):
    """ UCS Search implementation
    bd: game board, board class object
    """
    frontier = [node(bd.getInitials(), [], 0)]
    closed = {}

    while frontier:
        curr = heapq.heappop(frontier)
        path = curr.getParent() + [curr.getCor()]
        if curr == goal:
            print "Number of nodes in closed (UCS): ", len(closed)
            return path

        curCor = str(curr.getCor())

        closed[curCor] = curr.getCost()

        expand = bd.getNeighbours(curr.getCor())
        successors = []
        for x in expand:
            successors.append(node(x, path, 1 + curr.getCost()))

        for successor in successors:
            cost = successor.getCost()
            try: # to prevent calling index method multiple times
                index = frontier.index(successor)
            except Exception:
                pass

            if str(successor.getCor()) not in closed and successor not in frontier:
                heapq.heappush(frontier, successor)
            elif successor in frontier and frontier[index].getCost() > cost:
                frontier[index].setCost(cost)
                frontier[index].setParent(successor.getParent())

    return None

input = "input_matrix.txt"

brd = board(input)

brd.setBoard()

goalState = node([brd.getGoal()])

start_time = time.time()
pathaStar = aStar(brd, goalState)
finish_time = time.time()

if pathaStar != None: # in case there is no path
    for x in pathaStar:
        print x
else:
    print "No path to goal state!: A*"
print "Run Time of A*: ", finish_time - start_time


start_time = time.time()
pathUCS = ucs(brd, goalState)
finish_time = time.time()

if pathUCS != None: # in case there is no path
    for x in pathUCS:
        print x
else:
    print "No path to goal state!: UCS"
print "Run Time of UCS: ", finish_time - start_time
