from collections import deque
from itertools import count
from typing import List


# BFS
def shortestDistanceAfterQueries(
    n: int, queries: List[List[int]]
) -> List[int]:
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        g[i].append(i + 1)

    vis = [-1 for _ in range(n)]

    def bfs(i: int) -> int:
        q = deque([0])
        for step in count(1):
            tmp = q
            q = deque()
            for x in tmp:
                for y in g[x]:
                    if y == n - 1:
                        return step
                    if vis[y] != i:
                        vis[y] = i
                        q.append(y)
        return -1

    res = [0] * len(queries)
    for i, (l, r) in enumerate(queries):
        g[l].append(r)
        res[i] = bfs(i)

    return res


n = 5
queries = [[2, 4], [0, 2], [0, 4]]
print(shortestDistanceAfterQueries(n, queries))  # [3, 2, 1]
