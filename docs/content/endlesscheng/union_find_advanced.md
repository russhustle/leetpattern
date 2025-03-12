---
comments: True
---

# Union Find Advanced

- [x] [1202. Smallest String With Swaps](https://leetcode.cn/problems/smallest-string-with-swaps/) (Medium)
- [x] [1061. Lexicographically Smallest Equivalent String](https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/) (Medium)
- [ ] [1722. Minimize Hamming Distance After Swap Operations](https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/) (Medium)
- [ ] [765. Couples Holding Hands](https://leetcode.cn/problems/couples-holding-hands/) (Hard)
- [x] [684. Redundant Connection](https://leetcode.cn/problems/redundant-connection/) (Medium)
- [x] [685. Redundant Connection II](https://leetcode.cn/problems/redundant-connection-ii/) (Hard)
- [ ] [947. Most Stones Removed with Same Row or Column](https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/) (Medium)
- [x] [839. Similar String Groups](https://leetcode.cn/problems/similar-string-groups/) (Hard)
- [ ] [1970. Last Day Where You Can Still Cross](https://leetcode.cn/problems/last-day-where-you-can-still-cross/) (Hard)
- [ ] [2076. Process Restricted Friend Requests](https://leetcode.cn/problems/process-restricted-friend-requests/) (Hard)
- [x] [1579. Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.cn/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) (Hard)
- [ ] [959. Regions Cut By Slashes](https://leetcode.cn/problems/regions-cut-by-slashes/) (Medium)
- [ ] [2812. Find the Safest Path in a Grid](https://leetcode.cn/problems/find-the-safest-path-in-a-grid/) (Medium)
- [ ] [2503. Maximum Number of Points From Grid Queries](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) (Hard)
- [ ] [2867. Count Valid Paths in a Tree](https://leetcode.cn/problems/count-valid-paths-in-a-tree/) (Hard)
- [ ] [2421. Number of Good Paths](https://leetcode.cn/problems/number-of-good-paths/) (Hard)
- [ ] [2157. Groups of Strings](https://leetcode.cn/problems/groups-of-strings/) (Hard)
- [ ] [1632. Rank Transform of a Matrix](https://leetcode.cn/problems/rank-transform-of-a-matrix/) (Hard)
- [ ] [803. Bricks Falling When Hit](https://leetcode.cn/problems/bricks-falling-when-hit/) (Hard)
- [ ] [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/) (Hard)
- [ ] [3235. Check if the Rectangle Corner Is Reachable](https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/) (Hard)
- [ ] [2371. Minimize Maximum Value in a Grid](https://leetcode.cn/problems/minimize-maximum-value-in-a-grid/) (Hard) 👑
- [ ] [2459. Sort Array by Moving Items to Empty Space](https://leetcode.cn/problems/sort-array-by-moving-items-to-empty-space/) (Hard) 👑

## 1202. Smallest String With Swaps

-   [LeetCode](https://leetcode.com/problems/smallest-string-with-swaps/) | [LeetCode CH](https://leetcode.cn/problems/smallest-string-with-swaps/) (Medium)

-   Tags: array, hash table, string, depth first search, breadth first search, union find, sorting

```python title="1202. Smallest String With Swaps - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    n = len(s)
    par = list(range(n))
    components = defaultdict(list)

    def find(node):
        p = par[node]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 != p2:
            par[p1] = p2

    for index, j in pairs:
        union(index, j)

    for index in range(n):
        components[find(index)].append(index)

    res = list(s)
    for indices in components.values():
        chars = sorted([s[index] for index in indices])
        for index, char in zip(indices, chars):
            res[index] = char

    return "".join(res)


s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs))  # "bacd"

```

## 1061. Lexicographically Smallest Equivalent String

-   [LeetCode](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) | [LeetCode CH](https://leetcode.cn/problems/lexicographically-smallest-equivalent-string/) (Medium)

-   Tags: string, union find

```python title="1061. Lexicographically Smallest Equivalent String - Python Solution"
# Union Find
def smallestEquivalentString(s1: str, s2: str, baseStr: str) -> str:
    parent = {chr(i): chr(i) for i in range(ord("a"), ord("z") + 1)}

    def find(n):
        p = parent[n]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2

    for i in range(len(s1)):
        union(s1[i], s2[i])

    result = []
    for c in baseStr:
        result.append(find(c))

    return "".join(result)


s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(smallestEquivalentString(s1, s2, baseStr))  # "makkek"

```

## 1722. Minimize Hamming Distance After Swap Operations

-   [LeetCode](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) | [LeetCode CH](https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/) (Medium)

-   Tags: array, depth first search, union find

## 765. Couples Holding Hands

-   [LeetCode](https://leetcode.com/problems/couples-holding-hands/) | [LeetCode CH](https://leetcode.cn/problems/couples-holding-hands/) (Hard)

-   Tags: greedy, depth first search, breadth first search, union find, graph

## 684. Redundant Connection

-   [LeetCode](https://leetcode.com/problems/redundant-connection/) | [LeetCode CH](https://leetcode.cn/problems/redundant-connection/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph

```python title="684. Redundant Connection - Python Solution"
from typing import List


class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}
        self.rank = {i: 1 for i in range(1, n + 1)}

    def find(self, n):
        p = self.par[n]
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True


# Union Find
def findRedundantConnectionUF(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n)

    for u, v in edges:
        if not uf.union(u, v):
            return (u, v)


# DFS
def findRedundantConnectionDFS(edges: List[List[int]]) -> List[int]:
    graph, cycle = {}, {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

    def dfs(node, parent):
        if node in cycle:
            for k in list(cycle.keys()):
                if k == node:
                    return True
                del cycle[k]

        cycle[node] = None
        for child in graph[node]:
            if child != parent and dfs(child, node):
                return True
        del cycle[node]
        return False

    dfs(edges[0][0], -1)
    for a, b in edges[::-1]:
        if a in cycle and b in cycle:
            return (a, b)


edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantConnectionUF(edges))  # (2, 3)
print(findRedundantConnectionDFS(edges))  # (2, 3)

```

## 685. Redundant Connection II

-   [LeetCode](https://leetcode.com/problems/redundant-connection-ii/) | [LeetCode CH](https://leetcode.cn/problems/redundant-connection-ii/) (Hard)

-   Tags: depth first search, breadth first search, union find, graph

```python title="685. Redundant Connection II - Python Solution"
from typing import List


# Union Find
def findRedundantDirectedConnectionUF(edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n + 1)
    parent = list(range(n + 1))
    candidates = []

    for u, v in edges:
        if parent[v] != v:
            candidates.append([parent[v], v])
            candidates.append([u, v])
        else:
            parent[v] = u

    if not candidates:
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]

    for u, v in edges:
        if [u, v] == candidates[1]:
            continue
        if not uf.union(u, v):
            return candidates[0]

    return candidates[1]


class UnionFind:
    def __init__(self, n):
        self.par = {i: i for i in range(1, n + 1)}

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        self.par[p1] = p2
        return True


edges = [[1, 2], [1, 3], [2, 3]]
print(findRedundantDirectedConnectionUF(edges))

```

## 947. Most Stones Removed with Same Row or Column

-   [LeetCode](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | [LeetCode CH](https://leetcode.cn/problems/most-stones-removed-with-same-row-or-column/) (Medium)

-   Tags: hash table, depth first search, union find, graph

## 839. Similar String Groups

-   [LeetCode](https://leetcode.com/problems/similar-string-groups/) | [LeetCode CH](https://leetcode.cn/problems/similar-string-groups/) (Hard)

-   Tags: array, hash table, string, depth first search, breadth first search, union find

```python title="839. Similar String Groups - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def numSimilarGroups(strs: List[str]) -> int:
    n = len(strs)
    parent = list(range(n))
    rank = [0 for _ in range(n)]

    def find(n):
        p = parent[n]
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return
        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p1] < rank[p2]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            rank[p1] += 1

    def is_similar(s1, s2):
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 2:
                return False
        return True

    for i in range(n):
        for j in range(i + 1, n):
            if is_similar(strs[i], strs[j]):
                union(i, j)

    return sum(find(i) == i for i in range(n))


strs = ["tars", "rats", "arts", "star"]
print(numSimilarGroups(strs))  # 2

```

## 1970. Last Day Where You Can Still Cross

-   [LeetCode](https://leetcode.com/problems/last-day-where-you-can-still-cross/) | [LeetCode CH](https://leetcode.cn/problems/last-day-where-you-can-still-cross/) (Hard)

-   Tags: array, binary search, depth first search, breadth first search, union find, matrix

## 2076. Process Restricted Friend Requests

-   [LeetCode](https://leetcode.com/problems/process-restricted-friend-requests/) | [LeetCode CH](https://leetcode.cn/problems/process-restricted-friend-requests/) (Hard)

-   Tags: union find, graph

## 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

-   [LeetCode](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) | [LeetCode CH](https://leetcode.cn/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) (Hard)

-   Tags: union find, graph
- Return the maximum number of edges you can remove so that the graph remains fully traversable.

![1579](../../assets/1579.png){width=200px}

```python title="1579. Remove Max Number of Edges to Keep Graph Fully Traversable - Python Solution"
from typing import List


# Kruskal
def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    alice, bob = UnionFind(n), UnionFind(n)
    visited = 0

    for t, u, v in edges:
        if t == 3:
            if alice.union(u, v) | bob.union(u, v):
                visited += 1

    for t, u, v in edges:
        if t == 1:
            if alice.union(u, v):
                visited += 1
        elif t == 2:
            if bob.union(u, v):
                visited += 1

    if alice.components > 1 or bob.components > 1:
        return -1

    return len(edges) - visited


class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n + 1)}
        self.rank = {i: 0 for i in range(1, n + 1)}
        self.components = n

    def find(self, n):
        p = self.parent[n]
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        self.components -= 1

        return True


n = 4
edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
print(maxNumEdgesToRemove(n, edges))  # 2

```

## 959. Regions Cut By Slashes

-   [LeetCode](https://leetcode.com/problems/regions-cut-by-slashes/) | [LeetCode CH](https://leetcode.cn/problems/regions-cut-by-slashes/) (Medium)

-   Tags: array, hash table, depth first search, breadth first search, union find, matrix

## 2812. Find the Safest Path in a Grid

-   [LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/find-the-safest-path-in-a-grid/) (Medium)

-   Tags: array, binary search, breadth first search, union find, heap priority queue, matrix

## 2503. Maximum Number of Points From Grid Queries

-   [LeetCode](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) | [LeetCode CH](https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/) (Hard)

-   Tags: array, two pointers, breadth first search, union find, sorting, heap priority queue, matrix

## 2867. Count Valid Paths in a Tree

-   [LeetCode](https://leetcode.com/problems/count-valid-paths-in-a-tree/) | [LeetCode CH](https://leetcode.cn/problems/count-valid-paths-in-a-tree/) (Hard)

-   Tags: math, dynamic programming, tree, depth first search, number theory

## 2421. Number of Good Paths

-   [LeetCode](https://leetcode.com/problems/number-of-good-paths/) | [LeetCode CH](https://leetcode.cn/problems/number-of-good-paths/) (Hard)

-   Tags: array, hash table, tree, union find, graph, sorting

## 2157. Groups of Strings

-   [LeetCode](https://leetcode.com/problems/groups-of-strings/) | [LeetCode CH](https://leetcode.cn/problems/groups-of-strings/) (Hard)

-   Tags: string, bit manipulation, union find

## 1632. Rank Transform of a Matrix

-   [LeetCode](https://leetcode.com/problems/rank-transform-of-a-matrix/) | [LeetCode CH](https://leetcode.cn/problems/rank-transform-of-a-matrix/) (Hard)

-   Tags: array, union find, graph, topological sort, sorting, matrix

## 803. Bricks Falling When Hit

-   [LeetCode](https://leetcode.com/problems/bricks-falling-when-hit/) | [LeetCode CH](https://leetcode.cn/problems/bricks-falling-when-hit/) (Hard)

-   Tags: array, union find, matrix

## 1569. Number of Ways to Reorder Array to Get Same BST

-   [LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) | [LeetCode CH](https://leetcode.cn/problems/number-of-ways-to-reorder-array-to-get-same-bst/) (Hard)

-   Tags: array, math, divide and conquer, dynamic programming, tree, union find, binary search tree, memoization, combinatorics, binary tree

## 3235. Check if the Rectangle Corner Is Reachable

-   [LeetCode](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/) | [LeetCode CH](https://leetcode.cn/problems/check-if-the-rectangle-corner-is-reachable/) (Hard)

-   Tags: array, math, depth first search, breadth first search, union find, geometry

## 2371. Minimize Maximum Value in a Grid

-   [LeetCode](https://leetcode.com/problems/minimize-maximum-value-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/minimize-maximum-value-in-a-grid/) (Hard)

-   Tags: array, union find, graph, topological sort, sorting, matrix

## 2459. Sort Array by Moving Items to Empty Space

-   [LeetCode](https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/) | [LeetCode CH](https://leetcode.cn/problems/sort-array-by-moving-items-to-empty-space/) (Hard)

-   Tags: array, greedy, sorting
