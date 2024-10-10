import time
import heapq

class PuzzleState:
    def __init__(self, state, parent=None, move=None, g_value=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g_value = g_value
        self.f_value = 0  # f = g + h

    def is_solved(self, goal_state):
        return self.state.tolist() == goal_state.tolist()

    def legal_moves(self):
        # Assume this function returns a list of legal moves based on the current state
        pass

    def result(self, move):
        # Assume this function returns a new PuzzleState after applying the given move
        pass

class AStarSolver:
    """A* Search Algorithm using the provided Heuristic"""

    def __init__(self, heuristic):
        self.heuristic = heuristic

    def search(self, initial_puzzle, goal_puzzle):
        """A* search algorithm using the provided heuristic"""

        start_time = time.time()
        goal_state = goal_puzzle.state

        # Priority queue (min-heap) where each element is (f_value, PuzzleState)
        frontier = []
        heapq.heappush(frontier, (0, initial_puzzle))

        explored = set()

        # Counter for the number of explored nodes
        explored_nodes = 0

        while frontier:
            _, current_puzzle = heapq.heappop(frontier)

            if current_puzzle.is_solved(goal_state):
                return self._reconstruct_path(current_puzzle), explored_nodes, time.time() - start_time

            state_tuple = tuple(current_puzzle.state.flatten())
            if state_tuple not in explored:
                explored.add(state_tuple)
                explored_nodes += 1

                for move in current_puzzle.legal_moves():
                    new_puzzle = current_puzzle.result(move)
                    new_puzzle.g_value = current_puzzle.g_value + 1  # Increment g_value by 1 for each move

                    # Calculate h (heuristic value)
                    h_value = self.heuristic.h(new_puzzle.state, goal_state)

                    # Set the f_value (g + h)
                    new_puzzle.f_value = new_puzzle.g_value + h_value

                    heapq.heappush(frontier, (new_puzzle.f_value, new_puzzle))

        return [], explored_nodes, time.time() - start_time  # No solution found

    def _reconstruct_path(self, puzzle):
        """Reconstruct the path to the goal by following parent nodes."""
        path = []
        current = puzzle
        while current.parent is not None:
            path.append(current.move)
            current = current.parent
        return path[::-1]  # Reverse the path to get the correct order

