---
comments: True
---

# Array

- [x] [414. Third Maximum Number](https://leetcode.cn/problems/third-maximum-number/) (Easy)
- [x] [169. Majority Element](https://leetcode.cn/problems/majority-element/) (Easy)
- [x] [2022. Convert 1D Array Into 2D Array](https://leetcode.cn/problems/convert-1d-array-into-2d-array/) (Easy)
- [x] [54. Spiral Matrix](https://leetcode.cn/problems/spiral-matrix/) (Medium)
- [x] [59. Spiral Matrix II](https://leetcode.cn/problems/spiral-matrix-ii/) (Medium)

## 414. Third Maximum Number

-   [LeetCode](https://leetcode.com/problems/third-maximum-number/) | [LeetCode CH](https://leetcode.cn/problems/third-maximum-number/) (Easy)

-   Tags: array, sorting
-   Return the third maximum number in an array. If the third maximum does not exist, return the maximum number.

```python title="414. Third Maximum Number - Python Solution"
from typing import List


# Sort
def thirdMaxSort(nums: List[int]) -> int:
    nums = list(set(nums))
    nums.sort(reverse=True)

    return nums[2] if len(nums) >= 3 else nums[0]


# Compare
def thirdMaxCompare(nums: List[int]) -> int:
    first, second, third = float("-inf"), float("-inf"), float("-inf")

    for num in nums:
        if num > first:
            first, second, third = num, first, second
        elif first > num > second:
            second, third = num, second
        elif second > num > third:
            third = num

    return third if third != float("-inf") else first


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Sort     |    O(NlogN)     |     O(N)     |
# |  Compare    |       O(N)      |     O(1)     |
# |-------------|-----------------|--------------|


print(thirdMaxSort([3, 2, 1]))  # 1
print(thirdMaxCompare([3, 2, 1]))  # 1

```

## 169. Majority Element

-   [LeetCode](https://leetcode.com/problems/majority-element/) | [LeetCode CH](https://leetcode.cn/problems/majority-element/) (Easy)

-   Tags: array, hash table, divide and conquer, sorting, counting
-   Return the majority element in an array. The majority element is the element that appears more than `n // 2` times.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7pnhv842keE?si=fBYlNfKzdkiLgkF1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

| `num` | `count` | `res` |
| ----- | ------- | ----- |
| 2     | 1       | 2     |
| 2     | 2       | 2     |
| 1     | 1       | 2     |
| 1     | 0       | 2     |
| 1     | 1       | 1     |
| 2     | 0       | 1     |
| 2     | 1       | 2     |

```python title="169. Majority Element - Python Solution"
from collections import defaultdict
from typing import List


# Hash Map
def majorityElementHashMap(nums: List[int]) -> int:
    n = len(nums)
    freq = defaultdict(int)

    for num in nums:
        freq[num] += 1
        if freq[num] > n // 2:
            return num


# Array - Boyer-Moore Voting Algorithm
def majorityElementArray(nums: List[int]) -> int:
    res = None
    count = 0

    for num in nums:
        if count == 0:
            res = num
        count += 1 if num == res else -1

    return res


# | Algorithm | Time Complexity | Space Complexity |
# |-----------|-----------------|------------------|
# | HashMap   | O(N)            | O(N)             |
# | Array     | O(N)            | O(1)             |
# |-----------|-----------------|------------------|


nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElementArray(nums))  # 2
print(majorityElementHashMap(nums))  # 2

```

## 2022. Convert 1D Array Into 2D Array

-   [LeetCode](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | [LeetCode CH](https://leetcode.cn/problems/convert-1d-array-into-2d-array/) (Easy)

-   Tags: array, matrix, simulation

```python title="2022. Convert 1D Array Into 2D Array - Python Solution"
from typing import List


# Brute Force
def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
        return []
    array = []

    for i in range(m):
        row = original[n * i : n * (i + 1)]
        array.append(row)

    return array


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |  Brute     |  O(m)  |  O(1)   |
# |------------|--------|---------|


original = [1, 2, 3, 4]
m = 2
n = 2

print(construct2DArray(original, m, n))  # [[1, 2], [3, 4]]

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

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:

            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


# |-------------|-----------------|--------------|
# |  Approach   |      Time       |    Space     |
# |-------------|-----------------|--------------|
# |    Naive    |      O(N)       |     O(1)     |
# |-------------|-----------------|--------------|


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]

```

## 59. Spiral Matrix II

-   [LeetCode](https://leetcode.com/problems/spiral-matrix-ii/) | [LeetCode CH](https://leetcode.cn/problems/spiral-matrix-ii/) (Medium)

-   Tags: array, matrix, simulation
-   Return a square matrix filled with elements from 1 to n^2 in spiral order.

```python title="59. Spiral Matrix II - Python Solution"
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

```
