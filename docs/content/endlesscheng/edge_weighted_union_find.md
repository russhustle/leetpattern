---
comments: True
---

# Edge Weighted Union Find

## Table of Contents

- [x] [399. Evaluate Division](https://leetcode.cn/problems/evaluate-division/) (Medium)
- [ ] [2307. Check for Contradictions in Equations](https://leetcode.cn/problems/check-for-contradictions-in-equations/) (Hard) 👑

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

## 2307. Check for Contradictions in Equations

-   [LeetCode](https://leetcode.com/problems/check-for-contradictions-in-equations/) | [LeetCode CH](https://leetcode.cn/problems/check-for-contradictions-in-equations/) (Hard)

-   Tags: array, depth first search, union find, graph
