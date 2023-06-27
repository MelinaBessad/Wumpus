#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from problem import Wumpus
from searchAlgorithms import AStar
from searchAlgorithms import IDAStar

def main():
    maze = Wumpus()
    astar = AStar(maze, maze.heuristic)
    ida_star = IDAStar(maze, maze.heuristic)
    
    print("============================================")
    print("===========Welcome to Wumpus Game===========")
    print("============================================")
    print("monster's position  : ",maze.wumpus_position)
    print("treasure's position :",maze.treasure_position)
    print("--------------------------------------------")
    print("---------------A star-----------------------")
    print("--------------------------------------------")
    print(astar.solve())
    print("--------------------------------------------")
    #print("-----------IDA star-----------")
    print("--------------------------------------------")
    #print(ida_star.solve())
    
if __name__ == '__main__':
    main()
    