from collections import defaultdict
from heapq import heappop, heappush
from typing import List


# Dijkstra - Set
def networkDelayTime1(times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    minHeap = [(0, k)]  # (weight, node)
    visited = set()
    delay = 0

    while minHeap:
        cur, u = heappop(minHeap)

        if u in visited:
            continue
        visited.add(u)

        delay = max(delay, cur)

        for v, w in adj[u]:
            if v not in visited:
                heappush(minHeap, (cur + w, v))

    return delay if len(visited) == n else -1


# Dijkstra - Dict
def networkDelayTime2(times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    minHeap = [(0, k)]  # (weight, node)
    dist = defaultdict(int)
    dist[k] = 0

    while minHeap:
        cur, u = heappop(minHeap)

        if cur > dist[u]:
            continue

        for v, w in adj[u]:
            path = cur + w
            if v not in dist or path < dist[v]:
                dist[v] = path
                heappush(minHeap, (path, v))

    return max(dist.values()) if len(dist) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime1(times, n, k))  # 2
print(networkDelayTime2(times, n, k))  # 2
