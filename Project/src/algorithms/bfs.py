from collections import deque
import time

GOAL_STATE = (1, 3, 6,
               5, 0, 2,
               4, 7, 8)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def get_successors(state):
    successors = []
    zero = state.index(0)
    for move in MOVES[zero]:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        successors.append(tuple(new_state))
    return successors

def bfs(start):
    start_time = time.time()
    queue = deque([(start, [])])
    visited = set([start])
    nodes = 0

    while queue:
        state, path = queue.popleft()
        nodes += 1
        if state == GOAL_STATE:
            return path, nodes, (time.time() - start_time) * 1000
        for s in get_successors(state):
            if s not in visited:
                visited.add(s)
                queue.append((s, path + [s]))

if _name_ == '_main_':
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)
    result = bfs(start_state)
    if result:
        path, nodes, t = result
        print(f'BFS -> Nodes: {nodes}, Solution Length: {len(path)}, Time: {round(t, 2)} ms')
