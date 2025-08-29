---
comments: True
---

# Topological Order DP

## Table of Contents

- [ ] [2050. Parallel Courses III](https://leetcode.cn/problems/parallel-courses-iii/) (Hard)
- [x] [1857. Largest Color Value in a Directed Graph](https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/) (Hard)

## 2050. Parallel Courses III

-   [LeetCode](https://leetcode.com/problems/parallel-courses-iii/) | [LeetCode CH](https://leetcode.cn/problems/parallel-courses-iii/) (Hard)

-   Tags: array, dynamic programming, graph, topological sort
## 1857. Largest Color Value in a Directed Graph

-   [LeetCode](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/) | [LeetCode CH](https://leetcode.cn/problems/largest-color-value-in-a-directed-graph/) (Hard)

-   Tags: hash table, dynamic programming, graph, topological sort, memoization, counting
```python title="1857. Largest Color Value in a Directed Graph - Python Solution"
from collections import defaultdict, deque
from typing import List


# Topological Sort
def largestPathValue(colors: str, edges: List[List[int]]) -> int:
    n = len(colors)
    graph = defaultdict(list)
    indegree = [0 for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque([i for i in range(n) if indegree[i] == 0])

    dp = [[0] * 26 for _ in range(n)]

    for i in range(n):
        dp[i][ord(colors[i]) - ord("a")] = 1

    processed, max_color = 0, 0

    while q:
        n1 = q.popleft()
        processed += 1
        max_color = max(max_color, max(dp[n1]))

        for n2 in graph[n1]:
            indegree[n2] -= 1
            for i in range(26):
                dp[n2][i] = max(
                    dp[n2][i],
                    dp[n1][i] + (1 if i == ord(colors[n2]) - ord("a") else 0),
                )
            if indegree[n2] == 0:
                q.append(n2)

    return max_color if processed == n else -1


colors = "abaca"
edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
print(largestPathValue(colors, edges))  # 3

```

