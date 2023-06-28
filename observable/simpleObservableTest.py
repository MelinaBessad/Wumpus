#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from problem import Wumpus
from searchAlgorithms import AStar
from searchAlgorithms import IDAStar

def main():
    maze = Wumpus(4,3)
    #maze.generer_instance_aleatoire()
    astar = AStar(maze, maze.heuristic)
    ida_star = IDAStar(maze, maze.heuristic)
    # Afficher les informations
    print("============================================")
    print("===========Welcome to Wumpus Game===========")
    print("============================================")
    maze.afficher_labyrinthe()

    print("--------------------------------------------")
    print("---------------A star-----------------------")
    print("--------------------------------------------")
    print(astar.solve())
    print("--------------------------------------------")
    print("-----------IDA star-----------")
    print("--------------------------------------------")
    #print(ida_star.solve())
    
if __name__ == '__main__':
    main()
