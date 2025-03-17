---
comments: True
---

# Binary Search Others

- [x] [69. Sqrt(x)](https://leetcode.cn/problems/sqrtx/) (Easy)
- [x] [74. Search a 2D Matrix](https://leetcode.cn/problems/search-a-2d-matrix/) (Medium)
- [x] [240. Search a 2D Matrix II](https://leetcode.cn/problems/search-a-2d-matrix-ii/) (Medium)
- [ ] [2476. Closest Nodes Queries in a Binary Search Tree](https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/) (Medium)
- [x] [278. First Bad Version](https://leetcode.cn/problems/first-bad-version/) (Easy)
- [ ] [374. Guess Number Higher or Lower](https://leetcode.cn/problems/guess-number-higher-or-lower/) (Easy)
- [ ] [162. Find Peak Element](https://leetcode.cn/problems/find-peak-element/) (Medium)
- [ ] [1901. Find a Peak Element II](https://leetcode.cn/problems/find-a-peak-element-ii/) (Medium)
- [ ] [852. Peak Index in a Mountain Array](https://leetcode.cn/problems/peak-index-in-a-mountain-array/) (Medium)
- [ ] [1095. Find in Mountain Array](https://leetcode.cn/problems/find-in-mountain-array/) (Hard)
- [x] [153. Find Minimum in Rotated Sorted Array](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) (Medium)
- [ ] [154. Find Minimum in Rotated Sorted Array II](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/) (Hard)
- [x] [33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)
- [ ] [81. Search in Rotated Sorted Array II](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/) (Medium)
- [x] [222. Count Complete Tree Nodes](https://leetcode.cn/problems/count-complete-tree-nodes/) (Easy)
- [ ] [1539. Kth Missing Positive Number](https://leetcode.cn/problems/kth-missing-positive-number/) (Easy)
- [ ] [540. Single Element in a Sorted Array](https://leetcode.cn/problems/single-element-in-a-sorted-array/) (Medium)
- [x] [4. Median of Two Sorted Arrays](https://leetcode.cn/problems/median-of-two-sorted-arrays/) (Hard)
- [ ] [1064. Fixed Point](https://leetcode.cn/problems/fixed-point/) (Easy) 👑
- [ ] [702. Search in a Sorted Array of Unknown Size](https://leetcode.cn/problems/search-in-a-sorted-array-of-unknown-size/) (Medium) 👑
- [ ] [2936. Number of Equal Numbers Blocks](https://leetcode.cn/problems/number-of-equal-numbers-blocks/) (Medium) 👑
- [ ] [1060. Missing Element in Sorted Array](https://leetcode.cn/problems/missing-element-in-sorted-array/) (Medium) 👑
- [ ] [1198. Find Smallest Common Element in All Rows](https://leetcode.cn/problems/find-smallest-common-element-in-all-rows/) (Medium) 👑
- [ ] [1428. Leftmost Column with at Least a One](https://leetcode.cn/problems/leftmost-column-with-at-least-a-one/) (Medium) 👑
- [ ] [1533. Find the Index of the Large Integer](https://leetcode.cn/problems/find-the-index-of-the-large-integer/) (Medium) 👑
- [ ] [2387. Median of a Row Wise Sorted Matrix](https://leetcode.cn/problems/median-of-a-row-wise-sorted-matrix/) (Medium) 👑
- [ ] [302. Smallest Rectangle Enclosing Black Pixels](https://leetcode.cn/problems/smallest-rectangle-enclosing-black-pixels/) (Hard) 👑

## 69. Sqrt(x)

-   [LeetCode](https://leetcode.com/problems/sqrtx/) | [LeetCode CH](https://leetcode.cn/problems/sqrtx/) (Easy)

-   Tags: math, binary search

```python title="69. Sqrt(x) - Python Solution"
# Left Right Pointers
def mySqrt(x: int) -> int:
    """Returns the square root of a number."""
    if x < 2:
        return x

    left, right = 0, x // 2

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1


x = 8
print(mySqrt(x))  # 2

```

## 74. Search a 2D Matrix

-   [LeetCode](https://leetcode.com/problems/search-a-2d-matrix/) | [LeetCode CH](https://leetcode.cn/problems/search-a-2d-matrix/) (Medium)

-   Tags: array, binary search, matrix

```python title="74. Search a 2D Matrix - Python Solution"
from typing import List


# Binary Search
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = left + (right - left) // 2
        x = matrix[mid // n][mid % n]

        if x < target:
            left = mid + 1
        elif x > target:
            right = mid - 1
        else:
            return True

    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(searchMatrix(matrix, target))  # True

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

## 2476. Closest Nodes Queries in a Binary Search Tree

-   [LeetCode](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) | [LeetCode CH](https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/) (Medium)

-   Tags: array, binary search, tree, depth first search, binary search tree, binary tree

## 278. First Bad Version

-   [LeetCode](https://leetcode.com/problems/first-bad-version/) | [LeetCode CH](https://leetcode.cn/problems/first-bad-version/) (Easy)

-   Tags: binary search, interactive
-   Find the first bad version given a function `isBadVersion`.

```python title="278. First Bad Version - Python Solution"
# Binary Search
def firstBadVersion(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


def isBadVersion(version: int) -> bool:
    pass

```

## 374. Guess Number Higher or Lower

-   [LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/) | [LeetCode CH](https://leetcode.cn/problems/guess-number-higher-or-lower/) (Easy)

-   Tags: binary search, interactive

## 162. Find Peak Element

-   [LeetCode](https://leetcode.com/problems/find-peak-element/) | [LeetCode CH](https://leetcode.cn/problems/find-peak-element/) (Medium)

-   Tags: array, binary search

## 1901. Find a Peak Element II

-   [LeetCode](https://leetcode.com/problems/find-a-peak-element-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-a-peak-element-ii/) (Medium)

-   Tags: array, binary search, matrix

## 852. Peak Index in a Mountain Array

-   [LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/) | [LeetCode CH](https://leetcode.cn/problems/peak-index-in-a-mountain-array/) (Medium)

-   Tags: array, binary search

## 1095. Find in Mountain Array

-   [LeetCode](https://leetcode.com/problems/find-in-mountain-array/) | [LeetCode CH](https://leetcode.cn/problems/find-in-mountain-array/) (Hard)

-   Tags: array, binary search, interactive

## 153. Find Minimum in Rotated Sorted Array

-   [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) (Medium)

-   Tags: array, binary search

```python title="153. Find Minimum in Rotated Sorted Array - Python Solution"
from typing import List


# Binary Search
def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[right]


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))  # 0

```

## 154. Find Minimum in Rotated Sorted Array II

-   [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) | [LeetCode CH](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/) (Hard)

-   Tags: array, binary search

## 33. Search in Rotated Sorted Array

-   [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)

-   Tags: array, binary search

```python title="33. Search in Rotated Sorted Array - Python Solution"
from typing import List


# Binary Search
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search(nums, target))  # 4

```

## 81. Search in Rotated Sorted Array II

-   [LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) | [LeetCode CH](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/) (Medium)

-   Tags: array, binary search

## 222. Count Complete Tree Nodes

-   [LeetCode](https://leetcode.com/problems/count-complete-tree-nodes/) | [LeetCode CH](https://leetcode.cn/problems/count-complete-tree-nodes/) (Easy)

-   Tags: binary search, bit manipulation, tree, binary tree

```python title="222. Count Complete Tree Nodes - Python Solution"
from collections import deque
from typing import Optional

from binarytree import Node as TreeNode
from binarytree import build


# Recursive
def countNodesRecursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    num = 1 + countNodesRecursive(root.left) + countNodesRecursive(root.right)

    return num


# Iterative
def countNodesIterative(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    q = deque([root])
    count = 0

    while q:
        n = len(q)

        for _ in range(n):
            node = q.popleft()
            count += 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return count


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# | Recursive  |  O(n)  |  O(n)   |
# | Iterative  |  O(n)  |  O(n)   |
# |------------|--------|---------|

root = [1, 2, 3, 4, 5, 6]
root = build(root)
print(root)
#     __1__
#    /     \
#   2       3
#  / \     /
# 4   5   6
print(countNodesRecursive(root))  # 6
print(countNodesIterative(root))  # 6

```

## 1539. Kth Missing Positive Number

-   [LeetCode](https://leetcode.com/problems/kth-missing-positive-number/) | [LeetCode CH](https://leetcode.cn/problems/kth-missing-positive-number/) (Easy)

-   Tags: array, binary search

## 540. Single Element in a Sorted Array

-   [LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/single-element-in-a-sorted-array/) (Medium)

-   Tags: array, binary search

## 4. Median of Two Sorted Arrays

-   [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/) | [LeetCode CH](https://leetcode.cn/problems/median-of-two-sorted-arrays/) (Hard)

-   Tags: array, binary search, divide and conquer

```python title="4. Median of Two Sorted Arrays - Python Solution"
from typing import List


# Brute Force
def findMedianSortedArraysBF(nums1: List[int], nums2: List[int]) -> float:
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        return nums[n // 2]


# Binary Search
def findMedianSortedArraysBS(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums2[j - 1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2


# |--------------|-----------------|--------------|
# | Approach     | Time            | Space        |
# |--------------|-----------------|--------------|
# | Brute Force  | O((n+m)log(n+m))| O(n+m)       |
# | Binary Search| O(log(min(n,m)))| O(1)         |
# |--------------|-----------------|--------------|


nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArraysBF(nums1, nums2))  # 2.0
print(findMedianSortedArraysBS(nums1, nums2))  # 2.0

```

## 1064. Fixed Point

-   [LeetCode](https://leetcode.com/problems/fixed-point/) | [LeetCode CH](https://leetcode.cn/problems/fixed-point/) (Easy)

-   Tags: array, binary search

## 702. Search in a Sorted Array of Unknown Size

-   [LeetCode](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) | [LeetCode CH](https://leetcode.cn/problems/search-in-a-sorted-array-of-unknown-size/) (Medium)

-   Tags: array, binary search, interactive

## 2936. Number of Equal Numbers Blocks

-   [LeetCode](https://leetcode.com/problems/number-of-equal-numbers-blocks/) | [LeetCode CH](https://leetcode.cn/problems/number-of-equal-numbers-blocks/) (Medium)

-   Tags: array, binary search, interactive

## 1060. Missing Element in Sorted Array

-   [LeetCode](https://leetcode.com/problems/missing-element-in-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/missing-element-in-sorted-array/) (Medium)

-   Tags: array, binary search

## 1198. Find Smallest Common Element in All Rows

-   [LeetCode](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) | [LeetCode CH](https://leetcode.cn/problems/find-smallest-common-element-in-all-rows/) (Medium)

-   Tags: array, hash table, binary search, matrix, counting

## 1428. Leftmost Column with at Least a One

-   [LeetCode](https://leetcode.com/problems/leftmost-column-with-at-least-a-one/) | [LeetCode CH](https://leetcode.cn/problems/leftmost-column-with-at-least-a-one/) (Medium)

-   Tags: array, binary search, matrix, interactive

## 1533. Find the Index of the Large Integer

-   [LeetCode](https://leetcode.com/problems/find-the-index-of-the-large-integer/) | [LeetCode CH](https://leetcode.cn/problems/find-the-index-of-the-large-integer/) (Medium)

-   Tags: array, binary search, interactive

## 2387. Median of a Row Wise Sorted Matrix

-   [LeetCode](https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/) | [LeetCode CH](https://leetcode.cn/problems/median-of-a-row-wise-sorted-matrix/) (Medium)

-   Tags: array, binary search, matrix

## 302. Smallest Rectangle Enclosing Black Pixels

-   [LeetCode](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/) | [LeetCode CH](https://leetcode.cn/problems/smallest-rectangle-enclosing-black-pixels/) (Hard)

-   Tags: array, binary search, depth first search, breadth first search, matrix
