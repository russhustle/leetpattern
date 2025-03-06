from collections import deque
from typing import List


def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
        return [0]

    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    q = deque([i for i in range(n) if len(graph[i]) == 1])
    remaining = n

    while remaining > 2:
        size = len(q)
        remaining -= size

        for _ in range(size):
            cur = q.popleft()
            nei = graph[cur].pop()
            graph[nei].remove(cur)

            if len(graph[nei]) == 1:
                q.append(nei)

    return list(q)


n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(findMinHeightTrees(n, edges))  # [3, 4]
