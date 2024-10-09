import time
import heapq

class AStarSolver:
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

        # Priority queue (min-heap) where each element is (cost, puzzle_state, path_to_goal)
        frontier = []
        heapq.heappush(frontier, (0, initial_puzzle.copy(), []))
        explored = set()

        while frontier:
            cost, current_puzzle, path = heapq.heappop(frontier)

            if current_puzzle.is_solved():
                return path, time.time() - start_time

            if tuple(current_puzzle.state.flatten()) not in explored:
                explored.add(tuple(current_puzzle.state.flatten()))

                for move in current_puzzle.legal_moves():
                    new_puzzle = current_puzzle.result(move)
                    new_path = path + [move]

                    # Calculate g (cost so far) + h (chosen heuristic)
                    g_value = len(new_path)
                    h_value = self.heuristic.h(new_puzzle.state, goal_state)
                    f_value = g_value + h_value

                    heapq.heappush(frontier, (f_value, new_puzzle, new_path))

        return [], time.time() - start_time  # No solution found
