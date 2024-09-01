import heapq
from collections import defaultdict
from typing import List


def minimumCost(n: int, connections: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v, c in connections:
        graph[u].append((c, v))
        graph[v].append((c, u))

    cost = 0
    heap = [(0, 1)]  # (cost, node)
    visited = set()

    while heap:
        c1, n1 = heapq.heappop(heap)

        if n1 in visited:
            continue

        visited.add(n1)

        cost += c1

        for c2, n2 in graph[n1]:
            if n2 not in visited:
                heapq.heappush(heap, (c2, n2))

    return cost if len(visited) == n else -1


n = 3
connections = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
print(minimumCost(n, connections))  # 6
