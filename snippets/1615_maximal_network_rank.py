from collections import defaultdict
from typing import List


# Graph
def maximalNetworkRank(n: int, roads: List[List[int]]) -> int:
    degree = defaultdict(int)
    roads_set = set(map(tuple, roads))

    for a, b in roads_set:
        degree[a] += 1
        degree[b] += 1

    rank = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (i, j) in roads_set or (j, i) in roads_set:
                rank = max(rank, degree[i] + degree[j] - 1)
            else:
                rank = max(rank, degree[i] + degree[j])

    return rank


n = 4
roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
print(maximalNetworkRank(n, roads))  # 4
