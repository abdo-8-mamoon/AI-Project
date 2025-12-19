 8-Puzzle Problem – Search Algorithms Implementation
The 8-Puzzle is a classic Artificial Intelligence problem consisting of a 3×3 grid with 8 numbered tiles and one empty space (0).
The objective is to reach a goal configuration by sliding tiles into the empty space using valid moves.

Goal State:
1  3  6
5  0  2
4  7  8

GOAL_STATE = (1, 3, 6, 5, 0, 2, 4, 7, 8)

Initial State:
1  2  3
4  0  6
7  5  8

Implemented Algorithms:
- Breadth-First Search (BFS)
- Depth-First Search (DFS) with depth limit
- Uniform Cost Search (UCS)
- A* Search using Manhattan Distance heuristic

Heuristic Function:
The Manhattan Distance heuristic calculates the sum of horizontal and vertical distances of each tile from its goal position. The empty tile (0) is ignored.

Output:
For each algorithm, the program prints the number of explored nodes, solution length, and execution time in milliseconds.

Sample Output:
Algorithm | Nodes Explored | Solution Length | Time (ms)
------------------------------------------------------------
BFS | 181 | 5 | 3.12
DFS | 95 | 5 | 1.44
UCS | 167 | 5 | 4.01
A* | 42 | 5 | 0.87

Project Structure:
8-puzzle/
- puzzle.py
- README.md

How to Run:
Make sure Python 3.x is installed, then run:
python puzzle.py

Features:
- Fully working implementation
- Uses standard Python libraries only
- Clear comparison between search algorithms
- Suitable for AI coursework and academic projects

Concepts Covered:
State Space Search, Uninformed Search, Informed Search, Heuristic Functions, Performance Evaluation
