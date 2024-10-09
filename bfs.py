from collections import deque

def bfs_solve(puzzle):
    """
    Solve the 8-puzzle using BFS and return the sequence of moves.
    :param puzzle: The initial puzzle state as an EightPuzzle object.
    :return: A tuple containing the list of moves to solve the puzzle and the number of explored nodes.
    """
    frontier = deque([(puzzle.copy(), [])])  # Queue of (puzzle, moves)
    explored = set()
    explored_nodes = 0

    while frontier:
        current_puzzle, moves = frontier.popleft()

        if current_puzzle.is_solved():
            return moves, explored_nodes  # Return the list of moves to solve the puzzle and number of explored nodes

        if current_puzzle not in explored:
            explored.add(current_puzzle)
            explored_nodes += 1

            for move in current_puzzle.legal_moves():
                new_puzzle = current_puzzle.result(move)
                frontier.append((new_puzzle, moves + [move]))

    return [], explored_nodes  # No solution found
