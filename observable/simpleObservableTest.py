#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from problem import Wumpus
from searchAlgorithms import AStar
from searchAlgorithms import IDAStar

def main():
    maze = Wumpus()
    astar = AStar(maze, maze.heuristic)
    ida_star = IDAStar(maze, maze.heuristic)

    print("monster's position  : ",maze.wumpus_position)
    print("treasure's position :",maze.treasure_position)
    print("-----------A star------------")
    print(astar.solve())
    #print("-----------IDA star-----------")
    #print(ida_star.solve())
    
if __name__ == '__main__':
    main()
    