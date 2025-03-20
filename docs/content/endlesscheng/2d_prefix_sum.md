---
comments: True
---

# 2D Prefix Sum

## Table of Contents

- [x] [304. Range Sum Query 2D - Immutable](https://leetcode.cn/problems/range-sum-query-2d-immutable/) (Medium)
- [ ] [1314. Matrix Block Sum](https://leetcode.cn/problems/matrix-block-sum/) (Medium)
- [ ] [3070. Count Submatrices with Top-Left Element and Sum Less Than k](https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) (Medium)
- [ ] [1738. Find Kth Largest XOR Coordinate Value](https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/) (Medium)
- [ ] [3212. Count Submatrices With Equal Frequency of X and Y](https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/) (Medium)
- [ ] [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) (Medium)
- [ ] [221. Maximal Square](https://leetcode.cn/problems/maximal-square/) (Medium)
- [ ] [1277. Count Square Submatrices with All Ones](https://leetcode.cn/problems/count-square-submatrices-with-all-ones/) (Medium)
- [ ] [1504. Count Submatrices With All Ones](https://leetcode.cn/problems/count-submatrices-with-all-ones/) (Medium)
- [ ] [1074. Number of Submatrices That Sum to Target](https://leetcode.cn/problems/number-of-submatrices-that-sum-to-target/) (Hard)
- [ ] [3148. Maximum Difference Score in a Grid](https://leetcode.cn/problems/maximum-difference-score-in-a-grid/) (Medium)

## 304. Range Sum Query 2D - Immutable

-   [LeetCode](https://leetcode.com/problems/range-sum-query-2d-immutable/) | [LeetCode CH](https://leetcode.cn/problems/range-sum-query-2d-immutable/) (Medium)

-   Tags: array, design, matrix, prefix sum

```python title="304. Range Sum Query 2D - Immutable - Python Solution"
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return None

        self.sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.sum[i - 1][j]
                    + self.sum[i][j - 1]
                    - self.sum[i - 1][j - 1]  # to avoid double counting
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.sum[row2 + 1][col2 + 1]
            - self.sum[row1][col2 + 1]
            - self.sum[row2 + 1][col1]
            + self.sum[row1][col1]
        )


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]
obj = NumMatrix(matrix)
assert obj.sumRegion(2, 1, 4, 3) == 8
assert obj.sumRegion(1, 1, 2, 2) == 11
assert obj.sumRegion(1, 2, 2, 4) == 12
print("PASSED")

```

## 1314. Matrix Block Sum

-   [LeetCode](https://leetcode.com/problems/matrix-block-sum/) | [LeetCode CH](https://leetcode.cn/problems/matrix-block-sum/) (Medium)

-   Tags: array, matrix, prefix sum

## 3070. Count Submatrices with Top-Left Element and Sum Less Than k

-   [LeetCode](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) | [LeetCode CH](https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) (Medium)

-   Tags: array, matrix, prefix sum

## 1738. Find Kth Largest XOR Coordinate Value

-   [LeetCode](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/) | [LeetCode CH](https://leetcode.cn/problems/find-kth-largest-xor-coordinate-value/) (Medium)

-   Tags: array, divide and conquer, bit manipulation, sorting, heap priority queue, matrix, prefix sum, quickselect

## 3212. Count Submatrices With Equal Frequency of X and Y

-   [LeetCode](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/) | [LeetCode CH](https://leetcode.cn/problems/count-submatrices-with-equal-frequency-of-x-and-y/) (Medium)

-   Tags: array, matrix, prefix sum

## 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

-   [LeetCode](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) | [LeetCode CH](https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/) (Medium)

-   Tags: array, binary search, matrix, prefix sum

## 221. Maximal Square

-   [LeetCode](https://leetcode.com/problems/maximal-square/) | [LeetCode CH](https://leetcode.cn/problems/maximal-square/) (Medium)

-   Tags: array, dynamic programming, matrix

## 1277. Count Square Submatrices with All Ones

-   [LeetCode](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | [LeetCode CH](https://leetcode.cn/problems/count-square-submatrices-with-all-ones/) (Medium)

-   Tags: array, dynamic programming, matrix

## 1504. Count Submatrices With All Ones

-   [LeetCode](https://leetcode.com/problems/count-submatrices-with-all-ones/) | [LeetCode CH](https://leetcode.cn/problems/count-submatrices-with-all-ones/) (Medium)

-   Tags: array, dynamic programming, stack, matrix, monotonic stack

## 1074. Number of Submatrices That Sum to Target

-   [LeetCode](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) | [LeetCode CH](https://leetcode.cn/problems/number-of-submatrices-that-sum-to-target/) (Hard)

-   Tags: array, hash table, matrix, prefix sum

## 3148. Maximum Difference Score in a Grid

-   [LeetCode](https://leetcode.com/problems/maximum-difference-score-in-a-grid/) | [LeetCode CH](https://leetcode.cn/problems/maximum-difference-score-in-a-grid/) (Medium)

-   Tags: array, dynamic programming, matrix
