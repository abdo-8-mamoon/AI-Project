from collections import deque
import heapq
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

# ---------------- Utility Functions ----------------

def get_successors(state):
    successors = []
    zero = state.index(0)
    for move in MOVES[zero]:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        successors.append(tuple(new_state))
    return successors


def manhattan_distance(state):
    dist = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = GOAL_STATE.index(tile)
            dist += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
    return dist

# ---------------- Search Algorithms ----------------

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


def dfs(start, limit=30):
    start_time = time.time()
    stack = [(start, [], 0)]
    visited = set()
    nodes = 0

    while stack:
        state, path, depth = stack.pop()
        nodes += 1
        if state == GOAL_STATE:
            return path, nodes, (time.time() - start_time) * 1000
        if depth < limit:
            for s in get_successors(state):
                if s not in visited:
                    visited.add(s)
                    stack.append((s, path + [s], depth + 1))


def ucs(start):
    start_time = time.time()
    pq = [(0, start, [])]
    visited = set()
    nodes = 0

    while pq:
        cost, state, path = heapq.heappop(pq)
        nodes += 1
        if state == GOAL_STATE:
            return path, nodes, (time.time() - start_time) * 1000
        if state not in visited:
            visited.add(state)
            for s in get_successors(state):
                heapq.heappush(pq, (cost + 1, s, path + [s]))


def astar(start):
    start_time = time.time()
    pq = [(manhattan_distance(start), 0, start, [])]
    visited = set()
    nodes = 0

    while pq:
        f, g, state, path = heapq.heappop(pq)
        nodes += 1
        if state == GOAL_STATE:
            return path, nodes, (time.time() - start_time) * 1000
        if state not in visited:
            visited.add(state)
            for s in get_successors(state):
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan_distance(s), g + 1, s, path + [s])
                )

# ---------------- Run All Algorithms ----------------
if __name__ == '__main__':
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    results = []

    for name, func in [
        ('BFS', bfs),
        ('DFS', dfs),
        ('UCS', ucs),
        ('A*', astar)
    ]:
        result = func(start_state)
        if result:
            path, nodes, t = result
            results.append((name, nodes, len(path), round(t, 2)))

    print('Algorithm | Nodes Explored | Solution Length | Time (ms)')
    print('-' * 60)
    for r in results:
        print(f'{r[0]:<10} | {r[1]:<14} | {r[2]:<15} | {r[3]}')
