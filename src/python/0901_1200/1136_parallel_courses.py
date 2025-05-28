"""
- Return the minimum number of semesters needed to take all courses.

![1136](../../assets/1136.png)
"""

from collections import deque
from typing import List


# Topological Sort
def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    graph = {i: [] for i in range(1, n + 1)}
    indegree = {i: 0 for i in range(1, n + 1)}

    for pre, nxt in relations:
        graph[pre].append(nxt)
        indegree[nxt] += 1

    q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
    semester = 0
    done = 0

    while q:
        semester += 1
        size = len(q)

        for _ in range(size):
            pre = q.popleft()
            done += 1

            for nxt in graph[pre]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

    return semester if done == n else -1


n = 3
relations = [[1, 3], [2, 3]]
print(minimumSemesters(n, relations))  # 2
