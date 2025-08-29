---
comments: True
---

# Graph Union Find

## Table of Contents

- [x] [547. Number of Provinces](https://leetcode.cn/problems/number-of-provinces/) (Medium)
- [x] [684. Redundant Connection](https://leetcode.cn/problems/redundant-connection/) (Medium)
- [x] [323. Number of Connected Components in an Undirected Graph](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/) (Medium) 👑
- [x] [721. Accounts Merge](https://leetcode.cn/problems/accounts-merge/) (Medium)
- [x] [990. Satisfiability of Equality Equations](https://leetcode.cn/problems/satisfiability-of-equality-equations/) (Medium)
- [x] [952. Largest Component Size by Common Factor](https://leetcode.cn/problems/largest-component-size-by-common-factor/) (Hard)
- [x] [839. Similar String Groups](https://leetcode.cn/problems/similar-string-groups/) (Hard)
- [x] [305. Number of Islands II](https://leetcode.cn/problems/number-of-islands-ii/) (Hard) 👑
- [x] [1202. Smallest String With Swaps](https://leetcode.cn/problems/smallest-string-with-swaps/) (Medium)
- [x] [685. Redundant Connection II](https://leetcode.cn/problems/redundant-connection-ii/) (Hard)
- [x] [399. Evaluate Division](https://leetcode.cn/problems/evaluate-division/) (Medium)
- [x] [1101. The Earliest Moment When Everyone Become Friends](https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/) (Medium) 👑

## 547. Number of Provinces

-   [LeetCode](https://leetcode.com/problems/number-of-provinces/) | [LeetCode CH](https://leetcode.cn/problems/number-of-provinces/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
-   Return the number of provinces.

### Union Find

-   Find by Path Compression
-   Union by Rank
-   Time Complexity: O(log(n))
-   Space Complexity: O(n)

```python title="template/union_find.py"
--8<-- "template/union_find.py"
```

```python title="547. Number of Provinces - Python Solution"
from collections import defaultdict, deque
from typing import List

from template import UnionFind


# DFS (Adjacency Matrix)
def findCircleNumDFSMatrix(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in range(n):
            if node != neighbor and isConnected[node][neighbor] == 1:
                dfs(neighbor)

    res = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            res += 1

    return res


# DFS (Adjacency List)
def findCircleNumDFSList(isConnected: List[List[int]]) -> int:
    graph = defaultdict(list)
    n = len(isConnected)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    res = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            res += 1

    return res


# BFS (Adjacency Matrix)
def findCircleNumBFS(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()
    q = deque()
    res = 0

    for i in range(n):
        if i not in visited:
            res += 1

            q.append(i)
            while q:
                node = q.popleft()
                visited.add(node)
                for node, val in enumerate(isConnected[node]):
                    if val == 1 and node not in visited:
                        q.append(node)
                        visited.add(node)

    return res


# Union Find
def findCircleNumUF(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    uf = UnionFind(n)

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)

    res = len(set(uf.find(i) for i in range(n)))

    return res


# Union Find
def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    par = {i: i for i in range(n)}
    rank = {i: 0 for i in range(n)}

    def find(n):
        p = par[n]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return None

        if rank[p1] > rank[p2]:
            par[p2] = p1
        elif rank[p1] < rank[p2]:
            par[p1] = p2
        else:
            par[p2] = p1
            rank[p1] += 1

    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                union(i, j)

    res = len(set(find(i) for i in range(n)))

    return res


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(findCircleNumDFSList(isConnected))  # 2
print(findCircleNumDFSMatrix(isConnected))  # 2
print(findCircleNumBFS(isConnected))  # 2
print(findCircleNum(isConnected))  # 2
print(findCircleNumUF(isConnected))  # 2

```

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

## 323. Number of Connected Components in an Undirected Graph

-   [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [LeetCode CH](https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/) (Medium)

-   Tags: depth first search, breadth first search, union find, graph
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

## 721. Accounts Merge

-   [LeetCode](https://leetcode.com/problems/accounts-merge/) | [LeetCode CH](https://leetcode.cn/problems/accounts-merge/) (Medium)

-   Tags: array, hash table, string, depth first search, breadth first search, union find, sorting
```python title="721. Accounts Merge - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    parent = defaultdict(str)
    rank = defaultdict(int)
    email_to_name = defaultdict(str)
    merged_accounts = defaultdict(list)

    def find(n):
        p = parent[n]
        while p != parent[p]:
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

    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            if email not in parent:
                parent[email] = email
                rank[email] = 1
            email_to_name[email] = name
            union(first_email, email)

    for email in parent:
        root_email = find(email)
        merged_accounts[root_email].append(email)

    result = []
    for root_email, emails in merged_accounts.items():
        result.append([email_to_name[root_email]] + sorted(emails))

    return result


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
print(accountsMerge(accounts))
# [['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ['Mary', 'mary@mail.com'],
# ['John', 'johnnybravo@mail.com']]

```

## 990. Satisfiability of Equality Equations

-   [LeetCode](https://leetcode.com/problems/satisfiability-of-equality-equations/) | [LeetCode CH](https://leetcode.cn/problems/satisfiability-of-equality-equations/) (Medium)

-   Tags: array, string, union find, graph
```python title="990. Satisfiability of Equality Equations - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def equationsPossible(equations: List[str]) -> bool:
    parent = defaultdict(str)
    rank = defaultdict(int)

    def find(n):
        p = parent[n]
        while p != parent[p]:
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

    for equation in equations:
        if equation[0] not in parent:
            parent[equation[0]] = equation[0]
            rank[equation[0]] = 1
        if equation[3] not in parent:
            parent[equation[3]] = equation[3]
            rank[equation[3]] = 1

    for equation in equations:
        if equation[1] == "=":
            union(equation[0], equation[3])

    for equation in equations:
        if equation[1] == "!":
            if find(equation[0]) == find(equation[3]):
                return False

    return True


equations = ["a==b", "b!=a"]
print(equationsPossible(equations))  # False

```

## 952. Largest Component Size by Common Factor

-   [LeetCode](https://leetcode.com/problems/largest-component-size-by-common-factor/) | [LeetCode CH](https://leetcode.cn/problems/largest-component-size-by-common-factor/) (Hard)

-   Tags: array, hash table, math, union find, number theory
```python title="952. Largest Component Size by Common Factor - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def largestComponentSize(nums: List[int]) -> int:
    par = {i: i for i in nums}
    rank = {i: 0 for i in nums}

    def find(n):
        p = par[n]
        while par[p] != p:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 != p2:
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1

    def prime_factors(n):
        """Return the prime factors of n."""
        i = 2
        factors = set()
        while i * i <= n:
            while (n % i) == 0:
                factors.add(i)
                n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors

    factor_map = defaultdict(list)  # factor -> [nums]
    for num in nums:
        factors = prime_factors(num)
        for factor in factors:
            factor_map[factor].append(num)

    for factor, group in factor_map.items():
        for i in range(1, len(group)):
            union(group[0], group[i])

    sizes = defaultdict(int)  # component root -> size
    for num in nums:
        root = find(num)
        sizes[root] += 1

    return max(sizes.values())


nums = [20, 50, 9, 63]
print(largestComponentSize(nums))  # 2

```

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

## 305. Number of Islands II

-   [LeetCode](https://leetcode.com/problems/number-of-islands-ii/) | [LeetCode CH](https://leetcode.cn/problems/number-of-islands-ii/) (Hard)

-   Tags: array, hash table, union find
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

## 399. Evaluate Division

-   [LeetCode](https://leetcode.com/problems/evaluate-division/) | [LeetCode CH](https://leetcode.cn/problems/evaluate-division/) (Medium)

-   Tags: array, string, depth first search, breadth first search, union find, graph, shortest path
```python title="399. Evaluate Division - Python Solution"
from collections import defaultdict
from typing import List


# Union Find
def calcEquation(
    equations: List[List[str]], values: List[float], queries: List[List[str]]
) -> List[float]:
    graph = defaultdict(dict)
    for (a, b), v in zip(equations, values):
        graph[a][b] = v
        graph[b][a] = 1 / v

    def dfs(a, b, visited):
        if a not in graph or b not in graph:
            return -1.0

        if b in graph[a]:
            return graph[a][b]

        for c in graph[a]:
            if c not in visited:
                visited.add(c)
                d = dfs(c, b, visited)
                if d != -1.0:
                    return graph[a][c] * d
        return -1.0

    result = []
    for a, b in queries:
        result.append(dfs(a, b, set()))

    return result


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(calcEquation(equations, values, queries))  # [6.0, 0.5, -1.0, 1.0, -1.0]

```

## 1101. The Earliest Moment When Everyone Become Friends

-   [LeetCode](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) | [LeetCode CH](https://leetcode.cn/problems/the-earliest-moment-when-everyone-become-friends/) (Medium)

-   Tags: array, union find, sorting
```python title="1101. The Earliest Moment When Everyone Become Friends - Python Solution"
from typing import List


# Union Find
def earliestAcq(logs: List[List[int]], n: int) -> int:
    logs.sort()
    par = {i: i for i in range(n)}

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    for time, a, b in logs:
        pa, pb = find(a), find(b)
        if pa != pb:
            par[pa] = pb
            n -= 1
        if n == 1:
            return time
    return -1


logs = [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]
n = 4
print(earliestAcq(logs, n))  # 3

```

