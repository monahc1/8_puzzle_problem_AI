class Hamming:
    def h(self, current_state, goal_state):
        """Calculate Hamming distance: the number of misplaced tiles"""
        return sum(current_state[i][j] != goal_state[i][j] and current_state[i][j] != 0
                   for i in range(3) for j in range(3))
