#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from observable.problem import Wumpus
from observable.searchAlgorithms import AStar

def main():
    maze = Wumpus()
    astar = AStar(maze, maze.heuristic)
    
    print(astar.solve())
    
if __name__ == '__main__':
    main()
    