"""
-   `trust = [[1, 3], [2, 3], [1, 2], [4, 3]]`
"""

from typing import List


# Graph
def findJudge(n: int, trust: List[List[int]]) -> int:
    indegree = {i: 0 for i in range(1, n + 1)}
    outdegree = {i: 0 for i in range(1, n + 1)}

    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1

    for i in range(1, n + 1):
        if indegree[i] == n - 1 and outdegree[i] == 0:
            return i

    return -1


n = 4
trust = [[1, 3], [2, 3], [1, 2], [4, 3]]
print(findJudge(n, trust))  # 4
