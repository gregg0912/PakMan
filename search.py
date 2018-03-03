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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    """
    DFS will make use of the Stack data structure since the point of DFS is to traverse through the graph as deep as it can and backtrack afterwards

    A tuple will be pushed into the stack comprised of the node and the list of actions that Pacman will take

    An empty list of visited nodes is also initialized
    """
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = []

    """
    The while loop is used to visit all of the nodes.
    This loop will end once the stack is empty or the goal state is reached.
    """
    while not stack.isEmpty():
        node, directions = stack.pop()
        """
        Check if the popped node (current node) is the goal state. If yes, return the list of directions.
        """
        if problem.isGoalState(node):
            return directions
        """
        Since the node is popped from the stack, include it in the list of visited nodes.
        """
        visited.append(node)
        for successor in problem.getSuccessors(node):
            """
            Get all of the 'successors' or 'children' of the current node
            It will only be added into the stack if it has not been visited yet
            """
            if successor[0] not in visited:
                newdirections = directions + [successor[1]]
                stack.push((successor[0], newdirections))
    """
    If the stack is already empty and the goal state still wasn't reached, the funtion will instead return Directions.STOP
    """
    return [Directions.STOP]
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    """
    BFS will make use of the Queue data structure since the point of BFS is to traverse through the graph by level

    A tuple will be pushed into the queue comprised of the node and the list of actions that Pacman will take

    A list of visited nodes is initialized. The starting node is added to ensure that it will only be visited once.
    """
    queue = util.Queue()
    queue.push((problem.getStartState(), []))
    visited = [problem.getStartState()]

    """
    The while loop is used to visit all of the nodes.
    This loop will end once the queue is empty or the goal state is reached.
    """
    while not queue.isEmpty():
        node, directions = queue.pop()
        """
        Check if the popped node (current node) is the goal state. If yes, return the list of directions.
        """
        if problem.isGoalState(node):
            return directions
        """
        Get all of the 'successors' or 'children' of the current node
        It will only be added into the queue if it has not been visited yet.
        After adding it to the queue, include it in the list of visited nodes
        """
        for successor in problem.getSuccessors(node):
            if successor[0] not in visited:
                newdirections = directions + [successor[1]]
                queue.push((successor[0], newdirections))
                visited.append(successor[0])
    """
    If the queue is already empty and the goal state still wasn't reached, the funtion will instead return Directions.STOP
    """
    return [Directions.STOP]
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions

    """
    UCS will make use of the PriorityQueue data structure since it can use the actions' cost as a priority in the heap

    A tuple will be pushed into the priorityqueue comprised of the node and the list of actions that Pacman will take. An additional parameter is included which is the cost of the actions taken by Pacman

    An empty list of visited nodes is initialized.
    """
    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    visited = []
    """
    The while loop is used to visit all of the nodes.
    This loop will end once the priorityqueue is empty or the goal state is reached.
    """
    while not frontier.isEmpty():
        node, directions = frontier.pop()
        """
        Check if the popped node (current node) is the goal state. If yes, return the list of directions.
        """
        if problem.isGoalState(node):
            return directions

        """
        If the current node is not yet visited, include it in the list and explore its successors
        """
        if node not in visited:
            visited.append(node)
            """
            Get all of the 'successors' or 'children' of the current node
            It will only be added into the priorityqueue if it has not been visited yet.
            """
            for successor in problem.getSuccessors(node):
                if successor[0] not in visited:
                    newdirections = directions + [successor[1]]
                    frontier.push((successor[0],newdirections), problem.getCostOfActions(newdirections))
    """
    If the priority queue is already empty and the goal state still wasn't reached, the funtion will instead return Directions.STOP
    """
    return [Directions.STOP]

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

    from game import Directions

    """
    A* Search will make use of the PriorityQueue data structure since it can use the actions' cost + heuristics as a priority in the heap

    A tuple will be pushed into the priorityqueue comprised of the node and the list of actions that Pacman will take. An additional parameter is included which is the cost of the actions + heuristics taken by Pacman

    The heuristics function used is manhattanDistance which is found in searchAgents.py

    An empty list of visited nodes is initialized.
    """

    frontier = util.PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    visited = []
    """
    The while loop is used to visit all of the nodes.
    This loop will end once the priorityqueue is empty or the goal state is reached.
    """
    while not frontier.isEmpty():
        """
        Check if the popped node (current node) is the goal state. If yes, return the list of directions.
        """
        node, directions = frontier.pop()
        if problem.isGoalState(node):
            return directions
        """
        If the current node is not yet visited, include it in the list and explore its successors
        """
        if node not in visited:
            visited.append(node)
            """
            Get all of the 'successors' or 'children' of the current node
            It will only be added into the priorityqueue if it has not been visited yet.
            """
            for successor in problem.getSuccessors(node):
                if successor[0] not in visited:
                    newdirections = directions + [successor[1]]
                    cost = problem.getCostOfActions(newdirections) + heuristic(successor[0],problem)
                    frontier.push((successor[0],newdirections), cost)
    """
    If the priority queue is already empty and the goal state still wasn't reached, the funtion will instead return Directions.STOP
    """
    return [Directions.STOP]
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
