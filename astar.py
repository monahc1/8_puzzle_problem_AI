import time
import heapq

class AStarSolver:
    """A* Search Algorithm using the provided Heuristics"""

    def __init__(self, heuristic):
        self.heuristic = heuristic

    def g(self, current_puzzle, initial_puzzle):
        """Calculate the g-value: distance from the initial state (depth of the node)"""
        count = 0
        while current_puzzle.state.tolist() != initial_puzzle.state.tolist():
            count += 1
            current_puzzle = current_puzzle.parent
        return count

    def search(self, initial_puzzle, goal_puzzle):
        """A* search algorithm using the provided heuristic"""
        start_time = time.time()
        goal_state = goal_puzzle.state

        # Priority queue (min-heap) where each element is (f_value, puzzle_state, path_to_goal)
        frontier = []
        heapq.heappush(frontier, (0, initial_puzzle.copy(), []))
        explored = set()

        # Counter for the number of explored nodes
        explored_nodes = 0
        
        while frontier:
            cost, current_puzzle, path = heapq.heappop(frontier)

            if current_puzzle.is_solved():
                return path, explored_nodes, time.time() - start_time

            if tuple(current_puzzle.state.flatten()) not in explored:
                explored.add(tuple(current_puzzle.state.flatten()))

                # Increment the explored nodes counter
                explored_nodes += 1

                for move in current_puzzle.legal_moves():
                    new_puzzle = current_puzzle.result(move)
                    new_path = path + [move]

                    # Calculate g (cost so far) + h (chosen heuristic)
                    g_value = len(new_path)
                    h_value = self.heuristic.h(new_puzzle.state, goal_state)
                    new_puzzle.f_value = g_value + h_value  # Set the f_value before pushing into heap

                    heapq.heappush(frontier, (new_puzzle.f_value, new_puzzle, new_path))

        return [], explored_nodes, time.time() - start_time  # No solution found
