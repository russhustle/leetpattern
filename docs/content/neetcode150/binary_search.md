---
comments: True
---

# Binary Search

## Table of Contents

- [x] [704. Binary Search](https://leetcode.cn/problems/binary-search/) (Easy)
- [x] [74. Search a 2D Matrix](https://leetcode.cn/problems/search-a-2d-matrix/) (Medium)
- [x] [875. Koko Eating Bananas](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)
- [x] [153. Find Minimum in Rotated Sorted Array](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) (Medium)
- [x] [33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)
- [x] [981. Time Based Key-Value Store](https://leetcode.cn/problems/time-based-key-value-store/) (Medium)
- [x] [4. Median of Two Sorted Arrays](https://leetcode.cn/problems/median-of-two-sorted-arrays/) (Hard)

## 704. Binary Search

-   [LeetCode](https://leetcode.com/problems/binary-search/) | [LeetCode CH](https://leetcode.cn/problems/binary-search/) (Easy)

-   Tags: array, binary search
- Implement binary search algorithm.

```python title="704. Binary Search - Python Solution"
from typing import List


# Binary Search [left, right]
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


# Binary Search [left, right)
def search_half_open(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            return mid

    return -1


# Binary Search (left, right)
def search_open_interval(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            return mid

    return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert search(nums, target) == 4
    assert search_half_open(nums, target) == 4
    assert search_open_interval(nums, target) == 4

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

## 875. Koko Eating Bananas

-   [LeetCode](https://leetcode.com/problems/koko-eating-bananas/) | [LeetCode CH](https://leetcode.cn/problems/koko-eating-bananas/) (Medium)

-   Tags: array, binary search
-   Koko loves to eat bananas. She wants to eat all the bananas within `H` hours. Each pile has a number of bananas. The `i-th` pile has `piles[i]` bananas. Return the minimum integer `K` such that she can eat all the bananas within `H` hours.

```python title="875. Koko Eating Bananas - Python Solution"
from typing import List


# Binary Search
def minEatingSpeed(piles: List[int], h: int) -> int:
    def canEat(piles, k, h):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h

    left, right = 1, max(piles)

    while left <= right:
        mid = left + (right - left) // 2

        if canEat(piles, mid, h):
            right = mid - 1
        else:
            left = mid + 1

    return left


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))  # 4

```

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

## 981. Time Based Key-Value Store

-   [LeetCode](https://leetcode.com/problems/time-based-key-value-store/) | [LeetCode CH](https://leetcode.cn/problems/time-based-key-value-store/) (Medium)

-   Tags: hash table, string, binary search, design
```python title="981. Time Based Key-Value Store - Python Solution"
from collections import defaultdict


# Binary Search
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        self.times = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        tmp = self.keys[key]

        left, right = 0, len(tmp) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if tmp[mid] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return self.times[tmp[right]] if right >= 0 else ""


obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))  # bar
print(obj.get("foo", 3))  # bar
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))  # bar2
print(obj.get("foo", 5))  # bar2

```

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

