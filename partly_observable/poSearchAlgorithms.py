#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the different classes to run the search algorithms in a partially observable environment. 

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
        #Check if any state of the belief state is a goal state 
        if self.po_problem.isFinal(b_state):
            return []
        
        #Check if the belief state is on path
        if b_state in path : 
            return "Failure"
        
        for action in self.po_problem.actions(b_state):
            #update the list of new belief states 
            next_possible_states = self.po_problem.update(b_state,action)
            #add the current belief state to the path
            new_path = path + [b_state]
            plan = self.andSearch(next_possible_states, new_path)
            if plan != "Failure":
                return [action]+plan
            
        return "Failure"
    
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
        for states in b_states : 
            plan_i = self.orSearch(states, path)
            if plan_i=="Failure":
                return "Failure"
            plan.append(plan_i)
        return plan
        
                 
class AOStar:
    """ Class to run the AndOrSearch algorithm.
    """
    
    def __init__(self, po_problem, heuristic):
        """
        Parameters
        ----------
        po_problem : poProblem
            The partially observable problem to be solved. 
        heuristic : function
            The heuristic function to guide the search.
        open : 
            The set  of nodes that have been explored and for which it is not known whether they lead to a solution or not
        close:
            The set of nodes that have been treated
        """
        
        self.po_problem = po_problem
        self.heuristic = heuristic
        self.open = set()
        self.close = set()
    
    def solve(self):
        """
        Applies the AO* algorithm
        -------
        Returns 

        A contingency plan
        """
        # get the initial belief state
        belief_state = self.problem.getInitialState()
        # step 1 :  put the initial node in the set open 
        self.open.add(belief_state)
        
        while self.open:
            # Step 2: Select the most promising subplan T
            for action in self.po_problem.actions(belief_state):
                possible_future_states = self.po_problem.update(belief_state, action)

            
            # Step 3: Select a node n from Open and T
            node = self.selectNodeFromOpenAndSubplan(t)
            
            # Step 4: Check if node n is a final state
            if self.problem.isFinal(node):
                self.markNodeAsResolved(node)
                return self.constructPlan(node)
            
            # Step 5: Check if node n is unsolvable
            if self.isNodeUnsolvable(node):
                self.markNodeAsUnsolvable(node)
                continue
            
            # Step 6: Expand node n and add successors to Open
            successors = self.expandNode(node)
            self.open.update(successors)
        
        return "Failure"
    
    