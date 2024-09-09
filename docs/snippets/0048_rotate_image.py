from copy import deepcopy
from typing import List


# Math
def rotate1(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp


def rotate2(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
matrix1 = deepcopy(matrix)
rotate1(matrix1)
print(matrix1)
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
matrix2 = deepcopy(matrix)
rotate2(matrix2)
print(matrix2)
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
