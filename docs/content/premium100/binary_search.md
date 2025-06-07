---
comments: True
---

# Binary Search

## Table of Contents

- [x] [1228. Missing Number In Arithmetic Progression](https://leetcode.cn/problems/missing-number-in-arithmetic-progression/) (Easy) 👑
- [ ] [1060. Missing Element in Sorted Array](https://leetcode.cn/problems/missing-element-in-sorted-array/) (Medium) 👑
- [ ] [1533. Find the Index of the Large Integer](https://leetcode.cn/problems/find-the-index-of-the-large-integer/) (Medium) 👑
- [ ] [1150. Check If a Number Is Majority Element in a Sorted Array](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy) 👑
- [ ] [1231. Divide Chocolate](https://leetcode.cn/problems/divide-chocolate/) (Hard) 👑
- [ ] [644. Maximum Average Subarray II](https://leetcode.cn/problems/maximum-average-subarray-ii/) (Hard) 👑

## 1228. Missing Number In Arithmetic Progression

-   [LeetCode](https://leetcode.com/problems/missing-number-in-arithmetic-progression/) | [LeetCode CH](https://leetcode.cn/problems/missing-number-in-arithmetic-progression/) (Easy)

-   Tags: array, math

```python title="1228. Missing Number In Arithmetic Progression - Python Solution"
from typing import List


def missingNumber(arr: List[int]) -> int:
    n = len(arr)
    s1 = (arr[0] + arr[-1]) * (n + 1) // 2
    s2 = sum(arr)
    return s1 - s2


# Binary Search
def missingNumberBS(arr: List[int]) -> int:
    n = len(arr)
    diff = (arr[-1] - arr[0]) // n

    left, right = 0, n - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == arr[0] + mid * diff:
            left = mid + 1
        else:
            right = mid

    return arr[0] + left * diff


if __name__ == "__main__":
    assert missingNumber([5, 7, 11, 13]) == 9
    assert missingNumber([15, 13, 12]) == 14
    assert missingNumber([1, 3]) == 2
    assert missingNumberBS([5, 7, 11, 13]) == 9
    assert missingNumberBS([15, 13, 12]) == 14
    assert missingNumberBS([1, 3]) == 2

```

## 1060. Missing Element in Sorted Array

-   [LeetCode](https://leetcode.com/problems/missing-element-in-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/missing-element-in-sorted-array/) (Medium)

-   Tags: array, binary search
## 1533. Find the Index of the Large Integer

-   [LeetCode](https://leetcode.com/problems/find-the-index-of-the-large-integer/) | [LeetCode CH](https://leetcode.cn/problems/find-the-index-of-the-large-integer/) (Medium)

-   Tags: array, binary search, interactive
## 1150. Check If a Number Is Majority Element in a Sorted Array

-   [LeetCode](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) | [LeetCode CH](https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) (Easy)

-   Tags: array, binary search
## 1231. Divide Chocolate

-   [LeetCode](https://leetcode.com/problems/divide-chocolate/) | [LeetCode CH](https://leetcode.cn/problems/divide-chocolate/) (Hard)

-   Tags: array, binary search
## 644. Maximum Average Subarray II

-   [LeetCode](https://leetcode.com/problems/maximum-average-subarray-ii/) | [LeetCode CH](https://leetcode.cn/problems/maximum-average-subarray-ii/) (Hard)

-   Tags: array, binary search, prefix sum
