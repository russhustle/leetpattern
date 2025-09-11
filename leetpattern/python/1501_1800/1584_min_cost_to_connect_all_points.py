"""
- Tree: a connected acyclic graph
- Spanning Tree: a subgraph that is a tree and connects all the vertices together
- Minimum Spanning Tree (MST): a spanning tree with the minimum possible sum of edge weights
- Prim's Algorithm
  - Data Structure: Heap
  - Time Complexity: O(E * logV)
  - Space Complexity: O(V + E)
- Kruskal's Algorithm
  - Union Find
  - Time Complexity: O(E * logV)
  - Space Complexity: O(V + E)
"""

import heapq
from collections import defaultdict
from typing import List


# Prim
def minCostConnectPointsPrim(points: List[List[int]]) -> int:
    n = len(points)
    graph = defaultdict(list)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append((dist, j))
            graph[j].append((dist, i))

    cost = 0
    heap = [(0, 0)]  # (cost, node)
    visited = set()

    while heap:
        d1, n1 = heapq.heappop(heap)
        if n1 in visited:
            continue
        visited.add(n1)
        cost += d1

        for d2, n2 in graph[n1]:
            if n2 not in visited:
                heapq.heappush(heap, (d2, n2))

    return cost


# Kruskal
def minCostConnectPointsKruskal(points: List[List[int]]) -> int:
    n = len(points)
    par = {i: i for i in range(n)}
    rank = {i: 0 for i in range(n)}

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            par[p2] = p1
        elif rank[p1] < rank[p2]:
            par[p1] = p2
        else:
            par[p2] = p1
            rank[p1] += 1

        return True

    heap = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            heapq.heappush(heap, (dist, i, j))

    cost = 0
    while heap:
        d, n1, n2 = heapq.heappop(heap)
        if union(n1, n2):
            cost += d

    return cost


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(minCostConnectPointsPrim(points))  # 20
    print(minCostConnectPointsKruskal(points))  # 20
