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
    
    def pop_threshold(self, threshold):
        """
        Pops the search node with  AStar score equal to threshold. 

        Returns
        -------
       
        """
        return list(filter(lambda pair : pair[0] == threshold, self.frontier))
        
    def isEmpty(self):
        """ Checks if the frontier is empty.

        Returns
        -------
        bool
            True if the frontier is empty else False.
        """
        return True if len(self.frontier)==0 else False   

              

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
        init_state =  self.problem.getInitialState()
        init_node  = Node(self.problem, init_state, None, "")
        #initiate the frontier with the inial state
        frontier   = Frontier()
        frontier.push(0, init_node)
        #initiate the explored set
        explored_set = set()
        while(True):
            if frontier.isEmpty():
                raise Exception("Failure")
            #pop the node with the smallest score
            (s,n) = frontier.pop()
            if self.problem.isFinal(n.state):
                return n.getSolution()
            explored_set.add(n)
            #expand the node n and calculate the score of the result nodes
            for n1 in n.expand():
                score1 = self.heuristic(n1.state) + n1.pathCost
                frontier.push(score1,n1)


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
        self.explored_nodes = set()
        self.cost_explored_node = []
        

    def solve(self):
        init_state =  self.problem.getInitialState()
        init_node  = Node(self.problem, init_state, None, "")
        #initiate the frontier with the inial state
        self.frontier   = Frontier()
        #initiate the explored set
        self.explored_set = set()
        threshold = self.heuristic(init_state)
        #the cost of the initial state equals the manhattan distance between it and the treasure
        self.frontier.push(threshold, init_node)
        while True :
            result, threshold = self.depth_limited_search(init_node, threshold) 
            for (s,n) in (self.explored_nodes|set(self.frontier.frontier)):
                print("n : ",n)
                if self.problem.isFinal(n.state):
                    return n.getSolution()
    def depth_limited_search(self, node, threshold):
    
        if self.problem.isFinal(node.state):
            return node
        #we add the node the explored nodes set
        self.explored_set.add(node)
        (min_cost,smallest_node) = self.frontier.pop()
        for child in node.expand():
            child_cost = child.pathCost + self.heuristic(child.state)
            if child not in (self.explored_nodes|set(self.frontier.frontier)):
                self.frontier.push(child_cost,child)
            #we expand the child
            if child_cost <= threshold:
                result, new_threshold = self.depth_limited_search(child,threshold)
                if result is not None :
                    return result, new_threshold
                min_cost = min(min_cost, new_threshold)
        return None, threshold


      
    def solve_v1(self):
        """
        runs the IDAStar algorithm
        RETURNS 
        -------
            List of actions from the root to the terminal node found using IDA*.
        """
        root_state = self.problem.getInitialState()
        root_node  = Node(self.problem, root_state, None, "")
        threshold = self.heuristic(root_state)
        while True :
            result, threshold = self.depth_limited_search(root_node, threshold)
            for n in self.explored_nodes : 
                if self.problem.isFinal(n.state):
                    return n.getSolution()
                
    def depth_limited_search_V1(self, node, threshold):
        """
        runs the depth limited search
        RETURNS
        -------
            (result, threshold)
                result : is a union between the explored set and the nodes contained in the frontier
                threshold : is the minimum fscore of the nodes in the frontier
        """
        print("----------------------------")
        print("node----- : ",node)
        print("threshold------",threshold)
        if self.problem.isFinal(node.state):
            return ({node}, threshold)
        
        node_cost= node.pathCost + self.heuristic(node.state)
        self.cost_explored_node.append(node_cost)
        self.explored_nodes.add(node)
        min_cost = min(self.cost_explored_node)
        print("min_cost : ",min_cost)
        for child in node.expand():
            print("child : ",child)
            #calculate the child cost
            child_cost = child.pathCost + self.heuristic(child.state)
            print("child cost : ",child_cost)
            #we expand the child
            if child_cost <= threshold:
                result, new_threshold = self.depth_limited_search(child,threshold)
                if result is not None :
                    return self.explored_nodes|{result}, new_threshold
                min_cost = min(min_cost, new_threshold)
        return None, min_cost

