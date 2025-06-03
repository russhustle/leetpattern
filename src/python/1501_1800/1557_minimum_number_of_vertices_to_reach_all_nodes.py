"""
- Return a list of integers representing the minimum number of vertices needed to traverse all the nodes.
- Hint: Return the vertices with indegree 0.
"""

from typing import List


# Graph
def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    indegree = {i: 0 for i in range(n)}

    for _, end in edges:
        indegree[end] += 1

    return [i for i in range(n) if indegree[i] == 0]


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    assert findSmallestSetOfVertices(n, edges) == [0, 3]
