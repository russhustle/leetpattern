"""
- ![1168_0](../../assets/1168_0.png)

- ![1168_1](../../assets/1168_1.png)
"""

import heapq
from collections import defaultdict
from typing import List


# Prim
def minCostToSupplyWater1(
    n: int, wells: List[int], pipes: List[List[int]]
) -> int:
    graph = defaultdict(list)

    for h1, h2, cost in pipes:
        graph[h1].append((h2, cost))
        graph[h2].append((h1, cost))

    # Add the cost of the wells to the graph (house 0)
    for i in range(n):
        graph[0].append((i + 1, wells[i]))
        graph[i + 1].append((0, wells[i]))

    visited = set([0])
    heap = [(cost, dest) for dest, cost in graph[0]]
    heapq.heapify(heap)

    cost = 0

    while heap:
        c1, n1 = heapq.heappop(heap)
        if n1 in visited:
            continue
        visited.add(n1)
        cost += c1

        for n2, c2 in graph[n1]:
            if n2 not in visited:
                heapq.heappush(heap, (c2, n2))

    return cost


# Kruskal
def minCostToSupplyWater2(
    n: int, wells: List[int], pipes: List[List[int]]
) -> int:
    par = list(range(n + 1))
    rank = [0] * (n + 1)

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            if rank[p1] < rank[p2]:
                par[p1] = p2
            elif rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
                rank[p2] += 1
            return True
        return False

    graph = [(c, 0, i + 1) for i, c in enumerate(wells)]
    for h1, h2, c in pipes:
        graph.append((c, h1, h2))

    graph.sort()

    cost = 0

    for c, h1, h2 in graph:
        if union(h1, h2):
            cost += c

    return cost


# |------------|------------------|---------|
# |  Approach  |       Time       |  Space  |
# |------------|------------------|---------|
# |    Prim    | O((V + E) log V) | O(V + E)|
# |  Kruskal   |     O(E log E)   | O(V + E)|
# |------------|------------------|---------|


n = 3
wells = [1, 2, 2]
pipes = [[1, 2, 1], [2, 3, 1]]
print(minCostToSupplyWater1(n, wells, pipes))  # 3
print(minCostToSupplyWater2(n, wells, pipes))  # 3
