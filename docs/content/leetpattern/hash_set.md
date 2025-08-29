---
comments: True
---

# Hash Set

## Table of Contents

- [x] [349. Intersection of Two Arrays](https://leetcode.cn/problems/intersection-of-two-arrays/) (Easy)

## 349. Intersection of Two Arrays

-   [LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/) | [LeetCode CH](https://leetcode.cn/problems/intersection-of-two-arrays/) (Easy)

-   Tags: array, hash table, two pointers, binary search, sorting
```python title="349. Intersection of Two Arrays - Python Solution"
from typing import List


# Set
def intersectionSet(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)


# Hash
def intersectionHash(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)


# |------------|------- |---------|
# |  Approach  |  Time  |  Space  |
# |------------|--------|---------|
# |     Set    | O(n+m) |  O(n+m) |
# |    Hash    | O(n+m) |   O(n)  |
# |------------|--------|---------|


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersectionSet(nums1, nums2))  # [2]
print(intersectionHash(nums1, nums2))  # [2]

```
