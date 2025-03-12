---
comments: True
---

# Graph

- [ ] [277. Find the Celebrity](https://leetcode.cn/problems/find-the-celebrity/) (Medium) 👑
- [ ] [582. Kill Process](https://leetcode.cn/problems/kill-process/) (Medium) 👑
- [x] [323. Number of Connected Components in an Undirected Graph](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/) (Medium) 👑
- [ ] [1059. All Paths from Source Lead to Destination](https://leetcode.cn/problems/all-paths-from-source-lead-to-destination/) (Medium) 👑
- [ ] [1236. Web Crawler](https://leetcode.cn/problems/web-crawler/) (Medium) 👑
- [x] [305. Number of Islands II](https://leetcode.cn/problems/number-of-islands-ii/) (Hard) 👑
- [x] [694. Number of Distinct Islands](https://leetcode.cn/problems/number-of-distinct-islands/) (Medium) 👑
- [x] [1136. Parallel Courses](https://leetcode.cn/problems/parallel-courses/) (Medium) 👑

## 277. Find the Celebrity

- [LeetCode](https://leetcode.com/problems/find-the-celebrity/) | [LeetCode CH](https://leetcode.cn/problems/find-the-celebrity/) (Medium)

- Tags: two pointers, graph, interactive

## 582. Kill Process

- [LeetCode](https://leetcode.com/problems/kill-process/) | [LeetCode CH](https://leetcode.cn/problems/kill-process/) (Medium)

- Tags: array, hash table, tree, depth first search, breadth first search

## 323. Number of Connected Components in an Undirected Graph

- [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [LeetCode CH](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/) (Medium)

- Tags: depth first search, breadth first search, union find, graph

```python title="323. Number of Connected Components in an Undirected Graph - Python Solution"
from typing import List


# Union Find
def countComponents(n: int, edges: List[List[int]]) -> int:
    uf = UnionFind(n)
    count = n

    for u, v in edges:
        count -= uf.union(u, v)

    return count


class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, n):
        p = self.par[n]
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return 1


print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # 2

```

## 1059. All Paths from Source Lead to Destination

- [LeetCode](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) | [LeetCode CH](https://leetcode.cn/problems/all-paths-from-source-lead-to-destination/) (Medium)

- Tags: graph, topological sort

## 1236. Web Crawler

- [LeetCode](https://leetcode.com/problems/web-crawler/) | [LeetCode CH](https://leetcode.cn/problems/web-crawler/) (Medium)

- Tags: string, depth first search, breadth first search, interactive

## 305. Number of Islands II

- [LeetCode](https://leetcode.com/problems/number-of-islands-ii/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands-ii/) (Hard)

- Tags: array, hash table, union find

```python title="305. Number of Islands II - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:
    parent = defaultdict(tuple)
    islands = 0
    result = []
    visited = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def find(node):
        p = parent[node]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            parent[p1] = p2
            return True
        return False

    for r, c in positions:
        if (r, c) in visited:
            result.append(islands)
            continue

        islands += 1
        parent[(r, c)] = (r, c)
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in visited:
                if union((r, c), (nr, nc)):
                    islands -= 1

        result.append(islands)

    return result


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(numIslands2(m, n, positions))  # [1, 1, 2, 3]

```

## 694. Number of Distinct Islands

- [LeetCode](https://leetcode.com/problems/number-of-distinct-islands/) | [LeetCode CH](https://leetcode.cn/problems/number-of-distinct-islands/) (Medium)

- Tags: hash table, depth first search, breadth first search, union find, hash function

```python title="694. Number of Distinct Islands - Python Solution"
from collections import deque
from copy import deepcopy
from typing import List


# BFS
def numDistinctIslandsBFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    shapes = set()
    dirs = [[1, 0], [0, 1], [0, -1], [-1, 0]]

    def bfs(r, c):
        q = deque([(r, c)])
        shape = set()
        grid[r][c] = 0

        while q:
            row, col = q.popleft()
            shape.add((row - r, col - c))

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    q.append((nr, nc))
                    grid[nr][nc] = 0

        return tuple(shape)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                shapes.add(bfs(i, j))

    return len(shapes)


# DFS
def numDistinctIslandsDFS(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(r, c, org, shape):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
            return

        grid[r][c] = 0
        shape.add((r - org[0], c - org[1]))

        dfs(r - 1, c, org, shape)
        dfs(r + 1, c, org, shape)
        dfs(r, c - 1, org, shape)
        dfs(r, c + 1, org, shape)

    shapes = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                org = [i, j]
                shape = set()
                dfs(i, j, org, shape)
                shapes.add(tuple(shape))

    return len(shapes)


grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
print(numDistinctIslandsBFS(deepcopy(grid)))  # 3
print(numDistinctIslandsDFS(deepcopy(grid)))  # 3

```

## 1136. Parallel Courses

- [LeetCode](https://leetcode.com/problems/parallel-courses/) | [LeetCode CH](https://leetcode.cn/problems/parallel-courses/) (Medium)

- Tags: graph, topological sort
- Return the minimum number of semesters needed to take all courses.

![1136](../assets/1136.png)

```python title="1136. Parallel Courses - Python Solution"
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

```
