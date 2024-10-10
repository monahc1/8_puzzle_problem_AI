# class Hamming:
#     def h(self, current_state, goal_state):
#         """Calculate Hamming distance: the number of misplaced tiles"""
#         return sum(current_state[i][j] != goal_state[i][j] and current_state[i][j] != 0
#                    for i in range(3) for j in range(3))

class Hamming:
    """Hamming Distance heuristic: counts the number of misplaced tiles."""

    @staticmethod
    def h(current_state, goal_state):
        """Calculates Hamming Distance between current state and goal state."""
        hamming_count = sum(1 for i, j in zip(current_state.flatten(), goal_state.flatten()) if i != j and i != 0)
        return hamming_count
