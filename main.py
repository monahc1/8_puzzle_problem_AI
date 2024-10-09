from eight_puzzle import EightPuzzle
from astar import AStarSolver

# Import the desired heuristic
from heuristic_hamming import Hamming
from heuristic_manhattan import Manhattan
from heuristic_linear import ManhattanLinearConflict

def run_a_star_solver(heuristic):
    """Run A* solver with the chosen heuristic"""
    initial_state = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]  # Example initial state
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]    # Target solved state
    
    initial_puzzle = EightPuzzle(initial_state)
    goal_puzzle = EightPuzzle(goal_state)

    solver = AStarSolver(heuristic)
    solution_moves, elapsed_time = solver.search(initial_puzzle, goal_puzzle)

    if solution_moves:
        print(f"Solution found in {elapsed_time:.4f} seconds")
        print(f"Moves: {solution_moves}")
    else:
        print("No solution found")

if __name__ == "__main__":
    # Test with Hamming Distance
    print("Testing A* with Hamming Distance")
    run_a_star_solver(Hamming())

    # Test with Manhattan Distance
    print("\nTesting A* with Manhattan Distance")
    run_a_star_solver(Manhattan())

    # Test with Manhattan + Linear Conflict
    print("\nTesting A* with Manhattan Distance + Linear Conflict")
    run_a_star_solver(ManhattanLinearConflict())

