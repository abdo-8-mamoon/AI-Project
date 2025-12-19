# tests_algorithms.py

from main import bfs, dfs, ucs, astar, get_successors, manhattan_distance
from main import GOAL_STATE 


# Example start states
START_STATE_1 = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

START_STATE_2 = (
    1, 3, 6,
    5, 0, 2,
    4, 7, 8
)

# List of algorithms to test
algorithms = [
    ("BFS", bfs),
    ("DFS", dfs),
    ("UCS", ucs),
    ("A*", astar)
]

# List of start states
start_states = [
    ("Start State 1", START_STATE_1),
    ("Start State 2", START_STATE_2)
]

# Run tests
for state_name, start_state in start_states:
    print(f"\n=== Testing {state_name} ===")
    print("Algorithm | Nodes Explored | Solution Length | Time (ms)")
    print("-" * 60)
    for name, func in algorithms:
        result = func(start_state)
        if result:
            path, nodes, t = result
            print(f"{name:<10} | {nodes:<14} | {len(path):<15} | {round(t, 2)}")
        else:
            print(f"{name:<10} | No Solution Found")
