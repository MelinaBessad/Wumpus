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
    problem = POWumpus(4,3)
    andOrSearch = AndOrSearch(problem)
    
    print("============================================")
    print("===========Welcome to Wumpus Game===========")
    print("============================================")
    problem.afficher_labyrinthe()
    print("--------------------------------------------")
    print("---------------AndOrSearch------------------")
    print("--------------------------------------------")
    andOrSearch.solve()
    
    #aoStar = AOStar(problem, problem.heuristic)
    #print(aoStar.solve())    
    
    
if __name__ == '__main__':
    main()