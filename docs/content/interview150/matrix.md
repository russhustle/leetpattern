---
comments: True
---

# Matrix

## Table of Contents

- [x] [36. Valid Sudoku](https://leetcode.cn/problems/valid-sudoku/) (Medium)
- [x] [54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/) (Medium)
- [x] [48. Rotate Image](https://leetcode.cn/problems/rotate-image/) (Medium)
- [x] [73. Set Matrix Zeroes](https://leetcode.cn/problems/set-matrix-zeroes/) (Medium)
- [x] [289. Game of Life](https://leetcode.cn/problems/game-of-life/) (Medium)

## 36. Valid Sudoku

-   [LeetCode](https://leetcode.com/problems/valid-sudoku/) | [LeetCode CH](https://leetcode.cn/problems/valid-sudoku/) (Medium)

-   Tags: array, hash table, matrix
```python title="36. Valid Sudoku - Python Solution"
from typing import List


# Set
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue

            if board[i][j] in rows[i]:
                return False
            rows[i].add(board[i][j])

            if board[i][j] in cols[j]:
                return False
            cols[j].add(board[i][j])

            box_index = (i // 3) * 3 + j // 3
            if board[i][j] in boxes[box_index]:
                return False
            boxes[box_index].add(board[i][j])

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))  # True

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

## 289. Game of Life

-   [LeetCode](https://leetcode.com/problems/game-of-life/) | [LeetCode CH](https://leetcode.cn/problems/game-of-life/) (Medium)

-   Tags: array, matrix, simulation
```python title="289. Game of Life - Python Solution"
from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    m, n = len(board), len(board[0])

    def count_live(r, c):
        cnt = 0
        for dr, dc in DIRS:
            nr, nc = dr + r, dc + c
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] & 1:
                cnt += 1
        return cnt

    # Encode next state: bit 1 = current, bit 2 = next
    for i in range(m):
        for j in range(n):
            cnt = count_live(i, j)
            if board[i][j] == 1:  # currently alive
                if 2 <= cnt <= 3:
                    board[i][j] = 3  # 11: was alive, stays alive
            else:  # currently dead
                if cnt == 3:
                    board[i][j] = 2  # 10: was dead, becomes alive

    # Extract next state
    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1


if __name__ == "__main__":
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    gameOfLife(board)
    assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

```
