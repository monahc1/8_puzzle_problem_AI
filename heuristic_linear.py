class ManhattanLinearConflict:
    def manhattan_distance(self, current_state, goal_state):
        """Calculate Manhattan distance"""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = current_state[i][j]
                if value != 0:  # Skip the blank tile
                    # Find goal position of the tile
                    goal_pos = [(goal_state == value).nonzero()][0]
                    distance += abs(i - goal_pos[0][0]) + abs(j - goal_pos[1][0])
        return distance

    def linear_conflict(self, current_state, goal_state):
        """Calculate Linear Conflict"""
        conflict = 0

        # Check rows for linear conflict
        for row in range(3):
            current_row = current_state[row]
            goal_row = goal_state[row]
            for i in range(3):
                for j in range(i + 1, 3):
                    # Consider only non-zero values (ignore blank tile)
                    if current_row[i] != 0 and current_row[j] != 0:
                        # Ensure both tiles are supposed to be in the goal row
                        if current_row[i] in goal_row and current_row[j] in goal_row:
                            goal_pos_i = goal_row.tolist().index(current_row[i])
                            goal_pos_j = goal_row.tolist().index(current_row[j])
                            if goal_pos_i > goal_pos_j:  # Linear conflict
                                conflict += 1

        # Check columns for linear conflict
        for col in range(3):
            current_col = [current_state[row][col] for row in range(3)]
            goal_col = [goal_state[row][col] for row in range(3)]
            for i in range(3):
                for j in range(i + 1, 3):
                    # Consider only non-zero values (ignore blank tile)
                    if current_col[i] != 0 and current_col[j] != 0:
                        # Ensure both tiles are supposed to be in the goal column
                        if current_col[i] in goal_col and current_col[j] in goal_col:
                            goal_pos_i = goal_col.index(current_col[i])
                            goal_pos_j = goal_col.index(current_col[j])
                            if goal_pos_i > goal_pos_j:  # Linear conflict
                                conflict += 1

        return conflict * 2  # Each conflict adds 2 moves

    def h(self, current_state, goal_state):
        """Calculate the total heuristic: Manhattan distance + linear conflicts."""
        return self.manhattan_distance(current_state, goal_state) + self.linear_conflict(current_state, goal_state)
