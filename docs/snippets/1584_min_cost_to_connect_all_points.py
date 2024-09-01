import heapq
from collections import defaultdict
from typing import List


# Prim's Algorithm
def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append((j, dist))
            graph[j].append((i, dist))

    cost = 0
    heap = [(0, 0)]  # (cost, node)
    visited = set()

    while heap:
        n1, d1 = heapq.heappop(heap)
        if n1 in visited:
            continue
        visited.add(n1)
        cost += d1

        for n2, d2 in graph[n1]:
            if n2 not in visited:
                heapq.heappush(heap, (n2, d2))

    return cost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(minCostConnectPoints(points))  # 20
