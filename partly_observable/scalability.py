import matplotlib.pyplot as plt
from poProblem import POWumpus
from poSearchAlgorithms import AndOrSearch
import time

def main():
    sizes = [4, 5, 6, 7, 8]  
    num_snares = 3  

    computation_times_andorsearch = []
    solved_instances_andorsearch = []

    for size in sizes:
        problem = POWumpus(size, num_snares)
        andOrSearch = AndOrSearch(problem)

        start_time = time.time()
        solution_andorsearch = andOrSearch.solve()
        end_time = time.time()
        computation_time_andorsearch = end_time - start_time

        computation_times_andorsearch.append(computation_time_andorsearch)
        #solved_instances_andorsearch.append(len(solution_andorsearch))
        if solution_andorsearch is not None:
            solved_instances_andorsearch.append(1)  
        else:
            solved_instances_andorsearch.append(0)


    # les résultats :
    plt.figure(figsize=(10, 10))

    plt.subplot(2, 2, 1)
    plt.bar(sizes, computation_times_andorsearch)
    plt.xlabel('Maze Size')
    plt.ylabel('Computation Time (AndOrSearch)')
    plt.title('AndOrSearch')

    plt.subplot(2, 2, 2)
    plt.bar(sizes, solved_instances_andorsearch)
    plt.xlabel('Maze Size')
    plt.ylabel('Instances Solved (AndOrSearch)')
    plt.title('AndOrSearch')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
