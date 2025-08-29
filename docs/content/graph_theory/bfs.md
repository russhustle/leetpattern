---
comments: True
---

# BFS

## Table of Contents

- [x] [1926. Nearest Exit from Entrance in Maze](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/) (Medium)
- [x] [934. Shortest Bridge](https://leetcode.cn/problems/shortest-bridge/) (Medium)
- [x] [433. Minimum Genetic Mutation](https://leetcode.cn/problems/minimum-genetic-mutation/) (Medium)
- [x] [127. Word Ladder](https://leetcode.cn/problems/word-ladder/) (Hard)
- [x] [1306. Jump Game III](https://leetcode.cn/problems/jump-game-iii/) (Medium)
- [x] [542. 01 Matrix](https://leetcode.cn/problems/01-matrix/) (Medium)
- [x] [1091. Shortest Path in Binary Matrix](https://leetcode.cn/problems/shortest-path-in-binary-matrix/) (Medium)
- [x] [863. All Nodes Distance K in Binary Tree](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/) (Medium)
- [x] [864. Shortest Path to Get All Keys](https://leetcode.cn/problems/shortest-path-to-get-all-keys/) (Hard)

## 1926. Nearest Exit from Entrance in Maze

-   [LeetCode](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) | [LeetCode CH](https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/) (Medium)

-   Tags: array, breadth first search, matrix
```python title="1926. Nearest Exit from Entrance in Maze - Python Solution"
from collections import deque
from typing import List


# BFS
def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
    m, n = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(entrance[0], entrance[1], 0)])
    maze[entrance[0]][entrance[1]] = "+"

    while q:
        r, c, steps = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
                if nr in [0, m - 1] or nc in [0, n - 1]:
                    return steps + 1
                q.append((nr, nc, steps + 1))
                maze[nr][nc] = "+"

    return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
print(nearestExit(maze, entrance))  # 1

```

## 934. Shortest Bridge

-   [LeetCode](https://leetcode.com/problems/shortest-bridge/) | [LeetCode CH](https://leetcode.cn/problems/shortest-bridge/) (Medium)

-   Tags: array, depth first search, breadth first search, matrix
```python title="934. Shortest Bridge - Python Solution"
from collections import deque
from typing import List


# BFS + DFS; Coloring
def shortestBridge(grid: List[List[int]]) -> int:
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r, c, queue):
        grid[r][c] = 2
        queue.append((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(n) and nc in range(n) and grid[nr][nc] == 1:
                dfs(nr, nc, queue)

    q = deque()
    found = False
    for r in range(n):
        if found:
            break
        for c in range(n):
            if grid[r][c] == 1:
                dfs(r, c, q)
                found = True
                break

    steps = 0
    while q:
        m = len(q)
        for _ in range(m):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(n) and nc in range(n):
                    if grid[nr][nc] == 1:
                        return steps
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
        steps += 1

    return -1


grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
print(shortestBridge(grid))  # 1

```

## 433. Minimum Genetic Mutation

-   [LeetCode](https://leetcode.com/problems/minimum-genetic-mutation/) | [LeetCode CH](https://leetcode.cn/problems/minimum-genetic-mutation/) (Medium)

-   Tags: hash table, string, breadth first search
```python title="433. Minimum Genetic Mutation - Python Solution"
from collections import deque
from typing import List


# BFS
def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    if endGene not in bank:
        return -1

    bank = set(bank)
    q = deque([(startGene, 0)])

    while q:
        gene, step = q.popleft()
        if gene == endGene:
            return step

        for i in range(8):
            for c in "ACGT":
                if gene[i] == c:
                    continue
                newGene = gene[:i] + c + gene[i + 1 :]
                if newGene in bank:
                    bank.remove(newGene)
                    q.append((newGene, step + 1))
    return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(minMutation(startGene, endGene, bank))  # 2

```

## 127. Word Ladder

-   [LeetCode](https://leetcode.com/problems/word-ladder/) | [LeetCode CH](https://leetcode.cn/problems/word-ladder/) (Hard)

-   Tags: hash table, string, breadth first search
-   The most classic BFS problem.
-   Return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
-   Approach: BFS
-   Time Complexity: O(n * m^2)
-   Space Complexity: O(n * m)

```python title="127. Word Ladder - Python Solution"
from collections import defaultdict, deque
from typing import List


# BFS
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    n = len(beginWord)
    graph = defaultdict(list)  # pattern: words
    wordList.append(beginWord)

    for word in wordList:
        for i in range(n):
            pattern = word[:i] + "*" + word[i + 1 :]
            graph[pattern].append(word)

    visited = set([beginWord])
    q = deque([beginWord])
    res = 1

    while q:
        size = len(q)
        for _ in range(size):
            word = q.popleft()
            if word == endWord:
                return res

            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1 :]
                for neighbor in graph[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        res += 1

    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))  # 5

```

## 1306. Jump Game III

-   [LeetCode](https://leetcode.com/problems/jump-game-iii/) | [LeetCode CH](https://leetcode.cn/problems/jump-game-iii/) (Medium)

-   Tags: array, depth first search, breadth first search
```python title="1306. Jump Game III - Python Solution"
from collections import deque
from typing import List


# BFS
def canReach(arr: List[int], start: int) -> bool:
    n = len(arr)
    visited = [False for _ in range(n)]
    q = deque([start])

    while q:
        i = q.popleft()

        if arr[i] == 0:
            return True

        visited[i] = True

        for j in [i - arr[i], i + arr[i]]:
            if j in range(n) and not visited[j]:
                q.append(j)

    return False


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(canReach(arr, start))  # True

```

## 542. 01 Matrix

-   [LeetCode](https://leetcode.com/problems/01-matrix/) | [LeetCode CH](https://leetcode.cn/problems/01-matrix/) (Medium)

-   Tags: array, dynamic programming, breadth first search, matrix
```python title="542. 01 Matrix - Python Solution"
from collections import deque
from typing import List


# BFS
def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = [[float("inf")] * n for _ in range(m)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                q.append((i, j))

    while q:
        r, c = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] > dist[r][c] + 1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    return dist


mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(updateMatrix(mat))
# [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

```

## 1091. Shortest Path in Binary Matrix

-   [LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-in-binary-matrix/) (Medium)

-   Tags: array, breadth first search, matrix
```python title="1091. Shortest Path in Binary Matrix - Python Solution"
from collections import deque
from typing import List


# BFS
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    if n == 1:
        return 1

    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    q = deque([(0, 0, 1)])  # (row, column, distance)
    grid[0][0] = 1

    while q:
        r, c, d = q.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                if nr == nc == n - 1:
                    return d + 1
                q.append((nr, nc, d + 1))
                grid[nr][nc] = 1

    return -1


grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))  # 4

```

## 863. All Nodes Distance K in Binary Tree

-   [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [LeetCode CH](https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search, binary tree
```python title="863. All Nodes Distance K in Binary Tree - Python Solution"
from collections import deque
from typing import List

from binarytree import Node as TreeNode
from binarytree import build


# BFS
def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    parent = dict()

    def dfs(node, par=None):
        if node:
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)

    q = deque([(target, 0)])
    seen = set([target])

    while q:
        node, dist = q.popleft()

        if dist == k:
            return [node.val] + [node.val for node, _ in q]

        for nei in (node.left, node.right, parent[node]):
            if nei and nei not in seen:
                seen.add(nei)
                q.append((nei, dist + 1))

    return []


root = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(root)
#     ______3__
#    /         \
#   5__         1
#  /   \       / \
# 6     2     0   8
#      / \
#     7   4
target = root.left
k = 2
print(distanceK(root, target, k))  # [7, 4, 1]

```

## 864. Shortest Path to Get All Keys

-   [LeetCode](https://leetcode.com/problems/shortest-path-to-get-all-keys/) | [LeetCode CH](https://leetcode.cn/problems/shortest-path-to-get-all-keys/) (Hard)

-   Tags: array, bit manipulation, breadth first search, matrix
```python title="864. Shortest Path to Get All Keys - Python Solution"
from collections import deque
from typing import List


# BFS
def shortestPathAllKeys(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    visited = set()
    total = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for r in range(m):
        for c in range(n):
            if grid[r][c] == "@":
                q.append((r, c, 0, 0))
                visited.add((r, c, 0))
            if grid[r][c].islower():
                total += 1

    while q:
        r, c, keys, steps = q.popleft()

        if keys == (1 << total) - 1:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n:
                cell = grid[nr][nc]

                if cell == "#":
                    continue

                new_keys = keys
                if cell.islower():
                    new_keys |= 1 << (ord(cell) - ord("a"))

                if cell.isupper() and not (
                    keys & (1 << (ord(cell) - ord("A")))
                ):
                    continue

                if (nr, nc, new_keys) not in visited:
                    visited.add((nr, nc, new_keys))
                    q.append((nr, nc, new_keys, steps + 1))

    return -1


grid = ["@.a..", "###.#", "b.A.B"]
print(shortestPathAllKeys(grid))  # 8

```
