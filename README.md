# 8-Puzzle Solver using A* Algorithm

This project implements the 8-puzzle solver using the A* search algorithm with different heuristic functions: Hamming Distance, Manhattan Distance, and Manhattan Distance with Linear Conflict.


### Files and Their Purpose

- **`eight_puzzle.py`**: 
  Contains the `EightPuzzle` class which defines the puzzle board, legal moves, and functionality for checking if the puzzle is solved. This class also handles moving tiles around the board.

- **`astar.py`**: 
  Contains the implementation of the A* search algorithm, which finds the optimal solution to the 8-puzzle using a given heuristic. The A* solver uses a priority queue to explore puzzle states based on their f-values (g + h).

- **`heuristic_hamming.py`**: 
  Implements the Hamming distance heuristic, which counts the number of tiles that are not in their goal position (excluding the blank tile).

- **`heuristic_manhattan.py`**: 
  Implements the Manhattan distance heuristic, which sums the vertical and horizontal distances of each tile from its goal position.

- **`heuristic_linear.py`**: 
  Implements the Manhattan distance combined with Linear Conflict. Linear Conflict adds a penalty for tiles that are in the same row or column as their goal position but in the wrong order.

- **`main.py`**: 
  This is the main script to test the A* algorithm with each heuristic. It runs the solver on a predefined 8-puzzle configuration and outputs the sequence of moves and the time taken for each heuristic.

## Requirements

To run this project, you need the following:
- Python 3.x
- `numpy` (for matrix manipulation)
  
You can install `numpy` using `pip`:

```bash
pip install numpy
```

### How to Run

Clone or download the project to your local machine.
```bash
cd 8-puzzle-solver
```
In the terminal, navigate to the project directory:
```bash
python main.py
```



### Example output:
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

