    # search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):

    parentList = []
    pathList = []
    openList = []
    closedList = []

    openList.append(problem.getStartState())
    

    while openList:
        n = openList.pop()

        if problem.isGoalState(n):
            #Find goal node in parentList
            backtrackPoint = None
            for node in parentList:
                if(node[0][0] == n):
                    backtrackPoint = node #This is n, the goal

            pathList.append(backtrackPoint[0][1])

            #While the parent of my poing is not where I started,
            while not (backtrackPoint[1] == problem.getStartState()):
                #print(backtrackPoint)
                #Look for parent of my point in the parentList
                for parent in parentList:
                    #If parent of my current point is found (given every child should only have one parent)
                    if (backtrackPoint[1] == parent[0][0]):
                        pathList.append(parent[0][1]) #Append the action from parent to child
                        backtrackPoint = parent #continue backtracking from the parent towards the start

            pathList.reverse()

            #print(pathList)
            return pathList;

        if not (n in closedList):
            closedList.append(n)
            next = problem.getSuccessors(n)
            for suc in next:
                if not (suc[0] in closedList):
                    openList.append(suc[0])
                    parentList.append((suc, n))

    #util.raiseNotDefined()


def breadthFirstSearch(problem):
    
    parentList = []
    pathList = []
    openList = []
    closedList = []

    openList.append(problem.getStartState())
    print(openList)

    while openList:
        n = openList.pop(0)
        #print(n, problem.isGoalState(n))

        if problem.isGoalState(n):
            
            #Find goal node in parentList
            backtrackPoint = None
            for node in parentList:
                if(node[0][0] == n):
                    backtrackPoint = node #This is n, the goal

            print("I found the goal:", n, backtrackPoint)

            pathList.append(backtrackPoint[0][1])

            #While the parent of my poing is not where I started,
            while not (backtrackPoint[1] == problem.getStartState()):
                
                #Look for parent of my point in the parentList
                for parent in parentList:
                    #If parent of my current point is found (given every child should only have one parent)
                    if (backtrackPoint[1] == parent[0][0]):
                        pathList.append(parent[0][1]) #Append the action from parent to child
                        backtrackPoint = parent #continue backtracking from the parent towards the start

                #print(backtrackPoint)

            pathList.reverse()
            #print(pathList)
            return pathList;

        if not (n in closedList):
            closedList.append(n)
            next = problem.getSuccessors(n)
            for suc in next:
                if not (suc[0] in closedList):
                    openList.append(suc[0])
                    parentList.append((suc, n))
            

def uniformCostSearch(problem):
    
    parentList = []
    pathList = []
    openList = []
    closedList = []

    openList.append((problem.getStartState(), 0))
    #print(openList)

    while openList:
        n = openList.pop(0)

        if problem.isGoalState(n[0]):
            
            #Find goal node in parentList
            backtrackPoint = None
            for node in parentList:
                if(node[0][0] == n[0]):
                    backtrackPoint = node #This is n, the goal

            #print(parentList[0])
            #print("I found the goal:", n, backtrackPoint)

            pathList.append(backtrackPoint[0][1])

            #While the parent of my poing is not where I started,
            while not (backtrackPoint[1] == problem.getStartState()):
                
                #Look for parent of my point in the parentList
                for parent in parentList:
                    #If parent of my current point is found (given every child should only have one parent)
                    if (backtrackPoint[1] == parent[0][0]):
                        pathList.append(parent[0][1]) #Append the action from parent to child
                        backtrackPoint = parent #continue backtracking from the parent towards the start

                #print(backtrackPoint)

            pathList.reverse()
            #print(pathList)
            return pathList;

        if not (n[0] in closedList):
            closedList.append(n[0])
            next = problem.getSuccessors(n[0])
            for suc in next:
                if not (suc[0] in closedList):
                    openList.append((suc[0], n[1] + suc[2]))
                    parentList.append((suc, n[0]))

            openList.sort(key = lambda x: x[1])

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    
    parentList = []
    pathList = []
    openList = []
    closedList = []

    openList.append((problem.getStartState(), 0))
    #print(openList)

    while openList:
        n = openList.pop(0)

        if problem.isGoalState(n[0]):
            
            #Find goal node in parentList
            backtrackPoint = None
            for node in parentList:
                if(node[0][0] == n[0]):
                    backtrackPoint = node #This is n, the goal

            #print(parentList[0])
            #print("I found the goal:", n, backtrackPoint)

            pathList.append(backtrackPoint[0][1])

            #While the parent of my poing is not where I started,
            while not (backtrackPoint[1] == problem.getStartState()):
                
                #Look for parent of my point in the parentList
                for parent in parentList:
                    #If parent of my current point is found (given every child should only have one parent)
                    if (backtrackPoint[1] == parent[0][0]):
                        pathList.append(parent[0][1]) #Append the action from parent to child
                        backtrackPoint = parent #continue backtracking from the parent towards the start

                #print(backtrackPoint)

            pathList.reverse()
            #print(pathList)
            return pathList;

        if not (n[0] in closedList):
            closedList.append(n[0])
            next = problem.getSuccessors(n[0])
            for suc in next:
                if not (suc[0] in closedList):
                    openList.append((suc[0], n[1] + heuristic(suc[0], problem) + suc[2]))
                    parentList.append((suc, n[0]))

            openList.sort(key = lambda x: x[1])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
