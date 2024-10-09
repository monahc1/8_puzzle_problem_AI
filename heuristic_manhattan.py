class Manhattan:
    def h(self, current_state, goal_state):
        """Calculate Manhattan distance: sum of the vertical and horizontal distances of tiles from their goal positions"""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = current_state[i][j]
                if value != 0:  # Skip the blank tile
                    goal_pos = [(goal_state == value).nonzero()][0]
                    distance += abs(i - goal_pos[0][0]) + abs(j - goal_pos[1][0])
        return distance

