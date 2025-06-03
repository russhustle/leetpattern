from collections import defaultdict, deque
from typing import List


# Topological Sort
def checkIfPrerequisite(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    graph = defaultdict(list)
    indegree = defaultdict(int)
    record = defaultdict(set)  # store all prerequisites for each course

    for a, b in prerequisites:
        graph[a].append(b)
        indegree[b] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            record[nxt].add(cur)
            record[nxt].update(record[cur])

            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    res = []
    for u, v in queries:
        res.append(u in record[v])
    return res


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    queries = [[0, 1], [1, 0]]
    assert checkIfPrerequisite(numCourses, prerequisites, queries) == [
        False,
        True,
    ]
    numCourses = 3
    prerequisites = [[1, 2], [1, 0], [2, 0]]
    queries = [[1, 0], [1, 2]]
    assert checkIfPrerequisite(numCourses, prerequisites, queries) == [
        True,
        True,
    ]
