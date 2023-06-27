#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Wumpus test in partially observable environment

@author: Hugo Gilbert
"""

from poProblem import POWumpus
from poSearchAlgorithms import AndOrSearch
from poSearchAlgorithms import AOStar



def main():
    problem = POWumpus()
    andOrSearch = AndOrSearch(problem)
    andOrSearch.solve()

    print("monster's position  : ",problem.problem.wumpus_position)
    print("treasure's position :",problem.problem.treasure_position)
    
    #aoStar = AOStar(problem, problem.heuristic)
    #print(aoStar.solve())    
    
    
if __name__ == '__main__':
    main()