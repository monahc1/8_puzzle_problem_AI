import numpy as np
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class EightPuzzle:
    def __init__(self, initial_state):
        self.state = np.array(initial_state)
        self.blank_pos = np.argwhere(self.state == 0)[0]
        self.moves = []  # Track the moves that have been made
        self.g_value = 0  # Cost from the start node to this node
        self.f_value = 0  # Sum of g + h

    def is_solved(self, goal_state):
        """Check if the current puzzle matches the goal state."""
        return np.array_equal(self.state, goal_state.state)

    def move(self, direction):
        """Move the blank tile in a given direction if possible."""
        row, col = self.blank_pos
        if direction == 'up' and row > 0:
            self._swap((row, col), (row - 1, col))
        elif direction == 'down' and row < 2:
            self._swap((row, col), (row + 1, col))
        elif direction == 'left' and col > 0:
            self._swap((row, col), (row, col - 1))
        elif direction == 'right' and col < 2:
            self._swap((row, col), (row, col + 1))

    def _swap(self, pos1, pos2):
        """Swap two positions in the puzzle."""
        self.state[tuple(pos1)], self.state[tuple(pos2)] = self.state[tuple(pos2)], self.state[tuple(pos1)]
        self.blank_pos = pos2  # Update the blank position



    def copy(self):
        """Return a copy of the current puzzle."""
        new_puzzle = EightPuzzle(self.state.copy())
        new_puzzle.f_value = self.f_value  # Make sure to copy the f_value
        return new_puzzle

    def legal_moves(self):
        """Returns a list of legal moves from the current state."""
        row, col = self.blank_pos
        moves = []
        if row > 0:
            moves.append('up')
        if row < 2:
            moves.append('down')
        if col > 0:
            moves.append('left')
        if col < 2:
            moves.append('right')
        return moves

    def result(self, move):
        """Returns the resulting state from applying a move."""
        new_puzzle = self.copy()
        new_puzzle.move(move)
        return new_puzzle

    def __eq__(self, other):
        return np.array_equal(self.state, other.state)

    def __hash__(self):
        return hash(self.state.tobytes())

    def __lt__(self, other):
        """Less than comparison for A* algorithm's priority queue based on f_value."""
        return self.f_value < other.f_value

    def __str__(self):
        """String representation of the puzzle state."""
        return '\n'.join([' '.join(map(str, row)) for row in self.state]) + '\n'
