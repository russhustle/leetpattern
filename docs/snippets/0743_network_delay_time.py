from collections import defaultdict
from heapq import heappop, heappush
from typing import List


# Dijkstra
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    minHeap = [(0, k)]
    visited = set()
    t = 0

    while minHeap:
        w1, n1 = heappop(minHeap)

        if n1 in visited:
            continue

        visited.add(n1)
        t = max(t, w1)

        for n2, w2 in adj[n1]:
            if n2 not in visited:
                heappush(minHeap, (w1 + w2, n2))

    return t if len(visited) == n else -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # 2
