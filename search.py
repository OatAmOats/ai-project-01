# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """

    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # code here
    # create node where the state is problem.getStartState() and pathCost = 0
    # print("Start", problem.getStartState())
    # print("Is the statrt a goal?", problem.isGoalState(problem.getStartState()))
    # print("successors", problem.getSuccessors(problem.getStartState()))

    # Get root node using node initialization class
    root = Node(problem.getStartState(), None, None,0) #create root

    # Verify root node is not goal state (i.e. there are pellets to be obtained)
    if problem.isGoalState(root.state): #return if goal state
        ansList = []
        solutionFinder(root.state, ansList)
        return ansList 
    frontier = util.Stack() #create frontier and add root
    frontier.push(root)
    explored = set() # Create explored set
    keepGoing = True
    while keepGoing: # Keep doin this
        if frontier.isEmpty(): # If it's empty, return failure [I dont actually know how we're supposed to do this]
            return "failure"
        node = frontier.pop() # Take top node from the stack
        if problem.isGoalState(node.state): # Check for goal state
                        ansList = []
                        solutionFinder(node, ansList)
                        return ansList
        if node.state not in explored: # If it hasn't been explored : 
            explored.add(node.state) # Add to explored
            successors = problem.getSuccessors(node.state) 
            for i in range(0,len(successors)): # Create node for each successor and add it to the frontier
                successor = successors[i]
                succState = successor[0]
                succAction = successor[1]
                succStepCost = successor[2]
            
                child = Node(succState, succAction, node, node.pathCost + succStepCost)
                frontier.push(child)      

    util.raiseNotDefined() 


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    root = Node(problem.getStartState(), None, None,0) #create root node

    if problem.isGoalState(root.state): #check if root is goal state
        ansList = []
        solutionFinder(root, ansList)
        return ansList
    frontier = util.Queue() # Create frontier queue and add root
    frontier.push(root)
    explored = set()
    keepGoing = True
    while keepGoing:
        if frontier.isEmpty(): # If empty, return failure
            return "failure"
        node = frontier.pop() # Take oldest node from queue
        if problem.isGoalState(node.state): # Check for goal state
                        ansList = []
                        solutionFinder(node, ansList)
                        return ansList
        if node.state not in explored: # If node's state hasn't been explored
            explored.add(node.state) # Add to explored set
            successors = problem.getSuccessors(node.state)
            for i in range(0,len(successors)): 
                # Create node for each child and add to frontier
                successor = successors[i]
                succState = successor[0]
                succAction = successor[1]
                succStepCost = successor[2]
                child = Node(succState, succAction, node, node.pathCost + succStepCost)
                frontier.push(child)
                    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    root = Node(problem.getStartState(), None, None,0) # Create root node

    if problem.isGoalState(root.state): # Check for goal state
        ansList = []
        solutionFinder(root, ansList)
        return ansList
    
    frontier = util.PriorityQueue() # Create priority queue for frontier
    frontier.update(root, root.pathCost) # Now instead of just adding nodes, add nodes with their total path cost as priority
    
    explored = set()
    keepGoing = True
    while keepGoing:
        if frontier.isEmpty(): # Return failure if empty
            return "failure"
        node = frontier.pop() # Take highest priority node off frontier queue
        if problem.isGoalState(node.state): # Check for goal state
                        ansList = []
                        solutionFinder(node, ansList)
                        return ansList
        if node.state not in explored: # If node's state hasn't been explored:
            explored.add(node.state) # Add to explored
            successors = problem.getSuccessors(node.state)
            for i in range(0,len(successors)): # Create node for each child, and add to frontier
                successor = successors[i]
                succState = successor[0]
                succAction = successor[1]
                succStepCost = successor[2]
                child = Node(succState, succAction, node, node.pathCost + succStepCost)
                frontier.update(child, child.pathCost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    root = Node(problem.getStartState(), None, None,0) # Create root node
    if problem.isGoalState(root.state): # Check goal state
        ansList = []
        solutionFinder(root, ansList)
        return ansList
    frontier = util.PriorityQueue() # Create priority queue
    frontier.update(root, heuristic(root.state, problem)) # Priority is just 0

    explored = set()
    keepGoing = True
    while keepGoing:
        if frontier.isEmpty(): # If frontier is empty return failure
            return "failure"
        node = frontier.pop() # Take highest priority [lowest heuristic + pathcost] node off frontier
        if problem.isGoalState(node.state): # Check goal state
             ansList = []
             solutionFinder(node, ansList)
             return ansList
        if node.state not in explored: # If not explored
            explored.add(node.state) # Add to explored
            successors = problem.getSuccessors(node.state)
        
            for i in range(0,len(successors)): # And create node for each child, then add to frontier
                successor = successors[i]
                succState = successor[0]
                succAction = successor[1]

                # Heuristic except we also have to add the path cost and the stepCost for non-root nodes
                succPathCost = node.pathCost + successor[2]
                child = Node(succState, succAction, node, succPathCost)
                if child.state not in explored:
                    frontier.update(child, child.pathCost + heuristic(succState, problem)) # Add to frontier with update so it replaces things if priority is higher
    util.raiseNotDefined()


class Node:
    # Initialize node with relevant properties
    def __init__(self, state, action, parent, pathCost):
        self.state = state
        self.action = action
        self.parent = parent
        self.pathCost = pathCost
        self.solutionList = []

def solutionFinder(node: Node, list): # Creates stack of steps, adds them one by one to a list
    stack = util.Stack()
    solutionHelper(node, stack) # Recursively create stack through each node
    while not stack.isEmpty():
        list.append(stack.pop()) # Put eveyrthing from stack into list


def solutionHelper(node:Node, stack: util.Stack):
    if node.parent == None: # Stop when you reach the root
        return
    stack.push(node.action) # Put node on the stack
    solutionHelper(node.parent, stack) # Calls itself for recursion



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
