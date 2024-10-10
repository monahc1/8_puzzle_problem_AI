from queue import PriorityQueue
import time

class AStarSolver:
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def search(self, start_puzzle, goal_puzzle):
        frontier = PriorityQueue()
        frontier.put((0, start_puzzle))
        explored = set()
        explored_nodes = 0
        start_time = time.time()

        while not frontier.empty():
            _, current_puzzle = frontier.get()

            if current_puzzle.is_solved(goal_puzzle):  # Compare with goal_puzzle
                elapsed_time = time.time() - start_time
                return current_puzzle.moves, explored_nodes, elapsed_time

            if current_puzzle not in explored:
                explored.add(current_puzzle)
                explored_nodes += 1

                for move in current_puzzle.legal_moves():
                    new_puzzle = current_puzzle.result(move)
                    new_puzzle.moves = current_puzzle.moves + [move]  # Append move to the current path
                    new_puzzle.g_value = current_puzzle.g_value + 1  # Increment g_value
                    new_puzzle.f_value = new_puzzle.g_value + self.heuristic.evaluate(new_puzzle, goal_puzzle)
                    frontier.put((new_puzzle.f_value, new_puzzle))

        return [], explored_nodes, time.time() - start_time
