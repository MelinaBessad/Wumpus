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
    
    def __init__(self,po_problem):
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
        return self.orSearch(self.po_problem.getInitialState(), [])

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
        self.po_problem.printBeliefStates(b_state)
        #the conditional plan
        plan = []
        #Check if any state of the belief state is a goal state 
        if self.po_problem.isFinal(b_state):
            return plan
        #Check if the belief state is on path
        if b_state in path : 
            return None
        for action in self.po_problem.actions(b_state):
            #add the current belief state to the path
            path.append(b_state)
            #update the list of new belief states 
            list_b_state = self.po_problem.update(b_state,action)
            #run every belief state
            for new_b_state in list_b_state:
                plan_i = self.andSearch(new_b_state,path)
                if plan_i is not None :
                    plan+= plan_i
            if plan is not None:
                plan = [(b_state,action)]+plan
        return plan
            
    
    def andSearch(self, b_states, path):
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
        #initiate the conditional plan
        plan = []
        plan = self.orSearch(b_states,path)
        if plan is None:
            return None
        return plan
        

        

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
