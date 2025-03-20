---
comments: True
---

# Math Geometry

## Table of Contents

- [x] [48. Rotate Image](https://leetcode.cn/problems/rotate-image/) (Medium)
- [x] [54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/) (Medium)
- [x] [73. Set Matrix Zeroes](https://leetcode.cn/problems/set-matrix-zeroes/) (Medium)
- [x] [202. Happy Number](https://leetcode.cn/problems/happy-number/) (Easy)
- [x] [66. Plus One](https://leetcode.cn/problems/plus-one/) (Easy)
- [x] [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/) (Medium)
- [x] [43. Multiply Strings](https://leetcode.cn/problems/multiply-strings/) (Medium)
- [x] [166. Fraction to Recurring Decimal](https://leetcode.cn/problems/fraction-to-recurring-decimal/) (Medium)

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

## 202. Happy Number

-   [LeetCode](https://leetcode.com/problems/happy-number/) | [LeetCode CH](https://leetcode.cn/problems/happy-number/) (Easy)

-   Tags: hash table, math, two pointers
-   Return `True` if the number is a happy number, otherwise, return `False`.
-   A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

```python title="202. Happy Number - Python Solution"
def isHappy(n: int) -> bool:

    def getSum(n):
        sum_of_squares = 0
        while n:
            a, b = divmod(n, 10)
            sum_of_squares += b**2
            n = a
        return sum_of_squares

    record = set()

    while True:
        if n == 1:
            return True

        if n in record:
            return False
        else:
            record.add(n)

        n = getSum(n)


n = 19
print(isHappy(n))  # True

```

## 66. Plus One

-   [LeetCode](https://leetcode.com/problems/plus-one/) | [LeetCode CH](https://leetcode.cn/problems/plus-one/) (Easy)

-   Tags: array, math

```python title="66. Plus One - Python Solution"
from typing import List


# Math
def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits


digits = [4, 3, 2, 1]
print(plusOne(digits))  # [4, 3, 2, 2]

```

## 50. Pow(x, n)

-   [LeetCode](https://leetcode.com/problems/powx-n/) | [LeetCode CH](https://leetcode.cn/problems/powx-n/) (Medium)

-   Tags: math, recursion

```python title="50. Pow(x, n) - Python Solution"
# Iterative
def myPowIterative(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    cur = x

    while n > 0:
        if n % 2 == 1:
            result *= cur

        cur *= cur
        n //= 2

    return result


# Recursive
def myPowRecursive(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    if n % 2 == 0:
        return myPowRecursive(x * x, n // 2)
    else:
        return x * myPowRecursive(x * x, n // 2)


x = 2.00000
n = 10
print(myPowIterative(x, n))  # 1024.0
print(myPowRecursive(x, n))  # 1024.0

```

## 43. Multiply Strings

-   [LeetCode](https://leetcode.com/problems/multiply-strings/) | [LeetCode CH](https://leetcode.cn/problems/multiply-strings/) (Medium)

-   Tags: math, string, simulation

```python title="43. Multiply Strings - Python Solution"
# Math
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0 for _ in range(m + n)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum = mul + result[i + j + 1]

            result[i + j + 1] = sum % 10
            result[i + j] += sum // 10

    result_str = "".join(map(str, result)).lstrip("0")

    return result_str if result_str else "0"


num1 = "2"
num2 = "3"
print(multiply(num1, num2))  # "6"

```

## 166. Fraction to Recurring Decimal

-   [LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/) | [LeetCode CH](https://leetcode.cn/problems/fraction-to-recurring-decimal/) (Medium)

-   Tags: hash table, math, string

```python title="166. Fraction to Recurring Decimal - Python Solution"
# Math
def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    res = []

    if (numerator < 0) ^ (denominator < 0):
        res.append("-")

    numerator, denominator = abs(numerator), abs(denominator)

    # Integer part
    res.append(str(numerator // denominator))
    remainder = numerator % denominator

    if remainder == 0:
        return "".join(res)

    res.append(".")

    # Dictionary to store remainders and their corresponding indices
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            res.insert(remainder_map[remainder], "(")
            res.append(")")
            break

        remainder_map[remainder] = len(res)
        remainder *= 10
        res.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(res)


numerator = 4
denominator = 333
print(fractionToDecimal(numerator, denominator))  # 0.(012)

```
