---
comments: True
---

# General Tree Top-Down DFS

## Table of Contents

- [x] [1376. Time Needed to Inform All Employees](https://leetcode.cn/problems/time-needed-to-inform-all-employees/) (Medium)
- [ ] [1443. Minimum Time to Collect All Apples in a Tree](https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/) (Medium)
- [ ] [1377. Frog Position After T Seconds](https://leetcode.cn/problems/frog-position-after-t-seconds/) (Hard)
- [ ] [3067. Count Pairs of Connectable Servers in a Weighted Tree Network](https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) (Medium)
- [x] [3372. Maximize the Number of Target Nodes After Connecting Trees I](https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/) (Medium)
- [ ] [2467. Most Profitable Path in a Tree](https://leetcode.cn/problems/most-profitable-path-in-a-tree/) (Medium)
- [ ] [3373. Maximize the Number of Target Nodes After Connecting Trees II](https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/) (Hard)
- [ ] [1766. Tree of Coprimes](https://leetcode.cn/problems/tree-of-coprimes/) (Hard)
- [ ] [3425. Longest Special Path](https://leetcode.cn/problems/longest-special-path/) (Hard)
- [ ] [2791. Count Paths That Can Form a Palindrome in a Tree](https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) (Hard)

## 1376. Time Needed to Inform All Employees

-   [LeetCode](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [LeetCode CH](https://leetcode.cn/problems/time-needed-to-inform-all-employees/) (Medium)

-   Tags: tree, depth first search, breadth first search
```python title="1376. Time Needed to Inform All Employees - Python Solution"
from collections import defaultdict, deque
from typing import List


# DFS
def numOfMinutesDFS(
    n: int, headID: int, manager: List[int], informTime: List[int]
) -> int:
    graph = defaultdict(list)
    for i in range(n):
        if manager[i] != -1:
            graph[manager[i]].append(i)

    def dfs(node):
        time = 0
        for sub in graph[node]:
            time = max(time, dfs(sub))
        return time + informTime[node]

    return dfs(headID)


# BFS
def numOfMinutesBFS(
    n: int, headID: int, manager: List[int], informTime: List[int]
) -> int:
    graph = defaultdict(list)
    for i in range(n):
        if manager[i] != -1:
            graph[manager[i]].append(i)

    q = deque([(headID, 0)])
    max_time = 0

    while q:
        node, time = q.popleft()
        max_time = max(max_time, time)
        for sub in graph[node]:
            q.append((sub, time + informTime[node]))

    return max_time


n = 6
headID = 2
manager = [2, 2, -1, 2, 2, 2]
informTime = [0, 0, 1, 0, 0, 0]
print(numOfMinutesDFS(n, headID, manager, informTime))  # 1
print(numOfMinutesBFS(n, headID, manager, informTime))  # 1

```

## 1443. Minimum Time to Collect All Apples in a Tree

-   [LeetCode](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/) (Medium)

-   Tags: hash table, tree, depth first search, breadth first search
## 1377. Frog Position After T Seconds

-   [LeetCode](https://leetcode.com/problems/frog-position-after-t-seconds/) | [LeetCode CH](https://leetcode.cn/problems/frog-position-after-t-seconds/) (Hard)

-   Tags: tree, depth first search, breadth first search, graph
## 3067. Count Pairs of Connectable Servers in a Weighted Tree Network

-   [LeetCode](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) | [LeetCode CH](https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) (Medium)

-   Tags: array, tree, depth first search
## 3372. Maximize the Number of Target Nodes After Connecting Trees I

-   [LeetCode](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/) | [LeetCode CH](https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/) (Medium)

-   Tags: tree, depth first search, breadth first search
```python title="3372. Maximize the Number of Target Nodes After Connecting Trees I - Python Solution"
from typing import Callable, List, Tuple


def maxTargetNodes(
    edges1: List[List[int]], edges2: List[List[int]], k: int
) -> List[int]:
    n = len(edges1) + 1
    m = len(edges2) + 1

    def calc_tree(
        edges: List[List[int]], k: int
    ) -> Tuple[int, Callable[[int, int, int], int]]:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        diameter = 0

        def dfs_diameter(x: int, fa: int) -> int:
            nonlocal diameter
            max_len = 0
            for y in g[x]:
                if y != fa:
                    sub_len = dfs_diameter(y, x) + 1
                    diameter = max(diameter, max_len + sub_len)
                    max_len = max(max_len, sub_len)
            return max_len

        dfs_diameter(0, -1)

        def dfs(x: int, fa: int, d: int) -> int:
            if d > k:
                return 0
            cnt = 1
            for y in g[x]:
                if y != fa:
                    cnt += dfs(y, x, d + 1)
            return cnt

        return diameter, dfs

    max2 = 0
    if k:
        diameter, dfs = calc_tree(edges2, k - 1)
        if diameter < k:
            max2 = m  # All nodes in the second tree are target nodes
        else:
            max2 = max(dfs(i, -1, 0) for i in range(m))

    diameter, dfs = calc_tree(edges1, k)
    if diameter <= k:
        return [n + max2] * n  # All nodes in the first tree are target nodes
    return [dfs(i, -1, 0) + max2 for i in range(n)]

```

## 2467. Most Profitable Path in a Tree

-   [LeetCode](https://leetcode.com/problems/most-profitable-path-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/most-profitable-path-in-a-tree/) (Medium)

-   Tags: array, tree, depth first search, breadth first search, graph
## 3373. Maximize the Number of Target Nodes After Connecting Trees II

-   [LeetCode](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/) (Hard)

-   Tags: tree, depth first search, breadth first search
## 1766. Tree of Coprimes

-   [LeetCode](https://leetcode.com/problems/tree-of-coprimes/) | [LeetCode CH](https://leetcode.cn/problems/tree-of-coprimes/) (Hard)

-   Tags: array, math, tree, depth first search, number theory
## 3425. Longest Special Path

-   [LeetCode](https://leetcode.com/problems/longest-special-path/) | [LeetCode CH](https://leetcode.cn/problems/longest-special-path/) (Hard)

-   Tags: array, hash table, tree, depth first search, sliding window
## 2791. Count Paths That Can Form a Palindrome in a Tree

-   [LeetCode](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) (Hard)

-   Tags: dynamic programming, bit manipulation, tree, depth first search, bitmask
