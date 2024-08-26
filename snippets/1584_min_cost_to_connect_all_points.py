import heapq
from collections import defaultdict
from typing import List


# Prim's Algorithm
def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)

    graph = defaultdict(list)
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append((dist, j))
            graph[j].append((dist, i))

    cost = 0
    visit = set()
    minHeap = [(0, 0)]

    while len(visit) < n:
        dist, node = heapq.heappop(minHeap)
        if node in visit:
            continue
        visit.add(node)
        cost += dist
        for distance, neighbor in graph[node]:
            if neighbor not in visit:
                heapq.heappush(minHeap, (distance, neighbor))

    return cost


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
print(minCostConnectPoints(points))  # 20
