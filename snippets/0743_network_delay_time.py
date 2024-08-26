from collections import defaultdict
from heapq import heappop, heappush
from typing import List


# 1. Dijkstra - Set
def networkDelayTime1(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    minHeap = [(0, k)]  # (weight, node)
    visited = set()
    delay = 0

    while minHeap:
        cur, u = heappop(minHeap)

        if u in visited:
            continue
        visited.add(u)

        delay = max(delay, cur)

        for v, w in graph[u]:
            if v not in visited:
                heappush(minHeap, (cur + w, v))

    return delay if len(visited) == n else -1


# 2. Dijkstra - Dict
def networkDelayTime2(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    minHeap = [(0, k)]  # (weight, node)
    dist = defaultdict(int)
    dist[k] = 0

    while minHeap:
        cur, u = heappop(minHeap)

        if cur > dist[u]:
            continue

        for v, w in graph[u]:
            path = cur + w
            if v not in dist or path < dist[v]:
                dist[v] = path
                heappush(minHeap, (path, v))

    return max(dist.values()) if len(dist) == n else -1


# 3. Bellman-Ford
def networkDelayTimeBF(times: List[List[int]], n: int, k: int) -> int:
    # TC: O(N * E)
    # SC: O(N)

    dist = [float("inf")] * n
    dist[k - 1] = 0

    for _ in range(n - 1):
        for u, v, w in times:
            if dist[u - 1] + w < dist[v - 1]:
                dist[v - 1] = dist[u - 1] + w

    if any(d == float("inf") for d in dist):
        return -1

    return max(dist)


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime1(times, n, k))  # 2
print(networkDelayTime2(times, n, k))  # 2
print(networkDelayTimeBF(times, n, k))  # 2
