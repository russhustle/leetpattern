import heapq
from collections import defaultdict
from typing import List, Tuple


# Dijkstra
def dijkstra(connections: List[Tuple[int, int, int]], start: int):
    graph = defaultdict(dict)
    nodes = set()

    for u, v, w in connections:
        graph[u][v] = w
        nodes.add(u)
        nodes.add(v)

    distances = {node: float("inf") for node in nodes}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        d1, n1 = heapq.heappop(heap)
        if d1 > distances[n1]:
            continue

        for n2, d2 in graph[n1].items():
            dist = d1 + d2
            if dist < distances[n2]:
                distances[n2] = dist
                heapq.heappush(heap, (dist, n2))

    return distances


# Bellman-Ford
def bellman_ford(connections: List[Tuple[int, int, int]], start: int):
    nodes = set()

    for u, v, _ in connections:
        nodes.add(u)
        nodes.add(v)

    distances = {node: float("inf") for node in nodes}
    distances[start] = 0

    for _ in range(len(nodes) - 1):
        for u, v, w in connections:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    return distances


connections = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
start = 2
print(dijkstra(connections, start))
# {1: 1, 2: 0, 3: 1, 4: 2}
print(bellman_ford(connections, start))
# {1: 1, 2: 0, 3: 1, 4: 2}
