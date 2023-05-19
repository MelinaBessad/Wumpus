#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Wumpus test in partially observable environment

@author: Hugo Gilbert
"""

from partly_observable.poProblem import POWumpus
from partly_observable.poSearchAlgorithms import AndOrSearch
from partly_observable.poSearchAlgorithms import AOStar



def main():
    problem = POWumpus()
    andOrSearch = AndOrSearch(problem)
    print(andOrSearch.solve())
    
    aoStar = AOStar(problem, problem.heuristic)
    print(aoStar.solve())    
    
    
if __name__ == '__main__':
    main()