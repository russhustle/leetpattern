import heapq
from collections import defaultdict
from typing import List


# 1. Dijkstra - Set
def networkDelayTime1(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    heap = [(0, k)]
    visit = set()
    t = 0

    while heap:
        w1, n1 = heapq.heappop(heap)
        if n1 in visit:
            continue

        visit.add(n1)
        t = w1

        for n2, w2 in graph[n1]:
            heapq.heappush(heap, (w1 + w2, n2))

    return t if len(visit) == n else -1


# 2. Dijkstra - Dict
def networkDelayTime2(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    heap = [(0, k)]
    dist = defaultdict(int)

    while heap:
        w1, n1 = heapq.heappop(heap)
        if n1 in dist:
            continue

        dist[n1] = w1

        for n2, w2 in graph[n1]:
            heapq.heappush(heap, (w1 + w2, n2))

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


# |------------|---------|---------|
# |  Approach  |  Time   |  Space  |
# |------------|---------|---------|
# |Dijkstra    |O(E*logV)|  O(V+E) |
# |Bellman-Ford|O(E*V)   |  O(V)   |
# |------------|---------|---------|


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime1(times, n, k))  # 2
print(networkDelayTime2(times, n, k))  # 2
print(networkDelayTimeBF(times, n, k))  # 2
