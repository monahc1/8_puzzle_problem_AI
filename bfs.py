from collections import deque
import time 
def bfs_solve(puzzle, goal_puzzle):
    """
    Solve the 8-puzzle using BFS and return the sequence of moves.
    :param puzzle: The initial puzzle state as an EightPuzzle object.
    :param goal_puzzle: The goal puzzle state to compare against.
    :return: A tuple containing the list of moves to solve the puzzle and the number of explored nodes.
    """
    frontier = deque([(puzzle.copy(), [])])  # Queue of (puzzle, moves)
    explored = set()
    explored_nodes = 0
    start_time = time.time()

    while frontier:
        current_puzzle, moves = frontier.popleft()

        if current_puzzle.is_solved(goal_puzzle):
            elapsed_time = time.time() - start_time

            return moves, explored_nodes  # Return the list of moves to solve the puzzle and number of explored nodes

        if current_puzzle not in explored:
            explored.add(current_puzzle)
            explored_nodes += 1

            for move in current_puzzle.legal_moves():
                new_puzzle = current_puzzle.result(move)
                frontier.append((new_puzzle, moves + [move]))

    return [], explored_nodes  # No solution found
