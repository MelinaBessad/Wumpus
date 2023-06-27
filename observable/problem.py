#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains an abstract class to represent a search problem. 
This class in inherited by a simple Wumpus class to test your code.  
@author: Hugo Gilbert
"""
import numpy as np
from abc import ABC, abstractmethod


class Problem(ABC):
    """
    An astract class to represent a search problem.
    
    Methods
    -------
    actions(state)
        Yields the set of valid actions
    transition(state, action)
        The transtion function of the search problem
    isFinal(state)
        Asserts if a state is final or not
    actionCost(state, action)
        The cost function of the search problem
    getInitialState()
        Yields the initial state of the search problem
    """
    
    @abstractmethod    
    def actions(self, state):
        """ Yields the set of valid actions.
        Parameters
        ----------
        state : State
            a given state

        Returns
        -------
        set
            a set of chars representing the valid actions in the given state     
        """

        pass
    
    
    @abstractmethod
    def transition(self, state, action):
        """ The transtion function of the search problem.
        Parameters
        ----------
        state : State 
            a given state  
        action : char
            a valid action in the state

        Returns
        -------
        the state obtained when performing action in state
        """

        pass
    

    @abstractmethod
    def isFinal(self, state):
        """ Asserts if a state is final or not.

        Parameters
        ----------
        state : State
            a given state

        Returns
        -------
        True if the state is final else False

        """
        
        pass
    
    @abstractmethod
    def actionCost(self, state, action):
        """ The cost function of the search problem.
        Parameters
        ----------
        state : State 
            a given state  
        action : char
            a valid action in the state

        Returns
        -------
        the cost (a positive integer) incurred when performing action in state
        """
        
        pass
    
    @abstractmethod
    def getInitialState(self):
        """ Yields the initial state of the search problem.
        Returns
        -------
        the initial state of the search problem
        """
        
        pass
    

class Wumpus(Problem):    
    """
    A class to define a simple Wumpus problem.
    
    
    Attributes
    ----------
    ELEMENTS : dict
        Keys are strings and Values are chars. Used to describe the different elements in the maze
    ACTIONS : dict
        Keys are strings and Values are chars. Used to describe the different possible actions
    n : int
       The maze in an n * n grid
    wumpus_position: (int,int)
       The position of the wumpus in the maze
    treasure_position: (int,int)
       The position of the treasure in the maze
    maze : numpy.array
       An array of char representing the maze
       
    Methods
    -------
    actions(state)
        Yields the set of valid actions
    transition(state, action)
        The transtion function of the search problem
    isFinal(state)
        Asserts if a state is final or not
    actionCost(state, action)
        The cost function of the search problem
    getInitialState()
        Yields the initial state of the search problem
    heuristic(state)
        An heuristic function to guide the search
    """
    
    ELEMENTS = {"EMPTY" : 'E', "TREASURE" : 'T', "SNARE" : 'S', "WUMPUS": 'W'}
    ACTIONS = {"LEFT" : 'L', "RIGHT" : 'R', "UP" : 'U', "DOWN": 'D', "MAGIC": 'M'}
    
    
    def __init__(self):
        self.n = 4
        self.wumpus_position = (3,2)
        self.treasure_position = (2,3)
        self.maze = np.empty((self.n,self.n), np.dtype(str))
        self.maze[:] = Wumpus.ELEMENTS["EMPTY"]
        self.maze[1,2] = Wumpus.ELEMENTS["SNARE"]#piege
        self.maze[2,2] = Wumpus.ELEMENTS["SNARE"]
        self.maze[1,3] = Wumpus.ELEMENTS["SNARE"]
        self.maze[2,0] = Wumpus.ELEMENTS["SNARE"]
        self.maze[self.treasure_position] = Wumpus.ELEMENTS["TREASURE"]
        self.maze[self.wumpus_position] = Wumpus.ELEMENTS["WUMPUS"]
        
    class WumpusState:
        """
        Inner state class to define a state in the Wumpus problem.
        
        Attributes
        ----------
        position : (int, int)
            a position in the maze
        wumpus_beaten : bool
            True if the Wumpus is defeated else False
        """
        
        def __init__(self,pos = (0,0),wb = False):
            """
            Parameters
            ----------
            pos : (int, int), optional
                a position in the maze. The default is (0,0).
            wb : bool, optional
                True if the Wumpus is defeated else False. The default is False.
            """
            self.position = pos 
            self.wumpus_beaten = wb
            
        def __str__(self):
            return str(self.position) + " " + str(self.wumpus_beaten)
        
        def __hash__(self):
            return hash(self.position) + hash(self.wumpus_beaten)
        
        def __eq__(self, other):
            return (self.position == other.position) and self.wumpus_beaten == other.wumpus_beaten
        
        def __lt__(self,other):
            return (self.position,self.wumpus_beaten) < (other.position, other.wumpus_beaten)

         
    def actions(self, state):
        """ Yields the set of valid actions. The agent may move if it is not trapped by a snare or the Wumpus and may use magic if the Wumpus is close. 
        Parameters
        ----------
        state : State
            a given state

        Returns
        -------
        set
            a set of chars representing the valid actions in the given state     
        """
        
        posx, posy = state.position
        res = set()
        if (self.maze[posx,posy] == Wumpus.ELEMENTS["SNARE"])\
            or ((self.maze[posx,posy] == Wumpus.ELEMENTS["WUMPUS"]) and (state.wumpus_beaten == False)):
            return res
        if(posx!=0):
            res.add(Wumpus.ACTIONS["LEFT"])
        if(posx!=self.n-1):
            res.add(Wumpus.ACTIONS["RIGHT"])
        if(posy!=0):
            res.add(Wumpus.ACTIONS["DOWN"])
        if(posy!=self.n-1):
            res.add(Wumpus.ACTIONS["UP"])
        if(((abs(posx-self.wumpus_position[0])+abs(posy-self.wumpus_position[1])) == 1) and (state.wumpus_beaten == False)):
            res.add(Wumpus.ACTIONS["MAGIC"])                           
        return res
    
    def transition(self, state, action):
        """ The transtion function of the Wumpus search problem.
        Parameters
        ----------
        state : State 
            a given state  
        action : char
            a valid action in the state

        Returns
        -------
        the state obtained when performing action in state
        """
        
        posx, posy = state.position
        wb = state.wumpus_beaten
        if action == Wumpus.ACTIONS["LEFT"]:
            return self.WumpusState((posx-1,posy),wb)
        elif action == Wumpus.ACTIONS["RIGHT"]:
            return self.WumpusState((posx+1,posy),wb)
        elif action == Wumpus.ACTIONS["DOWN"]:
            return self.WumpusState((posx,posy-1),wb)
        elif action == Wumpus.ACTIONS["UP"]:
            return self.WumpusState((posx,posy+1),wb)
        elif action == Wumpus.ACTIONS["MAGIC"]:
            return self.WumpusState((posx,posy),True)
        raise Exception("Invalid action")
        
    def isFinal(self, state):
        """ Asserts if a state is final or not. A state is final if the position matches the one of the Treasure and if the Wumpus is defeated.

        Parameters
        ----------
        state : State
            a given state

        Returns
        -------
        True if the state is final else False

        """
        
        return state.position == self.treasure_position and state.wumpus_beaten
        
    def actionCost(self, state, action):
        """ The cost function of the Wumpus search problem.
        Parameters
        ----------
        state : State 
            a given state  
        action : char
            a valid action in the state

        Returns
        -------
        the cost (a positive integer) incurred when performing action in state, 1 for a move action and 5 to use magic
        """
        
        return 5 if action == Wumpus.ACTIONS["MAGIC"] else 1
        
    def getInitialState(self):
        """ Yields the initial state of the Wumpus search problem.
        Returns
        -------
        the initial state of the search problem, by default in (0,0) and the Wumpus alive
        """
        
        return self.WumpusState()
    
    def heuristic(self, state):
        """ An heuristic function to guide the search.
        Returns 
        -------
        the distance of manhattan between the state "state" and the treasure
        """

        posx, posy    = state.position
        posx_t,posy_t = self.treasure_position 
        return abs((posx_t-posx))+ abs((posy_t-posy))
    

        
