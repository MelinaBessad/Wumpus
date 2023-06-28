import time
import matplotlib.pyplot as plt
from problem import Wumpus
from searchAlgorithms import AStar
from searchAlgorithms import IDAStar

def main():

    num_snares = 3

    computation_times_astar = []
    solved_instances_astar = []
    computation_times_idastar = []
    solved_instances_idastar = []

    
    sizes = [4, 5, 6, 7, 8]  
    for size in sizes:
        maze_size = size
        maze = Wumpus(maze_size, num_snares)
        astar = AStar(maze, maze.heuristic)
        ida_star = IDAStar(maze, maze.heuristic)

        # A* 
        start_time_astar = time.time()
        solution_astar = astar.solve()
        end_time_astar = time.time()
        computation_time_astar = end_time_astar - start_time_astar
        computation_times_astar.append(computation_time_astar)
        solved_instances_astar.append(len(solution_astar))

        # IDA* 
        start_time_idastar = time.time()
        solution_idastar = ida_star.solve()
        end_time_idastar = time.time()
        computation_time_idastar = end_time_idastar - start_time_idastar
        computation_times_idastar.append(computation_time_idastar)
        solved_instances_idastar.append(len(solution_idastar))

    # les résultats :
    plt.figure(figsize=(10, 10))

    plt.subplot(2, 2, 1)
    plt.bar(sizes, computation_times_astar)
    plt.xlabel('Maze Size')
    plt.ylabel('Computation Time (A*)')
    plt.title('A*')

    plt.subplot(2, 2, 2)
    plt.bar(sizes, solved_instances_astar)
    plt.xlabel('Maze Size')
    plt.ylabel('Instances Solved (A*)')
    plt.title('A*')

    plt.subplot(2, 2, 3)
    plt.bar(sizes, computation_times_idastar)
    plt.xlabel('Maze Size')
    plt.ylabel('Computation Time (IDA*)')
    plt.title('IDA*')

    plt.subplot(2, 2, 4)
    plt.bar(sizes, solved_instances_idastar)
    plt.xlabel('Maze Size')
    plt.ylabel('Instances Solved (IDA*)')
    plt.title('IDA*')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
