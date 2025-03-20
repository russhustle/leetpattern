---
comments: True
---

# General Tree Top-Down DFS

## Table of Contents

- [x] [1376. Time Needed to Inform All Employees](https://leetcode.cn/problems/time-needed-to-inform-all-employees/) (Medium)
- [ ] [1443. Minimum Time to Collect All Apples in a Tree](https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/) (Medium)
- [ ] [1377. Frog Position After T Seconds](https://leetcode.cn/problems/frog-position-after-t-seconds/) (Hard)
- [ ] [3067. Count Pairs of Connectable Servers in a Weighted Tree Network](https://leetcode.cn/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) (Medium)
- [ ] [3372. Maximize the Number of Target Nodes After Connecting Trees I](https://leetcode.cn/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/) (Medium)
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
