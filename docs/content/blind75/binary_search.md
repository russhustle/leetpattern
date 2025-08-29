---
comments: True
---

# Binary Search

## Table of Contents

- [x] [153. Find Minimum in Rotated Sorted Array](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) (Medium)
- [x] [33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)

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
