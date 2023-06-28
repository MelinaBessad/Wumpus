#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the different classes to run the search algorithms in a partially observable environment. 

@author: Hugo Gilbert
"""

class AndOrSearch:
    """ Class to run the AndOrSearch algorithm.
    This class and this documentation has to be completed.
    """
    
    def __init__(self, po_problem):
        """
        Parameters
        ----------
        po_problem : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.po_problem = po_problem
    
    def solve(self):
        """
        Applies the and or search algorithm
        -------
        Returns 

        A contingency plan
        """
        plan = self.orSearch(self.po_problem.getInitialState(), [])
        if plan != "Failure":
            print("Treasure found!!!!")
            print("Game over!!!!!")
        print(plan)

    def orSearch(self, b_state, path):
        """
        Returns list of actions, conditional plan
        Parameters
        ----------
        b_State : set
            A beliefState, i.e., a set of states.
        path : list
            A list of belief states leading to the goal state

        Returns
        -------
        list
            list of actions, conditional plan
        """
        # initiate the plan
        plan = []
        print("")
        print("")
        print("-----Belief state----")
        self.po_problem.printBeliefStates(b_state)
        
        # Check if any state of the belief state is a goal state: every state on it is final and the wumpus has been defeated
        if self.po_problem.isFinal(b_state):
            return plan
        
        # Check if the belief state is on the path
        if b_state in path : 
            return "Failure"
        
        for action in self.po_problem.actions(b_state):
            # Add the current belief state to the path
            path.append(b_state)
            # Update the set of possible future states when performing action
            next_states= self.po_problem.update(b_state, action)

            print("Action :", action)
            # print path
            print("-------- Path   :")
            for b_st in path:
                self.po_problem.printBeliefStates(b_st)
            print("-------- Next Belief States  :")
            for b_s in next_states :
                self.po_problem.printBeliefStates(b_s)
            
            # call the and search function for with the new belief states
            plan = self.andSearch(next_states, path)
            
            print("--------- Resulting Belief State   :")
            self.po_problem.printBeliefStates(b_state)
            if plan != "Failure":
                plan = [action] + plan
                return plan
        
        return "Failure"
            
    def andSearch(self, states, path):
        """
        Returns list of actions, conditional plan
        Parameters
        ----------
        b_State : set
            A beliefState, i.e., a set of states.
        path : list
            A list of belief states 

        Returns
        -------
        list
            list of actions, conditional plan 
        """
        # Initiate the conditional plan
        plan = []
        for b_state in states:
            plan = self.orSearch(b_state, path)
            if plan == "Failure":
                return "Failure"
            if b_state:
                return plan
        
        return "Failure"


        

        

class AOStar:
    """ Class to run the AndOrSearch algorithm.
    This class and this documentation has to be completed.
    """
    
    def __init__(self, po_problem, heuristic):
        """
        Parameters
        ----------
        po_problem : poProblem
            The partially observable problem to be solved. 
        heuristic : function
            The heuristic function to guide the search.
        """
        
        self.po_problem = po_problem
        self.heuristic = heuristic
        
        
    def solve(self):
        """
        TODO
        """
        pass
