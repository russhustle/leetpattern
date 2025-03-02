from collections import defaultdict, deque
from typing import List


# Tree Diameter
def treeDiameter(edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {0}
    q = deque([0])
    cur = 0

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)

    visited = {cur}
    q = deque([cur])
    res = -1

    while q:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited.add(nxt)
        res += 1

    return res


edges = [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]
assert treeDiameter(edges) == 4
