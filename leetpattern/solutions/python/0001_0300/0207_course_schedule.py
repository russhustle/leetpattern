"""
- Return true if it is possible to finish all courses, otherwise return false.
- Dependency relationships imply the topological sort algorithm.
- Cycle detection
- Topological Sort
  - DAG (Directed Acyclic Graph)
  - Time complexity: O(V+E)
  - Space complexity: O(V+E)
  - Prerequisites: Indegree (Look at the problem 1557. Minimum Number of Vertices to Reach All Nodes)
    - Indegree: Number of incoming edges to a vertex
  - Applications: task scheduling, course scheduling, build systems, dependency resolution, compiler optimization, etc.

![ts1](../../assets/graph_ts1.png)

![ts2](../../assets/graph_ts2.png)

Course to prerequisites mapping

```mermaid
flowchart LR
    0((0)) --> 1((1))
    0((0)) --> 2((2))
    1((1)) --> 3((3))
    3((3)) --> 4((4))
    1((1)) --> 4((4))
```

Prerequisites to course mapping

```mermaid
flowchart LR
    1((1)) --> 0((0))
    2((2)) --> 0((0))
    3((3)) --> 1((1))
    4((4)) --> 3((3))
    4((4)) --> 1((1))
```

| course       | 0   | 0   | 1   | 1   | 3   |
| ------------ | --- | --- | --- | --- | --- |
| prerequisite | 1   | 2   | 3   | 4   | 4   |

| index     | 0   | 1   | 2   | 3   | 4   |
| --------- | --- | --- | --- | --- | --- |
| in-degree | 0   | 0   | 0   | 0   | 0   |

Initialize

- graph

| prerequisite | 1     | 2     | 3     | 4        |
| ------------ | ----- | ----- | ----- | -------- |
| course       | `[0]` | `[0]` | `[1]` | `[1, 3]` |

- in-degree

|           | 0   | 1   | 2   | 3   | 4   |
| --------- | --- | --- | --- | --- | --- |
| in-degree | 2   | 2   | 0   | 1   | 0   |

- queue: `[2, 4]`
- pop `2` from the queue

```mermaid
flowchart LR
    1((1)) --> 0((0))
    3((3)) --> 1((1))
    4((4)) --> 3((3))
    4((4)) --> 1((1))
```

|           | 0   | 1   | 2   | 3   | 4   |
| --------- | --- | --- | --- | --- | --- |
| in-degree | 1   | 2   | 0   | 1   | 0   |

- queue: `[4]`
- pop `4` from the queue

```mermaid
flowchart LR
    1((1)) --> 0((0))
    3((3)) --> 1((1))
```

|           | 0   | 1   | 2   | 3   | 4   |
| --------- | --- | --- | --- | --- | --- |
| in-degree | 1   | 1   | 0   | 0   | 0   |

- queue: `[3]`
- pop `3` from the queue

```mermaid
flowchart LR
    1((1)) --> 0((0))
```

|           | 0   | 1   | 2   | 3   | 4   |
| --------- | --- | --- | --- | --- | --- |
| in-degree | 1   | 0   | 0   | 0   | 0   |

- queue: `[1]`
- pop `1` from the queue

```mermaid
flowchart LR
    0((0))
```

|           | 0   | 1   | 2   | 3   | 4   |
| --------- | --- | --- | --- | --- | --- |
| in-degree | 0   | 0   | 0   | 0   | 0   |

- queue: `[0]`
- pop `0` from the queue
- All courses are taken. Return `True`.
"""

from collections import defaultdict, deque
from typing import List


# BFS (Kahn's Algorithm)
def canFinishBFS(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for crs, pre in prerequisites:
        graph[pre].append(crs)
        indegree[crs] += 1

    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0

    while q:
        crs = q.popleft()
        count += 1

        for nxt in graph[crs]:
            indegree[nxt] -= 1

            if indegree[nxt] == 0:
                q.append(nxt)

    return count == numCourses


# DFS + Set
def canFinishDFS1(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for crs, pre in prerequisites:
        graph[crs].append(pre)

    visiting = set()

    def dfs(crs):
        if crs in visiting:  # cycle detected
            return False
        if graph[crs] == []:
            return True

        visiting.add(crs)

        for pre in graph[crs]:
            if not dfs(pre):
                return False

        visiting.remove(crs)
        graph[crs] = []

        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


# DFS + List
def canFinishDFS2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for pre, crs in prerequisites:
        graph[crs].append(pre)

    # 0: init, 1: visiting, 2: visited
    status = [0] * numCourses

    def dfs(crs):
        if status[crs] == 1:  # cycle detected
            return False
        if status[crs] == 2:
            return True

        status[crs] = 1

        for pre in graph[crs]:
            if not dfs(pre):
                return False

        status[crs] = 2
        return True

    for crs in range(numCourses):
        if not dfs(crs):
            return False
    return True


prerequisites = [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]
print(canFinishBFS(5, prerequisites))  # True
print(canFinishDFS1(5, prerequisites))  # True
print(canFinishDFS2(5, prerequisites))  # True
