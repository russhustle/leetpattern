---
comments: True
---

# Binary Search

## Table of Contents

- [x] [704. Binary Search](https://leetcode.cn/problems/binary-search/) (Easy)
- [x] [278. First Bad Version](https://leetcode.cn/problems/first-bad-version/) (Easy)
- [x] [33. Search in Rotated Sorted Array](https://leetcode.cn/problems/search-in-rotated-sorted-array/) (Medium)
- [x] [981. Time Based Key-Value Store](https://leetcode.cn/problems/time-based-key-value-store/) (Medium)
- [ ] [1235. Maximum Profit in Job Scheduling](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/) (Hard)

## 704. Binary Search

-   [LeetCode](https://leetcode.com/problems/binary-search/) | [LeetCode CH](https://leetcode.cn/problems/binary-search/) (Easy)

-   Tags: array, binary search
-   Implement binary search algorithm.

```python title="704. Binary Search - Python Solution"
from typing import List


# Binary Search
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


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))  # 4

```

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

## 1235. Maximum Profit in Job Scheduling

-   [LeetCode](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | [LeetCode CH](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/) (Hard)

-   Tags: array, binary search, dynamic programming, sorting
