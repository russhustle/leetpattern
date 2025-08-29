---
comments: True
---

# Matrix

## Table of Contents

- [x] [73. Set Matrix Zeroes](https://leetcode.cn/problems/set-matrix-zeroes/) (Medium)
- [x] [54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/) (Medium)
- [x] [48. Rotate Image](https://leetcode.cn/problems/rotate-image/) (Medium)
- [x] [240. Search a 2D Matrix II](https://leetcode.cn/problems/search-a-2d-matrix-ii/) (Medium)

## 73. Set Matrix Zeroes

-   [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) | [LeetCode CH](https://leetcode.cn/problems/set-matrix-zeroes/) (Medium)

-   Tags: array, hash table, matrix
```python title="73. Set Matrix Zeroes - Python Solution"
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

```

## 54. Spiral Matrix

-   [LeetCode](https://leetcode.com/problems/spiral-matrix/) | [LeetCode CH](https://leetcode.cn/problems/spiral-matrix/) (Medium)

-   Tags: array, matrix, simulation
-   Return all elements of the matrix in spiral order.

```python title="54. Spiral Matrix - Python Solution"
from typing import List


# Array
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        if top <= bottom:

            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:

            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res


# Math
def spiralOrderMath(matrix: List[List[int]]) -> List[int]:
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Right Down Left Up
    m, n = len(matrix), len(matrix[0])
    size = m * n
    res = []
    i, j, di = 0, -1, 0

    while len(res) < size:
        dx, dy = dirs[di]
        for _ in range(n):
            i += dx
            j += dy
            res.append(matrix[i][j])
        di = (di + 1) % 4
        n, m = m - 1, n

    return res


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(spiralOrderMath([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

```

## 48. Rotate Image

-   [LeetCode](https://leetcode.com/problems/rotate-image/) | [LeetCode CH](https://leetcode.cn/problems/rotate-image/) (Medium)

-   Tags: array, math, matrix
```python title="48. Rotate Image - Python Solution"
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

```

## 240. Search a 2D Matrix II

-   [LeetCode](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [LeetCode CH](https://leetcode.cn/problems/search-a-2d-matrix-ii/) (Medium)

-   Tags: array, binary search, divide and conquer, matrix
```python title="240. Search a 2D Matrix II - Python Solution"
from typing import List


# Matrix
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n - 1

    while i < m and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            i += 1
        else:
            j -= 1

    return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]
target = 20
print(searchMatrix(matrix, target))  # False

```
