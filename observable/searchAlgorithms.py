from problem import Problem
from time import sleep
import heapq
"""
This module contains the different classes to run the search algorithms in an observable environment. 

@author: Hugo Gilbert
"""

class Node:
    """
    A class to define a node in the search tree. 
    
    Attributes
    ----------
    state : State
        A state of the search problem
    problem : Problem
        The search problem to be solved
    fatherNode : Node
        The father node in the search tree
    actionFromFather : char
        The action that led to this new node from the father node
    pathCost : int
        The cost of the path from the root to this node in the search tree
        
    Methods
    -------
    expand()
        Method to expand the node
    getSolution()
        Method to obtain the list of actions from the root to a terminal node 
        
    """
    def __init__(self, problem, state, fatherNode, actionFromFather):
        """
        Parameters
        ----------
        problem : Problem
            The search problem to be solved
        state : State
            A state of the search problem
        fatherNode : Node
            The father node in the search tree
        actionFromFather : char
            The action that led to this new node from the father node
        """
        
        self.state = state
        self.problem = problem
        self.fatherNode = fatherNode
        self.actionFromFather = actionFromFather
        self.pathCost = 0
        if(fatherNode):
            self.pathCost = fatherNode.pathCost + problem.actionCost(fatherNode.state, actionFromFather) 
    
    def __str__(self):
        return str(self.state) 
    
    def __lt__(self,other):
        return self.state < other.state
    
    def expand(self):
        """ Method to expand the node. 
        Returns
        -------
        res : list
            The list of successor nodes obtained from expanding the current node.
        """
        res = []
        for action in self.problem.actions(self.state):
            nextState = self.problem.transition(self.state,action)
            res.append(Node(self.problem, nextState, self, action))
        return res
            
    def getSolution(self):
        """ Method to obtain the list of actions from the root to a terminal node. 
        

        Returns
        -------
        res : []
            List of actions from the root to the terminal node.
        """
        res = []
        node = self
        #tant qu'on a un pere on retrace le chemin jusqu à la racine 
        while(node.fatherNode):
            res.append(node.actionFromFather)
            node = node.fatherNode
        #on inverse car on a remonté jusqu'à la racine
        res.reverse()
        return res

class Frontier:
    """ Class to represent the frontier in the AStar algorithm.
    
    Attributes
    ----------
    frontier : list
        A list representing the frontier. It contains pairs where the first element is an AStar score and the second element is a node.    
    
    Methods
    -------
    push(score, node)
        Pushes a new node in the fontier 
    pop()
        Pops the search node with smallest AStar score
    isEmpty()
        Checks if the frontier is empty
    """

    def __init__(self):
        self.frontier = []
    
    def __str__(self):
        return " ".join((str(x) + str(y)) for (x,y) in self.frontier)

    def push(self, score, node):
        """ Pushes a new node in the fontier. 
        If the node is already present, the method checks the current Astar score of the node to decide which one to keep.

        Parameters
        ----------
        score : int
            The AStar score of the node to be stored.
        node : Node
            The search node to be stored.

        """
        found = False
        for i in range(len(self.frontier)):
            (s,n) = self.frontier[i]
            if node.state == n.state:
                found = True
                #si le noeud qu'on souhaite ajouter a un meilleur score alors on l'ajoute et on supprime l'autre
                if s > score:
                    self.frontier.pop(i)
                    heapq.heappush(self.frontier, (score, node))
                break
        if(found is False):
            heapq.heappush(self.frontier, (score, node))
        
    def pop(self):
        """ Pops the search node with smallest AStar score. 

        Returns
        -------
        (int, Node)
            A pair with the search node with smallest AStar score (in second position), and the smallest AStar score (in first position).
        """
        return heapq.heappop(self.frontier)
    
    def isEmpty(self):
        """ Checks if the frontier is empty.

        Returns
        -------
        bool
            True if the frontier is empty else False.
        """
        return True if len(self.frontier)==0 else False 
    
    def print(self):
        """

        Returns
        -------
        String 
            A string of all the nodes in the frontier, without printing the wumpus beaten attribute
        """
        frontier = "{ "
        for i in range(len(self.frontier)):
            (s,n) = self.frontier[i]
            frontier += "[" +str(s)+","+str(n.state.position)+"]"
            if i<len(self.frontier)-1:
               frontier += ", "
        frontier += "} "
        return frontier




              

class AStar:
    """ Class for the AStar Algorithm.
    This class and this documentation has to be completed. 
    """
    
    def __init__(self, problem, heuristic):
        """
        Parameters
        ----------
        problem : Problem
            The search problem to be solved.
        heuristic : function
            The heuristic function to guide the search.
        """
        self.problem = problem
        self.heuristic = heuristic
    
    def solve(self):
        """
        runs the AStar algorithm

        RETURNS 
        -------
            List of actions from the root to the terminal node found using A*.
        """
        # get the initial state
        init_state =  self.problem.getInitialState()
        n  = Node(self.problem, init_state, None, "")
        #initiate the frontier with the inial state
        frontier   = Frontier()
        #initial state's A star score = 0
        frontier.push(0, n)
        #initiate the explored set
        explored_set = set()
        # check if the Wumpus is in an adjacent square
        print("------------- step0-----------")
        print("Explored nodes : {}")
        print("Frontier :",frontier.print())
        i = 1
        while not frontier.isEmpty():     
            #pop the node with the smallest score 
            (s,n) = frontier.pop()

            print("------------- step%d-----------" % i)
            if (n.state.position==self.problem.treasure_position):
                print("Treasure foud!!!! : ",n," — ")
            else:
                print("Node : ",n," — ","AStar score : ",str(n.pathCost))
            # print explored set
            node_strings = [str(node.state.position) for node in explored_set]  
            result = "{%s}" % ", ".join(node_strings)  
            print("Explored nodes : ", result)

            if self.problem.isFinal(n.state) and n.state.wumpus_beaten:
                print("--------Game Over--------")
                print("The treasure is mine")
                return n.getSolution()
            explored_set.add(n)

            #expand the node n and calculate the score of the result nodes
            if (n.expand() == []) :
                print("    /!\\ Encountered a Snare /!\\   ")
            for n1 in n.expand():
                (x,y) = n1.state.position
                score1 = self.heuristic(n1.state) + n1.pathCost
                # Check that n1 has not been explored yet
                explored = False
                for n_explored in explored_set:
                    if n1.state==n_explored.state :
                        explored = True
                        break 
                # alan should escape the snares and the wumpus if he is still alive
                # once the wumpus died its case becomes available for alan
                # Alan can't visit the same same twice
                if explored==False and self.problem.maze[x,y]!='S' and (self.problem.maze[x,y]!='W' or n1.state.wumpus_beaten):#ajouterla condition ne pas aller sur le wumpus si il est encore vivant
                    frontier.push(score1,n1)

            # print frontier
            print("Frontier : ",str(frontier))
            i = i + 1
        return "Failure"
         


class IDAStar:
    """ Class for the IDAStar Algorithm.
    This class and this documentation has to be completed.
    """
    
    def __init__(self, problem, heuristic):
        """
        Parameters
        ----------
        problem : Problem
            The search problem to be solved.
        heuristic : function
            The heuristic function to guide the search.
        """
        self.problem = problem
        self.heuristic = heuristic
        self.frontier = Frontier()
      
        

    def solve(self):
        """
        Run the IDAStar algorithm to find a solution to the problem.

        Returns
        -------
        List of actions
            The sequence of actions from the initial state to the goal state, representing the solution.
        """

        # get the initial state
        init_state =  self.problem.getInitialState()
        node  = Node(self.problem, init_state, None, "")
        # intiate the limit to heuristic(initilState)
        limit = self.heuristic(node.state)

        i=0
        # loop until we find a solution to the problem
        while True : 
            print("------------- step%d-----------" % i)
            print("Limit : ",limit)
            print("-------------------------------")
            # we start the  limited deepnening search with limit as a depth limit
            (result,new_limit) = self.IDAStar(node, limit)
            print("-------------------------------")
            # we check if 
            if result and self.problem.isFinal(result.state) and result.state.wumpus_beaten:
                print("--------Game Over--------")
                print("The treasure is mine")
                return result.getSolution()
            else :
                if new_limit == float('inf'):
                    return "No solution found :("
                limit = new_limit
            i += 1

    
    def IDAStar(self,node,limit):
        """
        Perform the IDAStar search from a given node with a given limit.

        Parameters
        ----------
        node : Node
            The current node to expand.
        limit : float
            The depth limit for the current iteration.

        Returns
        -------
        tuple
            A tuple containing the result node and the new limit for the next iteration.
        """
        if self.problem.isFinal(node.state):
            return (node, limit)
        
        min_cost = float('inf')
        # expand the nodes and add the nodes to the frontier
        for child in node.expand():
            (x,y) = child.state.position
            # ensure that we dont add a case containing a snare to the frontier
            if self.problem.maze[x,y]!='S':
                # calculate the score of the child
                score = self.heuristic(child.state) + child.pathCost
                self.frontier.push(score,child)

        # prints
        print("Node : ",str(node))
        print("Frontier : ",self.frontier.print())
        
        while not self.frontier.isEmpty():
            (child_score,child )=  self.frontier.pop()

            if child_score > limit:
                min_cost = min(min_cost, child_score)
                continue

            print("========Explore Node  (reccursive): %s ============"%str(child))
            result, new_limit= self.IDAStar(child, limit)
            if result is not None:
                return result, new_limit

            min_cost = min(min_cost, new_limit)

        if min_cost == float('inf'):
            return None, min_cost
        return None, min_cost
        