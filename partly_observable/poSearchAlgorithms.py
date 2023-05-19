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
        TODO
        """
        return self.orSearch(self.po_problem.getInitialState(), [])

    def orSearch(self, b_state, path):
        """
        TODO
        """
        pass
    
    def andSearch(self, b_states, path):
        """
        TODO
        """
        pass

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
