"""
-   Return a square matrix filled with elements from 1 to n^2 in spiral order.
"""

from pprint import pprint
from typing import List


# Array
def generateMatrix(n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    num = 1

    for layer in range((n + 1) // 2):
        for i in range(layer, n - layer):
            matrix[layer][i] = num
            num += 1
        for j in range(layer + 1, n - layer):
            matrix[j][n - 1 - layer] = num
            num += 1
        for i in range(n - 2 - layer, layer - 1, -1):
            matrix[n - 1 - layer][i] = num
            num += 1
        for j in range(n - 2 - layer, layer, -1):
            matrix[j][layer] = num
            num += 1

    return matrix


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |   Layer     |      O(N^2)     |     O(1)     |
# |-------------|-----------------|--------------|


pprint(generateMatrix(5))
# [[ 1,  2,  3,  4, 5],
#  [16, 17, 18, 19, 6],
#  [15, 24, 25, 20, 7],
#  [14, 23, 22, 21, 8],
#  [13, 12, 11, 10, 9]]
