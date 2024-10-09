
# 8-Puzzle Solver using A* Algorithm 🧩🔍

This project implements the 8-puzzle solver using the **A*** search algorithm with different heuristic functions: **Hamming Distance**, **Manhattan Distance**, and **Manhattan Distance with Linear Conflict**.

### 📂 Files and Their Purpose

- **`eight_puzzle.py`**: 🧮  
  Defines the puzzle board, legal moves, and puzzle-solving functionality.

- **`astar.py`**: 🧠🚀  
  Implements the A* search algorithm to find the optimal solution with a priority queue.

- **`heuristic_hamming.py`**: 🎯  
  Implements Hamming Distance heuristic, counting misplaced tiles.

- **`heuristic_manhattan.py`**: 🛣️  
  Implements Manhattan Distance heuristic, summing the distance each tile needs to move.

- **`heuristic_linear.py`**: 🔀💥  
  Adds Linear Conflict to Manhattan, penalizing misplaced tiles in the same row or column.

- **`main.py`**: 🏁  
  The main script to test the A* algorithm with different heuristics, showing solution and timing.

## 🛠️ Requirements

You’ll need **Python 3.x** and **`numpy`** (install it with `pip install numpy`).

### 🚀 How to Run

1. Clone/download the project.
2. Navigate to the directory:
```bash
cd 8-puzzle-solver
```
3. Run the main script:
```bash
python main.py
```

### 📝 Example output:
```
Testing A* with Hamming Distance
Solution found in 0.0004 seconds
Moves: ['down', 'right', 'up', 'left', 'down', 'right']

Testing A* with Manhattan Distance
Solution found in 0.0003 seconds
Moves: ['right', 'down', 'left', 'up', 'right']

Testing A* with Manhattan Distance + Linear Conflict
Solution found in 0.0005 seconds
Moves: ['down', 'right', 'left', 'up', 'right', 'down']
```

