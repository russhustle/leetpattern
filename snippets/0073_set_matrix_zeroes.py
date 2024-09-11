from copy import deepcopy
from typing import List


# Math
def setZeroes1(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])

    rows, cols = set(), set()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for i in rows:
        for j in range(n):
            matrix[i][j] = 0

    for i in range(m):
        for j in cols:
            matrix[i][j] = 0


# Math - Optimized
def setZeroes2(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    row_zero, col_zero = False, False

    for i in range(m):
        if matrix[i][0] == 0:
            col_zero = True
            break

    for j in range(n):
        if matrix[0][j] == 0:
            row_zero = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    if col_zero:
        for i in range(m):
            matrix[i][0] = 0

    if row_zero:
        for j in range(n):
            matrix[0][j] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(matrix)
# [[1, 1, 1],
#  [1, 0, 1],
#  [1, 1, 1]]
matrix1 = deepcopy(matrix)
setZeroes1(matrix1)
print(matrix1)
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]
matrix2 = deepcopy(matrix)
setZeroes2(matrix2)
print(matrix2)
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]
