from typing import List


# Graph
def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    indegree = {i: 0 for i in range(n)}

    for a, b in edges:
        indegree[b] += 1

    return [i for i in range(n) if indegree[i] == 0]


n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
print(findSmallestSetOfVertices(n, edges))  # [0, 3]
